# 🕹️ PlayerPulse Analytics
### End-to-End Product Analytics Pipeline for Mobile Game Retention

## 🌟 Project Overview
This repository showcases a complete Data Analytics lifecycle for a mobile gaming studio. I engineered a synthetic dataset of **176,000+ player events**, architected a MySQL database to handle telemetry, and developed a high-fidelity Power BI dashboard to identify critical churn points and optimize marketing ROI.

## 🧠 The Business Challenge
In this scenario, a hypothetical mobile game studio observed high initial installs but stagnating long-term revenue. I was tasked with:
1. **Onboarding Funnel Analysis:** Pinpointing exactly where players drop off during their first session.
2. **Channel Quality Evaluation:** Comparing the retention and "quality" of players acquired via Organic search vs. Paid Ads (TikTok, Google, Facebook).

## 🛠️ Technical Implementation
* **Data Engineering (Python):** Developed `data_generator.py` using `pandas` and `numpy` to create a realistic telemetry stream with intentional behavioral skews (e.g., lower retention for paid ad cohorts).
* **Database Architecture (MySQL):** * Engineered complex queries utilizing **Conditional Aggregations** to build 5-stage funnel metrics.
    * Implemented an enterprise-grade **SQL View** (`vw_retention_data`) calculating Day-1 and Day-7 retention using advanced date math.
* **Product Visualization (Power BI):** Designed a studio-standard interactive dashboard using a dark-mode aesthetic to provide executives with a "pulse" on player health.

## 💡 Key Insights & Actionable Recommendations

### 1. The "Level 5" Core Loop Friction
* **Discovery:** While 85% of players successfully complete the tutorial, **only 34.8% reach Level 5**. 
* **Insight:** This 50%+ drop-off immediately after the tutorial suggests a severe difficulty spike or lack of engagement in the early core loop.
* **Recommendation:** Flatten the difficulty curve between Levels 3 and 5. Implement "Early Win" rewards to bridge the gap and increase the conversion to the Monetization stage (Store Page Views).

### 2. Organic vs. Paid Quality Gap
* **Discovery:** Organic players exhibit a **44.14% Day-1 Retention**, significantly outperforming TikTok Ads (29.59%) and Facebook Ads (29.28%).
* **Insight:** Paid acquisition is bringing in high volume but low-intent players who churn quickly. 
* **Recommendation:** Reallocate 15% of the marketing budget from Facebook Ads to App Store Optimization (ASO) and community-driven organic growth to improve the overall LTV (Lifetime Value) of the player base.

## 📂 Repository Structure
* `data_generator.py`: Python engine for telemetry modeling.
* `retention_logic.sql`: SQL View architecture for cohort analysis.
* `funnel_logic.sql`: Query logic for onboarding stage conversion.
* `PlayerPulse_Dashboard.pdf`: High-resolution export of the interactive BI tool.

---
**Author:** Tanya Jain
