# B001 | Conflict Resolution — Technical Disagreement

**Category:** Conflict Resolution / Leadership  
**Difficulty:** Medium  
**Time Limit:** 5 minutes (spoken) | 10 minutes (written)  
**Commonly asked at:** Amazon, Google, Meta, Microsoft

---

## The Question

> **"Tell me about a time you had a significant technical disagreement with a teammate or your team. How did you handle it, and what was the outcome?"**

---

## Follow-up Questions

The interviewer may probe with any of these. Prepare for all of them:

1. How did you make sure the other person felt heard?
2. What would you do differently if you were in that situation again?
3. What if your manager sided with the other person — how would you respond?
4. Was this a case where you had to "disagree and commit"? How did that feel?

---

---

## 3. Candidate's Iterative Responses (STAR Method)

### Draft 1 (2026-03-24 02:02)

**Situation:**
在趨勢科技 (Trend Micro) 擔任 QA 時，負責 DLP/Device Control 功能的測試。該功能的核心是偵測任何 USB 設備的操作是否違反公司安全 Policy。

**Task:**
當時面臨最大的瓶頸是「USB 裝置操作的自動化」。我們需要一個方案來模擬不同作業系統 (VM) 下的 USB 熱拔插 (Hot-plug)，且必須能大規模整合進自動化測試流程中。

**Action:**
我針對三種技術方案進行了評估與對比：
1. **IOMMU (Hardware Passthrough):** 研究後發現它只能將整顆 USB Controller 轉移給 VM，無法模擬單個 USB Device，且擴充性極差。
2. **Digi AnywhereUSB:** 硬體解決方案，穩定但成本極其昂貴（一台 4-port Hub 當時報價約數千美金）。
3. **USB/IP (Open Source):** 軟體過網路傳送 USB 數據。

**Conflict:** 團隊中有資深同事強烈反對使用 USB/IP，理由是 Network Jitter 可能導致連線不穩。
**Resolution:** 我透過數據說服他們，Jitter 主要影響的是影音串流（實時同步），而我們的測試場景是「熱拔插偵測」與「檔案讀寫」，對微秒級的延遲不敏感。最終我成功推動了 USB/IP 方案的導入。

**Result:**
成功建立了 USB 自動化測試基礎設施。不僅節省了數萬美金的硬體購置成本，還實現了 7x24 小時的無人值守 USB Policy 驗證，TestCase 覆蓋率提升了 X%。

---

## 4. Mentor's Feedback & Scoring

### Draft 2 (Finalized — 2026-03-24)

**Situation:**
在趨勢科技負責 DLP (Data Loss Prevention) 產品的 USB 入口防護測試。我們需要自動化驗證「Device Control Policy」，確保當不同品牌、型號的 USB 裝置接入時，系統能精準執行攔截或放行。

**Task:**
核心挑戰在於 **「如何在虛擬化測試環境 (VM) 中大規模模擬真實 USB 物理行為」**。傳統手動插拔無法滿足 7x24 的 CI/CD 需求，且必須支持同時並發的上百台 VM 測試。

**Action:**
1. **方案研究與技術辯論：** 當時團隊提議使用 **IOMMU (Hardware Passthrough)**。我透過深入研究 IOMMU 與 VHCI Controller 的底層機制，證實它只能物理移交整個 Controller 而無法靈活模擬單體 Device 實例。
2. **成本管理：** 評估了工業級 **Digi AnywhereUSB (8-port)**，單台成本約 **60,000 TWD**。我提議改用基於 **USB/IP 協議** 的替代硬體方案，單台成本降至 **20,000 TWD**，直接節省了 66% 的購置預算。
3. **解決團隊矛盾：** 面對同事對 Network Jitter 的質疑，我分析了 USB 報文類別，指出「非同步傳輸 (Bulk Transfer)」在我們的 Policy 偵測場景中遠比「同步傳輸 (Isochronous)」具備更高的容錯性，並以實驗數據消弭疑慮。

**Result:**
1. **成本節省：** 在部署上百台 VM 的規模下，累計省下近百萬元的硬體預算。
2. **規模化產出：** 系統穩定支撐了 8 個品牌的手機與 4 款主流 Android 設備的自動化測試。
3. **效率提升：** 將原本需要 2 名人力全職手動測試的項目，轉化為 100% 無人值守自動化。

---

## 4. Mentor's Feedback & Scoring

### Final Assessment: 3.8 / 4 (Exceptional)

**點評：**
這是一個標準的 **「Senior QA / Lead」** 等級答案。你展現了：
- **底層研究能力** (IOMMU vs USB/IP)
- **商業意識** (66% Cost reduction)
- **架構設計力** (Scale to 100+ VMs)

你在聯想的面試中，如果能冷靜地講出這套邏輯與數據，對方會直接把你視為「能解決問題的實戰派」。

---

---

## Scoring Rubric

| Dimension | 1 — Poor | 2 — Fair | 3 — Good | 4 — Exceptional |
|---|---|---|---|---|
| **Communication** | Vague, emotional tone | Described what happened but unclear | Clear structure, professional tone | Concise, data-backed, mature |
| **Conflict Handling** | Avoided or escalated | Waited for others to resolve | Proactively engaged with logic | Led resolution with evidence + empathy |
| **Outcome** | No resolution mentioned | Outcome unclear | Clear resolution described | Quantified impact + lessons learned |

---

## Red Flags That Will Tank Your Score

- Blaming the other person without acknowledging their perspective.
- Saying "we decided" instead of "I specifically did X."
- Picking a trivial disagreement (e.g., code style, variable naming).
- No data or logical reasoning behind your position.
- No mention of what you learned or how you'd handle it better.

---

## Tips for a 4-Point Answer

- **Use "I", not "we"** — the interviewer wants to know YOUR contribution.
- **Show your reasoning process**: Did you run a benchmark? Write a comparison doc? Run a spike?
- **Demonstrate empathy**: Acknowledge the other person's valid points before countering.
- **End with scale**: What was the business or technical impact of the final decision?
