#Learning Primitive Datatypes and Type Casting
# 1. Defining different types of data
my_name = "Saleha"       # str
my_age = 24             # int
my_height = 5.3         # float
is_student = True       # bool

# 2. Checking their types using type()
print("--- Datatypes Checking ---")
print(my_name, type(my_name))
print(my_age, type(my_age))
print(my_height, type(my_height))
print(is_student, type(is_student))

# 3. Explicit Type Casting (Conversion)
# Age jo ke number hai, usay text (string) mein convert karna:
age_as_text = str(my_age)

print("\n--- After Type Casting ---")
print(age_as_text, type(age_as_text))