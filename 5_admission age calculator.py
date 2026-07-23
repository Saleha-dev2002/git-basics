birth_year_text = "2020"
birth_year_number = int(birth_year_text)
current_year = 2026
calculated_age = current_year - birth_year_number
is_eligible = calculated_age >=5

print("--School Admission System--")
print(f"child's Age: { calculated_age} years")
print(f"Is the child eligible for admission: { is_eligible} ")
