USE players;

WITH FunnelCounts AS (
    SELECT
        COUNT(DISTINCT CASE WHEN event_name = 'app_install' THEN player_id END) AS step_1_installs,
        COUNT(DISTINCT CASE WHEN event_name = 'tutorial_complete' THEN player_id END) AS step_2_tutorial,
        COUNT(DISTINCT CASE WHEN event_name = 'level_5_reached' THEN player_id END) AS step_3_level5,
        COUNT(DISTINCT CASE WHEN event_name = 'store_page_viewed' THEN player_id END) AS step_4_store,
        COUNT(DISTINCT CASE WHEN event_name = 'in_app_purchase' THEN player_id END) AS step_5_purchase
    FROM player_events
)
SELECT
    step_1_installs,
    step_2_tutorial,
    ROUND((step_2_tutorial * 100.0 / step_1_installs), 2) AS tutorial_conv_pct,
    step_3_level5,
    ROUND((step_3_level5 * 100.0 / step_2_tutorial), 2) AS level5_conv_pct,
    step_4_store,
    ROUND((step_4_store * 100.0 / step_3_level5), 2) AS store_conv_pct,
    step_5_purchase,
    ROUND((step_5_purchase * 100.0 / step_4_store), 2) AS purchase_conv_pct
FROM FunnelCounts;