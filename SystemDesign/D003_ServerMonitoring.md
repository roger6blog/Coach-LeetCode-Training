# System Design Training Log: Day 3
## Topic: Server Monitoring Agent & Redfish API Integration

### 1. Challenge Context
**Scenario:** Lenovo ISG R&D Team.
**Task:** Design a Monitoring Agent that runs on a Data Center management node.
**Goal:** Periodically fetch health status (Fan speed, CPU temp, Power) from 5,000+ servers via **Redfish API**.

---

### 2. Interviewer's Questions (The Drill-down)

#### Q1: Redfish API Fundamentals
Redfish is based on what protocol and data format? Compared to IPMI, what are its primary advantages for Developers and QA Automation engineers?

#### Q2: Polling vs. Event Push
For real-time hardware failure alerts, would you use HTTP Polling or Redfish's Event Service (SSE/Webhooks)? Analyze the trade-offs in a distributed datacenter environment.

#### Q3: Scalability & Reliability
How do you handle concurrency for 5,000+ nodes? How do you prevent the Agent from hanging due to network latency or unresponsive nodes?

---

### 3. Candidate's Iterative Responses
*1.Redfish是基於HTTPS傳輸JSON的Restful API標準 跟IPMI比起來，他更能勝任收集大量機器資訊的高吞吐量場合，因為強制走HTTPS，安全性相對IPMI高很多，傳輸的命令用JSON也比IMPI更容易理解內容．適用於大型資料中心*

*2.在現代的分散式資料中心環境下，一個HTTP polling就是一個connection, 以資料中心的數量級這會是個連線數災難，它的好處是實作容易但系統負擔重，用Server Sent Event是較輕量化的選擇，缺點是實作較為複雜*

*3. 建立多個HTTPS server，前面掛一個Load balancer，根據每個HTTPS server的loading來指派請求到loading較輕的Server*

---

### 4. Mentor's Feedback & Refinement

#### Q1: Redfish vs IPMI (Passed)
點出了 **HTTPS/JSON** 的關鍵。Redfish 的 JSON 格式讓 QA 能直接用 Python `requests` 庫進行解析，不再需要調用晦澀的 `ipmitool` 二進制命令。這對聯想這種全球研發團隊的自動化測試流至關重要。

#### Q2: Polling vs Eventing (Passed)
理解了 Polling 的頻寬浪費問題。在實務上，Lenovo ISG 會使用 **Redfish Events (Sub/Pub)** 來處理「電源斷電」、「風扇停轉」等關鍵告警，而 Polling 僅用於「定時抓取數值（如：溫度趨勢）」。

#### Q3: 並發處理邏輯 (Critical Logic Gap!)
你的回答：「建立多個 HTTPS Server 掛 Load Balancer」。
**導師糾正：** 你的角色是「監控代理人 (Agent)」，這是一個 **Client (客戶端)** 行為。對 5,000 台伺服器發起請求時，Load Balancer 加在你前方是沒用的。

**聯想 ISG 等級的標準答案應該是：**
1. **Async I/O (非阻塞 IO)：** 使用 Python 的 `asyncio` 或 Go 的 `goroutine`。單台機器可以同時掛載數千個「非阻塞」的 HTTP 請求等待回傳。
2. **Task Queue (任務隊列)：** 使用 **Celery + RabbitMQ/Redis**。將「抓取伺服器 A 的資訊」視為一個 Task，分發給 10 個 Worker 節點同時執行，這樣負載就會均攤在管理網段中。
3. **Connection Pooling (連線池)：** 複用 TCP 連線，減少每次握手的負擔。

---
