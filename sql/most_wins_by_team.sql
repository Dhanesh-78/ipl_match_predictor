SELECT winner AS Team,
	count(*) AS Matches_won
FROM matches
WHERE winner!='No Result'
GROUP BY winner
ORDER BY Matches_won DESC
LIMIT 10;