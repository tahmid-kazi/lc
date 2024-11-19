# Write your MySQL query statement below
# 11/19/24) Tue) 324-329pm) tk)
SELECT w1.Id
FROM Weather w1
JOIN Weather w2
    on DATEDIFF(w1.RecordDate, w2.RecordDate) = 1
WHERE w1.Temperature > w2.Temperature;