/*
196. Delete Duplicate Emails

Write a SQL query to delete all duplicate email entries in a table named Person,
keeping only unique emails based on its smallest Id.

+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
Id is the primary key column for this table.
For example, after running your query, the above Person table should have
the following rows:

+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+
Note:

Your output is the whole Person table after executing your sql.
Use delete statement.
 */


-- Way 1
DELETE FROM Person
WHERE Id IN (
    SELECT Id
    FROM (
        SELECT a.*
        FROM Person a, Person b
        WHERE a.Email=b.Email AND a.Id > b.Id
    ) AS t
)


/* Not working
(You can't specify target table 'Person' for update in FROM clause)

DELETE FROM Person
WHERE Id IN (
    SELECT a.Id
    FROM Person a, Person b
    WHERE a.Email=b.Email AND a.Id > b.Id
)
*/


-- Way 2
DELETE p1 FROM Person p1,
    Person p2
WHERE
    p1.Email = p2.Email AND p1.Id > p2.Id


-- Way 3
DELETE p2 FROM Person p1,
    Person p2
WHERE
    p1.Email = p2.Email AND p1.Id < p2.Id


