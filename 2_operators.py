# Define Variables
total_choclates = 27
number_of_peeps = 4

# floor division (//) Normal division (/) jab hum karte hain, toh Python hamesha point (decimal) mein answer deta hai. Lekin // point ke baad wali saari values ko khatam kar deta hai aur sirf poora number (integer) deta hai.

chocolates_for_distribution = total_choclates // number_of_peeps

# Modulus (%) Yeh divide nahi karta, balki divide hone ke baad jo hissa baqi bach jata hai (remainder), yeh sirf woh batata hai

remaining_chocolates = total_choclates % number_of_peeps

# Output
print(f"chocholates for per person: {chocolates_for_distribution}.")
print(f"Remaining:{remaining_chocolates}.")