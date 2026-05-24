SELECT batter,
	SUM(batsman_runs) AS Total_runs,
    ROUND(SUM(batsman_runs)*100/COUNT(*),1) AS Strike_rate
FROM deliveries
GROUP BY batter
ORDER BY total_runs
DESC LIMIT 10;