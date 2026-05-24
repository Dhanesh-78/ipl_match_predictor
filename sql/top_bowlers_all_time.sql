SELECT bowler,
	SUM(CASE WHEN dismissal_kind NOT IN
		('run out','retired hurt') AND
        dismissal_kind IS NOT NULL THEN 1 ELSE 0 END) AS Wickets
FROM deliveries
GROUP BY bowler
ORDER BY Wickets DESC
LIMIT 10;
