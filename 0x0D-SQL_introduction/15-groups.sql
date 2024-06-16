-- A script to list the number of records 
-- with the same value in the table second_table 
-- of database hbtn_0c_0
SELECT score, COUNT(*) AS number 
FROM second_table 
GROUP BY score 
ORDER BY number DESC;
