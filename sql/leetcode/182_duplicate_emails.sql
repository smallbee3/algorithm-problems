/*
182. Duplicate Emails

Write a SQL query to find all duplicate emails in a table named Person.

+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
For example, your query should return the following for the above table:

+---------+
| Email   |
+---------+
| a@b.com |
+---------+
Note: All emails are in lowercase.


 */


-- Step 1
SELECT Email, COUNT(Email)
FROM Person
GROUP BY Email
HAVING COUNT(Email)

{"headers":["Email","COUNT(Email)"],"values":[["a@b.com",2],["c@d.com",1]]}


-- Step 2
SELECT Email, COUNT(Email)
FROM Person
GROUP BY Email
HAVING COUNT(Email) > 1

{"headers":["Email","COUNT(Email)"],"values":[["a@b.com",2]]}


-- Answer
SELECT Email
FROM Person
GROUP BY Email
HAVING COUNT(Email) > 1

{"headers":["Email"],"values":[["a@b.com"]]}



-- Why not ?
SELECT Email
FROM Person
HAVING COUNT(Email) > 1

>>
https://leetcode.com/problems/duplicate-emails/discuss/53562/What's-wrong-with-my-solution-(without-group-by)