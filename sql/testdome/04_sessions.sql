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


Time : 6.4 min
Tests: 3 pass / 0 fail
  Example case: Correct answer
  Users with several sessions: Correct answer
  Various users: Correct answer
*/

SELECT userid, AVG(duration) AS AverageDuration
FROM sessions
GROUP BY userId
HAVING COUNT(userid) > 1

/*
Result:
userId    AVG(duration)
-----------------------
1         12
*/

/*
## NOTE
> In HAVING clause, userId, id or duration are all available as object of COUNT.
> Because HAVING clause here just check the number of record, not usedId.
> userId is already checked by GROUP BY clause.
 */