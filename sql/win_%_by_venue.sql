SELECT venue,
	ROUND(SUM(CASE WHEN toss_decision='field' THEN 1 ELSE 0 END)*100/COUNT(*),1) AS field_pct
FROM matches
GROUP BY venue HAVING COUNT(*) > 10
ORDER BY field_pct DESC;