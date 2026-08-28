import sqlite3

class MoneyExchangeDB:
    """creates the database schema."""

    def __init__(self, db_path: str = "money_exchange.db"):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.conn.execute("PRAGMA foreign_keys = ON")  # enforced OFF by default in SQLite
        self.create_tables()

    def create_tables(self) -> None:
        cursor = self.conn.cursor()

        cursor.executescript(
            """
            CREATE TABLE IF NOT EXISTS employees (
                employee_id     INTEGER PRIMARY KEY AUTOINCREMENT,
                username        TEXT NOT NULL UNIQUE,
                password_hash   TEXT NOT NULL,
                full_name       TEXT NOT NULL,
                role            TEXT NOT NULL DEFAULT 'admin'
            );

            CREATE TABLE IF NOT EXISTS customers (
                customer_id     INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name      TEXT NOT NULL,
                last_name       TEXT NOT NULL,
                email           TEXT,
                phone           TEXT,
                created_by      INTEGER NOT NULL,
                FOREIGN KEY (created_by) REFERENCES employees(employee_id)
                    ON DELETE RESTRICT
            );

            CREATE TABLE IF NOT EXISTS currencies (
                currency_code   TEXT PRIMARY KEY,
                currency_name   TEXT NOT NULL,
                symbol          TEXT
            );

            CREATE TABLE IF NOT EXISTS exchange_rates (
                rate_id         INTEGER PRIMARY KEY AUTOINCREMENT,
                base_currency   TEXT NOT NULL,
                target_currency TEXT NOT NULL,
                rate            REAL NOT NULL CHECK (rate > 0),
                effective_date  DATETIME NOT NULL,
                FOREIGN KEY (base_currency)   REFERENCES currencies(currency_code) ON DELETE RESTRICT,
                FOREIGN KEY (target_currency) REFERENCES currencies(currency_code) ON DELETE RESTRICT,
                CHECK (base_currency <> target_currency)
            );

            CREATE TABLE IF NOT EXISTS transactions (
                transaction_id   INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id      INTEGER NOT NULL,
                employee_id      INTEGER NOT NULL,
                from_currency    TEXT NOT NULL,
                to_currency      TEXT NOT NULL,
                amount_from      REAL NOT NULL CHECK (amount_from > 0),
                amount_to        REAL NOT NULL CHECK (amount_to > 0),
                rate_applied     REAL NOT NULL CHECK (rate_applied > 0),
                transaction_date DATETIME NOT NULL,
                FOREIGN KEY (customer_id)   REFERENCES customers(customer_id)     ON DELETE RESTRICT,
                FOREIGN KEY (employee_id)   REFERENCES employees(employee_id)     ON DELETE RESTRICT,
                FOREIGN KEY (from_currency) REFERENCES currencies(currency_code)  ON DELETE RESTRICT,
                FOREIGN KEY (to_currency)   REFERENCES currencies(currency_code)  ON DELETE RESTRICT
            );

            CREATE INDEX IF NOT EXISTS idx_rates_pair
                ON exchange_rates(base_currency, target_currency, effective_date);
            CREATE INDEX IF NOT EXISTS idx_txn_customer ON transactions(customer_id);
            CREATE INDEX IF NOT EXISTS idx_txn_date ON transactions(transaction_date);
            """
        )
        self.conn.commit()

    def close(self) -> None:
        self.conn.close()


if __name__ == "__main__":
    db = MoneyExchangeDB("money_exchange.db")
    print(f"Database created at: {db.db_path}")

    tables = db.conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'"
    ).fetchall()
    print("Tables:", [t[0] for t in tables])

    db.close()