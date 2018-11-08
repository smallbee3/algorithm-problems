/*
1. Students

Given the following data definition,
write a query that returns the number of students whose first name is John.


TABLE students
   id INTEGER PRIMARY KEY,
   firstName VARCHAR(30) NOT NULL,
   lastName VARCHAR(30) NOT NULL


Time : 10 (min)

Tests: 3 pass / 0 fail
  No students named John: Correct answer
  Several students named John: Correct answer
  Every student is named John: Correct answer
*/


-- Write only the SQL statement that solves the problem and nothing else.
SELECT COUNT(*)
FROM students
where firstName='John'



/*
Result:
count(*)
--------
2



### Notes

> Mistakes :
> john -> John
*/