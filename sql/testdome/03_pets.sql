/*
3. Pets

Information about pets is kept in two separate tables:


TABLE dogs
  id INTEGER NOT NULL PRIMARY KEY,
  name VARCHAR(50) NOT NULL

TABLE cats
  id INTEGER NOT NULL PRIMARY KEY,
  name VARCHAR(50) NOT NULL


Write a query that select all distinct pet names.
See the example case for more details.


Time : 9.27 (min)

Tests: 4 pass / 0 fail
  Example case: Correct answer
  Unique names: Correct answer
  Cats have the same names as dogs: Correct answer
  Various duplicate names: Correct answer
*/


/*SELECT DISTINCT dogs.name, cats.name
FROM dogs
LEFT JOIN cats*/
-- JOIN cannot have a one column as a result.


SELECT dogs.name FROM dogs
UNION
SELECT cats.name FROM cats


/*
Result:
name
-----
Bella
Kitty
Lola
*/