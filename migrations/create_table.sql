DROP TABLE IF EXISTS expenses;


CREATE TABLE IF NOT EXISTS expenses (
    id SERIAL PRIMARY KEY,
    expense_date VARCHAR(50) NOT NULL,
    expense_name VARCHAR(255) NOT NULL,
    amount DECIMAL NOT NULL,
    categories VARCHAR(50) NOT NULL
);