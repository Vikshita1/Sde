DROP TABLE IF EXISTS bills;

CREATE TABLE bills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL,
    month TEXT NOT NULL,
    amount REAL NOT NULL
);

