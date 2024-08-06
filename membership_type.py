# Ask the user for their membership type
membership_type = input("Enter your membership type (Regular, Premium, Guest): ").strip().lower()

# Determine borrowing limits based on membership type
if membership_type == "regular":
    max_books = 3
    message = f"As a Regular member, you can borrow up to {max_books} books."
elif membership_type == "premium":
    max_books = 10
    message = f"As a Premium member, you can borrow up to {max_books} books."
elif membership_type == "guest":
    message = "As a Guest member, you cannot borrow books."
else:
    message = "Invalid membership type. Please enter Regular, Premium, or Guest."

# Print the appropriate message
print(message)
