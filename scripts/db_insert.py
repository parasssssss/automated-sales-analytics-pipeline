import os
import psycopg2
from psycopg2.extras import execute_values
from dotenv import load_dotenv

load_dotenv()


def insert_data(df):
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="sales_db",
            user="postgres",
            password=os.getenv("db_password")
        )
        
        cursor = conn.cursor()

        # Prepare data
        data = [
            (
                row['order_id'],
                row['product_id'],
                row['order_date'],
                row['product_name'],
                row['category'],
                row['sales'],
                row['profit'],
                row['quantity'],
                row['discount'],
                row['region']
            )
            for _, row in df.iterrows()
        ]

        # UPSERT query
        query = """
        INSERT INTO sales (
            order_id, product_id, order_date, product_name,
            category, sales, profit, quantity, discount, region
        )
        VALUES %s
        ON CONFLICT (order_id, product_id)
        DO UPDATE SET
            sales = EXCLUDED.sales,
            profit = EXCLUDED.profit,
            quantity = EXCLUDED.quantity,
            discount = EXCLUDED.discount
        """

        execute_values(cursor, query, data)

        conn.commit()
        cursor.close()
        conn.close()

        print("Data inserted/updated successfully")

    except Exception as e:
        print("Error:", e)