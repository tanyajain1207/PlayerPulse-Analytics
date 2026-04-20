USE players;

WITH Installs AS (
    SELECT player_id, acquisition_channel, DATE(event_time) as install_date
    FROM player_events
    WHERE event_name = 'app_install'
),
ActiveDays AS (
    SELECT DISTINCT player_id, DATE(event_time) as active_date
    FROM player_events
    WHERE event_name = 'session_start'
)
SELECT 
    i.acquisition_channel,
    COUNT(DISTINCT i.player_id) AS total_installs,
    COUNT(DISTINCT CASE WHEN a.active_date = DATE_ADD(i.install_date, INTERVAL 1 DAY) THEN i.player_id END) AS day_1_retained,
    ROUND(COUNT(DISTINCT CASE WHEN a.active_date = DATE_ADD(i.install_date, INTERVAL 1 DAY) THEN i.player_id END) * 100.0 / COUNT(DISTINCT i.player_id), 2) AS d1_retention_pct,
    COUNT(DISTINCT CASE WHEN a.active_date = DATE_ADD(i.install_date, INTERVAL 7 DAY) THEN i.player_id END) AS day_7_retained,
    ROUND(COUNT(DISTINCT CASE WHEN a.active_date = DATE_ADD(i.install_date, INTERVAL 7 DAY) THEN i.player_id END) * 100.0 / COUNT(DISTINCT i.player_id), 2) AS d7_retention_pct
FROM Installs i
LEFT JOIN ActiveDays a ON i.player_id = a.player_id
GROUP BY i.acquisition_channel
ORDER BY total_installs DESC;