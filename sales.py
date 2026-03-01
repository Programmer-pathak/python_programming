#Sales Data Analysis
#Given sales data of products, write a program to calculate total sales, average sales, and identify the top-selling product.

sales_data = {
    "Product A": 100,
    "Product B": 150,
    "Product C": 50,
    "Product D": 300,
    "Product E": 60
}
total_sales = sum(sales_data.values())

average_sales = total_sales / len(sales_data)

top_product = max(sales_data, key=sales_data.get)
top_sales = sales_data[top_product]

print(f"Total Sales: {total_sales}")
print(f"Average Sales: {average_sales:.2f}")
print(f"Top-selling Product is \"{top_product}\" with sales {top_sales}")