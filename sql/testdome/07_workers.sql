/*
7. Workers

The following data definition defines an organization's employee
 hierarchy.

An employee is a manager if any other employee has
their managerId set to the first employees id. An employee
who is a manager may or may not also have a manager.


TABLE employees
  id INTEGER NOT NULL PRIMARY KEY
  managerId INTEGER REFERENCES employees(id)
  name VARCHAR(30) NOT NULL

Write a query that selects the names of employees who are not managers.
See the example case for more details.

Time : 10.21 min
Tests: 4 pass / 0 fail
  Example case: Correct answer
  No managers: Correct answer
  Workers have managers: Correct answer
  Managers have managers: Correct answer
 */


SELECT name
FROM employees
WHERE id NOT IN
(SELECT managerId FROM employees WHERE managerId IS NOT NULL)

/*
Result:
name
----
Mike
 */