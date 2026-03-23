# System Design Training Log: Day 2
## Topic: Distributed Logging & Tracing in Microservices

### 1. Challenge Context
**Scenario:** Netskope-like SASE architecture.
**Flow:** `Client -> API Gateway -> Auth Service -> Resource Manager -> Database`
**Problem:** Intermittent `500 Internal Server Error` at the Gateway with no stack trace in high-level logs.

---

### 2. Interviewer's Questions (The Drill-down)

#### Q1: Correlation ID (Trace ID)
How do you design an ID system to track a specific request across thousands of machines? Where is it generated? How is it propagated?

#### Q2: Log Aggregation (ELK/EFK Stack)
How do you centralize logs? Describe the flow and the three main components (Agent/Buffer/Search Engine) usually involved in such an architecture.

#### Q3: Log Testability (QA Perspective)
How do you verify the reliability of the logging system? Design an automated test case to prove that a failure in `Resource Manager` is correctly traceable from the `API Gateway`.

---

### 3. Candidate's Iterative Responses (18:21)
- **Trace ID:** 會在 API Gateway 生成一個 `X-TRACE-ID` 放在 Header 中往下傳，所有組件埋入一樣的 ID 即可追蹤資料流。
- **Aggregation:** 使用 Splunk 或 Grafana 這種集中式的日誌伺服器。
- **Testing:** 發送一個帶 Trace ID 的 Request，到 Resource Manager 檢查其 Header 是否含有該 ID。

---

### 4. Mentor's Feedback & Refinements
#### Q1: Trace ID (Passed)
邏輯正確，由 Gateway 作為 Entry Point 生成唯一 ID 是標準做法。在 Netskope 這類重視合規性的公司，這還能用來做 Request Rate Limiting 或 Audit Trail。

#### Q2: Log Aggregation (Needs Depth)
雖提到 Splunk/Grafana，但遺漏了關鍵的「日誌流架構」。
- **Agent (e.g. FluentBit/Logstash):** 負責從各容器收集、解析日誌。
- **Buffer/Queue (e.g. Kafka/Redis):** 這是高併發不可缺少的。如果 Log Server 瞬間塞爆，緩衝層能保證日誌不遺失、不阻塞你的核心業務 API。
- **Search Engine (e.g. Splunk/ElasticSearch):** 索引與持久化。

#### Q3: Log Testability (QA Logic Gap)
檢查「Header」只是在測 Service A 是否把變數傳給了 Service B。
**真正的日誌測試（QA for Logs）應該是：**
「執行 API 呼叫後，自動化腳本去對 Log API (如 Splunk API) 進行查詢，驗證在分散的五個服務中，是否**同時出現了**帶有同一 Trace ID 的五條日誌記錄。」這才是驗證「可觀測性」的自動化測試。

---

### 5. Implementation Deep Dive: The Log Pipeline
日誌伺服器不是「一台電腦」，而是一條不斷處理資料的「生產線」。在 Netskope 這種規模，實作邏輯如下：

#### A. 收集端 (Collector / Shipper)
- **Tool:** FluentBit / Filebeat (輕量型)
- **實作:** 在每個微服務容器旁放一個 Sidecar。它只負責一件事：監控 Log 檔案，一把有新行，就立刻把資料推出去。
- **重點:** 絕不在 App 程式碼裡同步寫 Log 到遠端，否則遠端一慢，App 就掛了。

#### B. 緩衝層 (Buffer / Queue)
- **Tool:** Kafka / Redis
- **實作:** 收集器把 Log 丟進 Kafka 的特定 Topic。
- **重點:** 這是系統的「保險絲」。當 Log 暴增時，Kafka 會把日誌穩穩存住，讓後端慢慢消化，不影響前方 App 運作。

#### C. 處理端 (Indexer / Transformer)
- **Tool:** Logstash / Fluentd
- **實作:** 從 Kafka 讀取原始日誌 (Raw text)，解析 JSON 格式，標註資料來源、時間戳。
- **重點:** 在這裡做「結構化」，方便後續搜尋。

#### D. 儲存與檢索 (Storage / Search Engine)
- **Tool:** ElasticSearch / OpenSearch / Splunk
- **實作:** 分散式索引資料庫。
- **重點:** 這是整套系統的靈魂。它能讓你查「過去一小時內，所有 `X-TRACE-ID: abcd` 的日誌」，並在 100ms 內回傳結果。

#### E. 視覺化 (Visualization)
- **Tool:** Kibana / Grafana
- **實作:** 給維運與 QA 用的儀表板。
