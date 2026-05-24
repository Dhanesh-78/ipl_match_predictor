SELECT toss_decision,
  COUNT(*) AS times_chosen,
  ROUND(SUM(CASE WHEN toss_winner = winner THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 1) AS win_pct
FROM matches WHERE winner != 'No Result'
GROUP BY toss_decision
ORDER BY times_chosen;