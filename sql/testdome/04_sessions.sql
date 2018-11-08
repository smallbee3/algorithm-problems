/*
4. Sessions

App usage data are kept in the following table:

TABLE sessions
  id INTEGER PRIMARY KEY,
  userId INTEGER NOT NULL,
  duration DECIMAL NOT NULL

Write a query that selects userId and average session duration
for each user who has more than one session.

See the example case for more details.


Time : 6.4 (min)
  Example case: Correct answer
  Users with several sessions: Correct answer
  Various users: Correct answer
*/

SELECT userid, AVG(duration) AS AverageDuration
FROM sessions
GROUP BY userid
HAVING COUNT(userid) > 1

/*
Result:
Tests: 3 pass / 0 fail
userId    AVG(duration)
-----------------------
1         12
*/