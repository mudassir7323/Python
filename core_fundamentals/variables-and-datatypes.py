# ============================================
#       Python Variables & Data Types
# ============================================


# ── 1. STRING (str) ──────────────────────────
first_name = "Alice"
last_name = 'Johnson'
full_name = first_name + " " + last_name       # concatenation
greeting  = f"Hello, {full_name}!"             # f-string

print("── Strings ──")
print(first_name)               # Alice
print(full_name)                # Alice Johnson
print(greeting)                 # Hello, Alice Johnson!
print(type(first_name))         # <class 'str'>
print(len(full_name))           # 13  (number of characters)
print(full_name.upper())        # ALICE JOHNSON
print(full_name.lower())        # alice johnson


# ── 2. INTEGER (int) ─────────────────────────
age          = 25
year_of_birth = 2000
apples       = 10
oranges      = 4

total_fruits  = apples + oranges
diff_fruits   = apples - oranges
times         = apples * oranges
remainder     = apples % 3          # modulus (leftover after division)

print("\n── Integers ──")
print(age)                          # 25
print(year_of_birth)                # 2000
print("Apples + Oranges:", total_fruits)   # 14
print("Apples - Oranges:", diff_fruits)    # 6
print("Apples × Oranges:", times)          # 40
print("10 mod 3 =", remainder)             # 1
print(type(age))                           # <class 'int'>


# ── 3. FLOAT (float) ─────────────────────────
price       = 9.99
temperature = 36.6
pi          = 3.14159
discount    = 0.15                     # 15%

discounted_price = price - (price * discount)

print("\n── Floats ──")
print(price)                           # 9.99
print(temperature)                     # 36.6
print(pi)                              # 3.14159
print(f"Price after discount: {discounted_price:.2f}")   # 8.49
print(type(price))                     # <class 'float'>

# int ↔ float conversion
whole   = int(pi)          # 3   (truncates decimal)
decimal = float(age)       # 25.0
print(f"int(pi) = {whole},  float(age) = {decimal}")


# ── 4. BOOLEAN (bool) ────────────────────────
is_student     = True
is_employed    = False
has_discount   = is_student and not is_employed   # True

print("\n── Booleans ──")
print(is_student)               # True
print(is_employed)              # False
print(has_discount)             # True
print(type(is_student))         # <class 'bool'>

# Comparisons produce booleans
print(10 > 5)                   # True
print(10 == 5)                  # False
print(age >= 18)                # True  (age = 25)


# ── 5. NONE ───────────────────────────────────
middle_name  = None             # no value yet
result       = None

print("\n── None ──")
print(middle_name)              # None
print(result)                   # None
print(type(middle_name))        # <class 'NoneType'>
print(middle_name is None)      # True
print(middle_name == None)


# ── 6. DYNAMIC TYPING ────────────────────────
print("\n── Dynamic Typing ──")
x = 42
print(f"x = {x}  →  type: {type(x)}")    # int

x = 3.14
print(f"x = {x}  →  type: {type(x)}")    # float

x = "Python"
print(f"x = {x}  →  type: {type(x)}")    # str

x = True
print(f"x = {x}  →  type: {type(x)}")    # bool


# ── 7. MULTIPLE ASSIGNMENT ───────────────────
print("\n── Multiple Assignment ──")
a, b, c = 10, 20, 30
print(a, b, c)                  # 10 20 30

p = q = r = 0
print(p, q, r)                  # 0 0 0


# ── 8. CONSTANTS (convention: ALL_CAPS) ──────
MAX_SCORE   = 100
TAX_RATE    = 0.08
APP_NAME    = "MyApp"

print("\n── Constants ──")
print(MAX_SCORE)                # 100
print(TAX_RATE)                 # 0.08
print(APP_NAME)                 # MyApp


# ── 9. PUTTING IT ALL TOGETHER ───────────────
print("\n── Student Report ──")
student_name  = "Bob"           # str
student_age   = 20              # int
gpa           = 3.75            # float
is_graduated  = False           # bool
scholarship   = None            # None (not assigned yet)

print(f"Name       : {student_name}")
print(f"Age        : {student_age}")
print(f"GPA        : {gpa}")
print(f"Graduated  : {is_graduated}")
print(f"Scholarship: {scholarship}")
print(f"Eligible?  : {gpa >= 3.5 and not is_graduated}")