/*
5. Web Shop

Each item in a web shop belongs to a seller.
To ensure service quality, each seller has a rating.

The data are kept in the following two tables:


TABLE sellers
  id INTEGER PRIMARY KEY,
  name VARCHAR(30) NOT NULL,
  rating INTEGER NOT NULL

TABLE items
  id INTEGER PRIMARY KEY,
  name VARCHAR(30) NOT NULL,
  sellerId INTEGER REFERENCES sellers(id)

Write a query that selects the item name and the name of its
seller for each item that belongs to a seller with a rating greater
 than 4.

See the example case for more details.

Time : 6.44 min
Tests: 4 pass / 0 fail
  Example case: Correct answer
  Single seller with single item: Correct answer
  Top rated sellers: Correct answer
  Low rated sellers: Correct answer

 */

SELECT items.name AS Item, sellers.name AS Seller
FROM items
JOIN sellers ON items.sellerID=sellers.id
WHERE sellers.rating > 4


/*
Result:
Item        Seller
------------------
Notebook    Penny
Pencil      Penny
 */
