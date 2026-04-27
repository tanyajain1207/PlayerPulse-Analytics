# 🕹️ PlayerPulse Analytics
### End-to-End Product Analytics Pipeline for Mobile Game Retention

## 🌟 Project Overview
This repository showcases a complete Data Analytics lifecycle for a mobile gaming studio. I engineered a synthetic dataset of **176,000+ player events**, architected a MySQL database to handle telemetry, and developed a high-fidelity Power BI dashboard to identify critical churn points and optimize marketing ROI.

## 🧠 The Business Challenge
A hypothetical mobile game studio observed high initial installs but stagnating long-term revenue. I performed a deep-dive analysis to:
1. **Identify Onboarding Friction:** Pinpoint exactly where players drop off during their first 24 hours.
2. **Evaluate Channel Quality:** Compare the LTV potential of Organic traffic vs. Paid Ads (TikTok, Google, Facebook).

## 🛠️ Technical Implementation
* **Data Engineering (Python):** Developed `data_generator.py` to simulate realistic telemetry streams with behavioral skews (e.g., higher churn in specific ad cohorts).
* **SQL Architecture (MySQL):** * Designed **Database Views** (`vw_retention_data`) for high-performance BI reporting.
    * Utilized **Conditional Aggregations** and **Date Offsets** to calculate rolling cohort retention.
* **Visualization (Power BI):** Designed a studio-standard interactive dashboard using a dark-mode aesthetic to provide executives with a "pulse" on player health.

## 💡 Key Insights & Actionable Recommendations

### 1. The "Level 5" Core Loop Friction
* **Discovery:** While 85% of players complete the tutorial, **only 34.8% reach Level 5**. 
* **Recommendation:** Flatten the difficulty curve between Levels 3 and 5. Implement "Early Win" rewards to bridge the gap and increase the conversion to the Monetization stage.

### 2. Organic vs. Paid Quality Gap
* **Discovery:** Organic players exhibit a **44.14% Day-1 Retention**, significantly outperforming TikTok (29.59%) and Facebook (29.28%).
* **Recommendation:** Reallocate 15% of the Paid UA budget into App Store Optimization (ASO) to leverage higher-quality organic growth.

## 🚀 How to Run
1. Run `data_generator.py` to generate the `player_events.csv`.
2. Import the CSV into MySQL and run `retention_logic.sql` to build the analytical views.
3. Open the `PlayerPulse_Dashboard.pbix` (or view the PDF) to explore the insights.

## 📂 Repository Structure
* `data.py`: Python engine for telemetry data modeling.
* `db_setup.py`: Script for initializing the database schema.
* `retention_analysis.sql`: SQL View architecture for cohort analysis.
* `funnel_analysis.sql`: Query logic for onboarding stage conversion.
* `playerpulse_dashboard.pdf`: The Power BI dashboard project file.
* `Dashboard_Screenshot.png`: High-resolution view of the interactive BI tool. *(Note: Make sure to upload this!)*

---
**Author:** Tanya Jain  
*Aspiring Business Analyst* 
