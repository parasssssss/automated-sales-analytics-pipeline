def analyze_data(df):
    
    # KPIs
    total_sales = df['sales'].sum()
    total_profit = df['profit'].sum()
    total_orders = df['order_id'].nunique()

    print("Total Sales:", total_sales)
    print("Total Profit:", total_profit)
    print("Total Orders:", total_orders)

    # Top Products
    top_products = df.groupby('product_name')['sales'].sum().sort_values(ascending=False).head(5)
    print("\nTop 5 Products:\n", top_products)

    # Sales by Region
    sales_by_region = df.groupby('region')['sales'].sum()
    print("\nSales by Region:\n", sales_by_region)

    # Time Features
    df['year'] = df['order_date'].dt.year
    df['month'] = df['order_date'].dt.month

    # Sales by Year
    sales_by_year = df.groupby('year')['sales'].sum()
    print("\nSales by Year:\n", sales_by_year)

    # Sales by Month
    sales_by_month = df.groupby('month')['sales'].sum()
    print("\nSales by Month:\n", sales_by_month)

    # Monthly Trend
    monthly_trend = df.groupby(['year', 'month'])['sales'].sum()
    print("\nMonthly Trend:\n", monthly_trend)

    # Discount vs Profit
    discount_profit = df.groupby('discount')['profit'].mean()
    print("\nDiscount vs Profit:\n", discount_profit)

    # Loss Making Products
    loss_products = df[df['profit'] < 0]
    top_loss_products = loss_products.groupby('product_name')['profit'].sum().sort_values().head(5)
    print("\nTop Loss Making Products:\n", top_loss_products)

    # Category Profit
    category_profit = df.groupby('category')['profit'].sum()
    print("\nProfit by Category:\n", category_profit)