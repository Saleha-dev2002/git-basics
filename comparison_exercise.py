user_age = 20
account_balance = 150
item_price = 150
passing_marks = 50
user_score = 45

is_adult = user_age >= 18
can_afford = account_balance >= item_price
exact_balance = account_balance == item_price
has_failed = user_score < passing_marks

print(f"Is Adult: {is_adult}")
print(f"Can Afford: {can_afford}")
print(f"Exact Balance Match: {exact_balance}")
print(f"Has Failed: {has_failed}")