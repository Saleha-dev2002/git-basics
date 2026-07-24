order_amount = 1200          # Transaction amount in $
customer_account_age = 5     # Account age in days
is_guest_checkout = True     # Guest user or registered
daily_limit = 1000           # System max daily limit

is_high_value = order_amount > 1000
is_new_account = customer_account_age > 30
is_guest = is_guest_checkout == True

#Forward slash /n simple text print karega, jabke backslash \n line break karega
print(f"Is the Value is High?\n{is_high_value}")
print(f"Customer Account is new?\n{is_new_account}")
print(f"Is guest checkout?\n{is_guest_checkout}")