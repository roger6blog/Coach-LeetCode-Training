# System Design Training Log: Day 1
## Topic: Load Testing & Connection Pooling

### 1. Challenge Context
**Scenario:** A core Authentication API is undergoing Load Testing.
**Traffic:** 10,000 RPS (Requests Per Second).
**Problem:** Random `502 Bad Gateway` and Timeouts under load. DB CPU/RAM remains low (10%).

---

### 2. Interviewer's Questions (The Drill-down)

#### Q1: Tooling Selection
Which tools are suitable for 10k RPS? (k6, Locust, JMeter, etc.)

#### Q2: High-Concurrency Metrics
Beyond CPU/RAM, what specific system metrics point to bottlenecks in high-concurrency? (Connection Pools, File Descriptors, Thread Pools).

#### Q3: 502 Bad Gateway Analysis
What does a 502 from Nginx typically signify in terms of Upstream health?

---

### 3. Key Concepts & Mentors' Feedback
- **Nginx 502:** Usually indicates the Upstream (Backend App) has crashed or failed to respond within time.
- **Connection Pool Exhaustion:** If the DB is idle (10% CPU) but API times out, the bottleneck is often the finite number of connections between App and DB. 
- **The PG-Bouncer Solution:** Use an intermediate Multiplexer to manage heavy TCP connections and reuse persistent DB processes.
- **Slow Query Optimization:** The root cause of "exhausted pools" is often a few queries taking seconds instead of milliseconds.

---

### 4. Evaluation (Netskope Tier)
**Grade:** Needs Improvement.
**Reason:** Initial response was too surface-level (Manual testing mindset). Moved towards architectural-level thinking by end of session.
