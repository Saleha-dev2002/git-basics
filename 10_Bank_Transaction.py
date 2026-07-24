# Variables
account_balance = 50000
daily_limit = 25000
entered_pin = 1234
correct_pin = 1234
requested_amount = 20000

# Nested Logic
if entered_pin == correct_pin:
    if requested_amount > account_balance:
        print("❌ Insufficient Balance.")
    elif requested_amount > daily_limit:
        print("❌ Daily Withdrawal Limit Exceeded.")
    else:
        new_balance = account_balance - requested_amount
        print(f" HuHu Withdrawal Successful! New balance is: {new_balance}")
else:
    print("❌ Incorrect PIN. Access Denied.")