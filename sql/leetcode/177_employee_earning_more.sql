/*
181. Employees Earning More Than Their Managers

The Employee table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.

+----+-------+--------+-----------+
| Id | Name  | Salary | ManagerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | NULL      |
| 4  | Max   | 90000  | NULL      |
+----+-------+--------+-----------+
Given the Employee table, write a SQL query that finds out employees who earn more than their managers. For the above table, Joe is the only employee who earns more than his manager.

+----------+
| Employee |
+----------+
| Joe      |
+----------+


 */

-- Succeed
SELECT A.Name AS Employee
FROM Employee A, Employee B
WHERE A.ManagerId IS NOT NULL
AND A.ManagerId = B.Id
ANd A.Salary > B.Salary


-- Refactoring : Eradicate 'NOT NULL'
SELECT A.Name AS Employee
FROM Employee A, Employee B
WHERE A.ManagerId = B.Id
ANd A.Salary > B.Salary