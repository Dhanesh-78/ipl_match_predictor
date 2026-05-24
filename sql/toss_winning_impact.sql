SELECT
	COUNT(*) AS Total_matches,
    SUM(CASE WHEN toss_winner=winner THEN 1 ELSE 0 END) AS Toss_winner_won,
    ROUND(SUM(CASE WHEN toss_winner=winner THEN 1 ELSE 0 END)*100/COUNT(*),2) AS Toss_win_pct
FROM matches
WHERE winner!='No Result';