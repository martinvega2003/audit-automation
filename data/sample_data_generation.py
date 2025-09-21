# Run: python data/sample_data_generation.py
import pandas as pd
import random
from datetime import datetime, timedelta

def generate_rows(n=250, seed=42):
    random.seed(seed)
    start = datetime(2025, 1, 1)
    rows = []
    for i in range(n):
        tx_date = start + timedelta(days=random.randint(0, 300))
        # create amounts centered around 200, occasionally negative or extreme
        amount = round(random.gauss(200, 350), 2)
        rows.append({
            "transaction_id": f"TX{1000 + i}",
            "date": tx_date.strftime("%Y-%m-%d"),
            "customer_id": f"C{random.randint(1,80)}",
            "amount": amount,
            "currency": random.choice(["USD", "USD", "USD", "PEN"]),  # mostly USD
            "product_category": random.choice(["Shoes", "Apparel", "Accessories", "Electronics"])
        })

    return rows

def introduce_errors(df):
    # introduce a duplicate transaction_id
    if len(df) >= 3:
        df.loc[0, "transaction_id"] = df.loc[1, "transaction_id"]
    # invalid date format
    if len(df) >= 4:
        df.loc[2, "date"] = "2025/13/01"
    # negative amount
    if len(df) >= 5:
        df.loc[3, "amount"] = -150.00
    # empty required field
    if len(df) >= 6:
        df.loc[4, "transaction_id"] = None
    return df

def main():
    rows = generate_rows(250)
    df = pd.DataFrame(rows)

    # add some high outliers
    for _ in range(3):
        idx = random.randint(0, len(df)-1)
        df.loc[idx, "amount"] = df.loc[idx, "amount"] * 20

    df = introduce_errors(df)
    out_path = "data/raw_transactions.xlsx"
    df.to_excel(out_path, index=False)
    print(f"Sample data generated: {out_path} (records: {len(df)})")

if __name__ == "__main__":
    main()