-- Select all records of the table with order
SELECT score, name
COUNT(*) AS OrsderCount
FROM second_table
GROUP BY score
ORDER BY score ASC;
