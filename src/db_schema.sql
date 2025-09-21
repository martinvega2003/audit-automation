-- SQL schema for transactions table (SQLite-friendly)
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    transaction_id TEXT NOT NULL,
    date DATE NOT NULL,
    customer_id TEXT,
    amount NUMERIC NOT NULL,
    currency TEXT,
    product_category TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Unique index to help detect duplicates at DB level
CREATE UNIQUE INDEX IF NOT EXISTS ux_transactions_transaction_id
ON transactions (transaction_id);