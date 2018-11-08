/*
2. Enrollment

A table containing the students enrolled in a yearly course has incorrect data
in records with ids between 20 and 100 (inclusive).


TABLE enrollments
  id INTEGER NOT NULL PRIMARY KEY
  year INTEGER NOT NULL
  studentId INTEGER NOT NULL


Write a query that updates the field 'year' of every faulty record to 2015.


Time : 3 (min)

Tests: 3 pass / 0 fail
  Ids equal to 20 and 100: Correct answer
  Ids between 20 and 100: Correct answer
  All ids: Correct answer
*/


UPDATE enrollments
SET year='2015'
WHERE id BETWEEN 20 AND 100



/*
Result:
2 rows affected.

SQL> SELECT id, year, studentId FROM enrollments;
id     year    studentId
------------------------
1      2003    1
20     2015    2
100    2015    3
110    2016    4
*/