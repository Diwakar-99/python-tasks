# Global variable to keep track of the total sales amount
total_sales = 0

def record_sales():
    global total_sales  # Use the global keyword to modify the global variable

    # Local variable to store the daily sales amount
    daily_sales = float(input("Enter the daily sales amount: "))

    # Update the total sales
    total_sales += daily_sales

# Simulate recording sales for multiple days
num_days = int(input("Enter the number of days to record sales: "))
for _ in range(num_days):
    record_sales()

# Print the total sales amount at the end
print(f"\nTotal Sales after {num_days} days: ${total_sales}")
 
