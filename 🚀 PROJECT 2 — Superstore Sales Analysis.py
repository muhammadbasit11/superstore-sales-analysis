import pandas as pd
# 1️⃣Load dataset
df=pd.read_csv("super_store.csv")
# 2️⃣Check shape
shape=df.shape
print(shape)
# 3️⃣Check data types
data_type=df.dtypes
print(data_type)                 #dtype gives us the data type of columns
# 4️⃣Check missing values
total_nulls=df.isnull().sum()
print(f"THE TOTAL NULL VALUES PER COLUMN IS\n{total_nulls}")
# 5️⃣Check duplicate orders
duplicated_orders=df["Order ID"].duplicated().sum()           
print(f"THE TOTAL DUPLICATED ORDERS ARE {duplicated_orders}")

#converting 'Order Date', 'Ship Date' into pd.to_datetime
df["Order Date"]=pd.to_datetime(df["Order Date"],format="%d/%m/%Y")

df["Ship Date"]=pd.to_datetime(df["Ship Date"],format="%d/%m/%Y")

# 🟢 PHASE 2 — Feature Engineering (Very Important)

#creating column of year
df["Year"]=df["Order Date"].dt.year
#creating column of month
df["Month"]=df["Order Date"].dt.month
##creating column of month name
df["MonthName"]=df["Order Date"].dt.month_name()
#creating column of day of the week
df["Day"]=df["Order Date"].dt.day_name()
#creating column of the date
df["Date"]=df["Order Date"].dt.day
#creating column of days of shipping
# df["ShippingDays"]=df["Order Date"].dt.month
df["ShippingDays"]= (df["Ship Date"] - df["Order Date"]).dt.days #it is special it takes the the shipping date
                                                                 #then it takes the date of order and subtract it

# 🟢 PHASE 3 — Revenue Analysis

# 1️⃣ Total Sales
print(f"THE ENTIRE SALE IS :{df['Sales'].sum():.2f}")

# 2️⃣ Sales by Year
year_sale=df.groupby("Year")["Sales"].sum().sort_index()
# Is revenue increasing yearly?
year_growth=year_sale.pct_change()*100
print(f"THE YEARLY GROWTH IS {year_growth}")

# 3️⃣ Sales by Month
monthly_sale=df.groupby(["Month","MonthName"])["Sales"].sum().sort_index()
print(f"the total sale in the months is\n{monthly_sale}")
# Which month performs best?
print(f"THE MONTH IN WHICH MOST SALE HAS HAPPENED IS {monthly_sale.idxmax()[1]}")

# 4️⃣ Sales by Region
sales_by_region=df.groupby("Region")["Sales"].sum()
# Which region generates most revenue?
print(f"the sales from different REGIONS  is\n{sales_by_region}")
print(f"the most sales is from {sales_by_region.idxmax()} which is {sales_by_region.max()}")

# 5 Sales by States
sales_by_state=df.groupby("State")["Sales"].sum()
print(f"the sales by state is {sales_by_state}")
top_sales_state=sales_by_state.idxmax()
print(f"the most sales by state is from {top_sales_state} which is {sales_by_state.max()}")


# 6️⃣ Sales by Category
sales_by_category=df.groupby("Category")["Sales"].sum()
print(f"the sale by category is\n{sales_by_category}")
# Which category drives most revenue?
top_category=sales_by_category.idxmax()
print(f"the most sold category is {top_category}")

# 7️⃣ Sales by Sub-Category

sales_by_sub_category=df.groupby("Sub-Category")["Sales"].sum()
print(f"THE SALES OF SUB CATEGORY IS\n{sales_by_sub_category}")
# Which product type is strongest?
top_product=sales_by_sub_category.idxmax()
print(f"the most sold product type is {top_product}")

# 🟢 PHASE 4 — Customer Analysis

# 1️⃣ Top 10 Customers by Sales
top_10_customers=df.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False).head(10)
print(f"the top 10 customers are\n{top_10_customers}")

# 2️⃣ Sales by Segment
# Consumer vs Corporate vs Home Office.
sale_by_segment=df.groupby("Segment")["Sales"].sum()
print(f"the total sale by segment is\n{sale_by_segment}")

# 🟢 PHASE 5 — Product Analysis

# 1️⃣ Top 10 Products by Sales
top_10_product=df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)
print(f"the top 10 products are\n{top_10_product}")

# 2️⃣ Most Ordered Product (by count)
top_ordered_product=df.groupby("Product Name")["Product ID"].count().sort_values(ascending=False)
print(f"the most ordered product is {top_ordered_product.idxmax()} which is ordered {top_ordered_product.max()}")

# 🟢 PHASE 6 — Shipping Analysis


# 1️⃣ Average Shipping Time
shipping_time=df["ShippingDays"].mean()
print(f"the average shipping time is about {int(shipping_time)} days")


# 2️⃣ Shipping Time by Ship Mode
shipping_time_diff_mode=df.groupby("Ship Mode")["ShippingDays"].mean()
print(f"the average shipping time is about\n{(shipping_time_diff_mode)}")
# Which shipping method is fastest?
top_shipping_mode=shipping_time_diff_mode.idxmin()
print(f"the fatest shipping mode is:{top_shipping_mode}")

# 🟢 PHASE 7 — Deep Thinking Questions

# Which region contributes most to revenue?
print(f"the most sales is from {sales_by_region.idxmax()} which is {sales_by_region.max()}")
# Which category drives maximum sales?
print(f"the most sold category is {top_category}")
# Who are the most valuable customers?
top_10_customers=df.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False).head(5)
print(f"the top 5 customers are\n{top_10_customers}")
# Which state dominates the business?
print(f"the most sales by state is from {top_sales_state} which is {sales_by_state.max()}")
