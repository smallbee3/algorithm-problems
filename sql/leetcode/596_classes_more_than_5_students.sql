/*
596. Classes More Than 5 Students

There is a table courses with columns: student and class

Please list out all classes which have more than or equal to 5 students.

For example, the table:

+---------+------------+
| student | class      |
+---------+------------+
| A       | Math       |
| B       | English    |
| C       | Math       |
| D       | Biology    |
| E       | Math       |
| F       | Computer   |
| G       | Math       |
| H       | Math       |
| I       | Math       |
+---------+------------+
Should output:

+---------+
| class   |
+---------+
| Math    |
+---------+
Note:
The students should not be counted duplicate in each course.
 */


/* Fail with duplicate data

SELECT class
FROM courses
GROUP BY class
HAVING Count(class) >= 5
 */


SELECT class
FROM (
    SELECT DISTINCT *
    FROM courses
) AS t
GROUP BY class
HAVING Count(class) >= 5


/*
* Learning
  1. Eradicate duplicate data from the table

 */