# ============================================================
#         Python Operators & Expressions — Full Guide
#         Covers: Arithmetic, Comparison, Logical,
#                 Assignment, Membership, Identity, Bitwise
# ============================================================


# ── 1. ARITHMETIC OPERATORS ─────────────────────────────────
print("=" * 55)
print("  1. ARITHMETIC OPERATORS")
print("=" * 55)

a, b = 17, 5

print(f"a = {a}, b = {b}")
print(f"a + b  = {a + b}")        # 22  — addition
print(f"a - b  = {a - b}")        # 12  — subtraction
print(f"a * b  = {a * b}")        # 85  — multiplication
print(f"a / b  = {a / b}")        # 3.4 — true division (always float)
print(f"a // b = {a // b}")       # 3   — floor division (drops decimal)
print(f"a % b  = {a % b}")        # 2   — modulus (remainder)
print(f"a ** b = {a ** b}")       # 1419857 — exponentiation

# ── Tricky: Negative floor division ──
print("\n-- Negative Floor Division (tricky!) --")
print(f"-7 // 2  = {-7 // 2}")    # -4  (rounds DOWN, not toward zero)
print(f" 7 // -2 = {7 // -2}")    # -4
print(f"-7 % 2   = {-7 % 2}")     # 1   (result has sign of divisor)
print(f" 7 % -2  = {7 % -2}")     # -1

# ── Tricky: Chained exponentiation (right-to-left!) ──
print("\n-- Chained Exponentiation (right-to-left!) --")
result = 2 ** 3 ** 2              # same as 2 ** (3**2) = 2**9 = 512
print(f"2 ** 3 ** 2 = {result}")  # 512, NOT 64

# ── Real-world: Even/odd check using modulus ──
print("\n-- Even / Odd Check --")
for n in [0, 1, 7, 42, -3]:
    label = "even" if n % 2 == 0 else "odd"
    print(f"  {n:>4} is {label}")

# ── Real-world: Digit extraction using // and % ──
print("\n-- Extract Digits from a Number --")
number = 4795
thousands = number // 1000
hundreds  = (number % 1000) // 100
tens      = (number % 100)  // 10
ones      =  number % 10
print(f"{number}  →  thousands={thousands}, hundreds={hundreds}, tens={tens}, ones={ones}")


# ── 2. COMPARISON OPERATORS ─────────────────────────────────
print("\n" + "=" * 55)
print("  2. COMPARISON OPERATORS")
print("=" * 55)

x, y = 10, 20
print(f"x={x}, y={y}")
print(f"x == y : {x == y}")
print(f"x != y : {x != y}")
print(f"x >  y : {x > y}")
print(f"x <  y : {x < y}")
print(f"x >= y : {x >= y}")
print(f"x <= y : {x <= y}")

# ── Tricky: Chained comparisons (Python-only feature) ──
print("\n-- Chained Comparisons --")
age = 25
print(f"18 <= age < 60  →  {18 <= age < 60}")   # True
print(f"1 < 2 < 3 < 4   →  {1 < 2 < 3 < 4}")   # True
print(f"1 < 2 > 1 < 3   →  {1 < 2 > 1 < 3}")   # True (each pair checked)

# ── Tricky: Comparing different types ──
print("\n-- Comparing Numbers & Floats --")
print(f"0.1 + 0.2 == 0.3       → {0.1 + 0.2 == 0.3}")          # False! (float precision)
print(f"round(0.1+0.2, 1)==0.3 → {round(0.1 + 0.2, 1) == 0.3}") # True  (use round)
import math
print(f"math.isclose(0.1+0.2, 0.3) → {math.isclose(0.1 + 0.2, 0.3)}")  # True (best way)

# ── Tricky: String comparison (lexicographic) ──
print("\n-- String Comparison (alphabetical order) --")
print(f"'apple' < 'banana' → {'apple' < 'banana'}")   # True
print(f"'Z' < 'a'          → {'Z' < 'a'}")            # True! (uppercase < lowercase in ASCII)
print(f"'abc' == 'ABC'     → {'abc' == 'ABC'}")        # False


# ── 3. LOGICAL OPERATORS ────────────────────────────────────
print("\n" + "=" * 55)
print("  3. LOGICAL OPERATORS")
print("=" * 55)

print(f"True  and True  = {True and True}")
print(f"True  and False = {True and False}")
print(f"False or  True  = {False or True}")
print(f"False or  False = {False or False}")
print(f"not True        = {not True}")
print(f"not False       = {not False}")

# ── Tricky: Short-circuit evaluation ──
print("\n-- Short-Circuit Evaluation --")
# 'and' stops at first False, 'or' stops at first True
def say(label, val):
    print(f"  called {label}()")
    return val

# Only first function called (False and ... skips second)
print("False and say('B', True) →", False and say("B", True))
# Only first function called (True or ... skips second)
print("True  or  say('B', False) →", True or say("B", False))

# ── Tricky: Logical operators return VALUES, not just True/False ──
print("\n-- 'and'/'or' Return Values (not just booleans!) --")
print(f"'hello' and 'world' = {'hello' and 'world'}")   # 'world'  (last truthy)
print(f"''      and 'world' = {'' and 'world'}")        # ''       (first falsy)
print(f"''      or  'world' = {'' or 'world'}")         # 'world'  (first truthy)
print(f"0       or  42      = {0 or 42}")               # 42

# Real use: default values
username = ""
display  = username or "Guest"
print(f"\nusername='' → display as: '{display}'")       # Guest

# ── Truthy / Falsy values ──
print("\n-- Falsy Values in Python --")
falsy = [0, 0.0, "", [], {}, None, False]
for val in falsy:
    print(f"  bool({str(val):<8}) = {bool(val)}")


# ── 4. ASSIGNMENT OPERATORS ─────────────────────────────────
print("\n" + "=" * 55)
print("  4. ASSIGNMENT OPERATORS")
print("=" * 55)

score = 100
print(f"start        : score = {score}")
score += 15;  print(f"score += 15  : score = {score}")
score -= 5;   print(f"score -= 5   : score = {score}")
score *= 2;   print(f"score *= 2   : score = {score}")
score //= 3;  print(f"score //= 3  : score = {score}")
score **= 2;  print(f"score **= 2  : score = {score}")
score %= 1000;print(f"score %%= 1000: score = {score}")

# ── Walrus operator := (Python 3.8+) ──
print("\n-- Walrus Operator := (assign inside expression) --")
data = [3, 7, 1, 9, 2, 8, 5]
# Without walrus:
length = len(data)
if length > 5:
    print(f"  (normal)  list has {length} items — processing...")

# With walrus (assign AND check in one line):
if (n := len(data)) > 5:
    print(f"  (walrus)  list has {n} items — processing...")


# ── 5. MEMBERSHIP OPERATORS ─────────────────────────────────
print("\n" + "=" * 55)
print("  5. MEMBERSHIP OPERATORS  (in / not in)")
print("=" * 55)

fruits = ["apple", "banana", "cherry"]
text   = "Hello, World!"
grades = {"Alice": 90, "Bob": 85}

print(f"'banana' in fruits          → {'banana' in fruits}")       # True
print(f"'mango'  in fruits          → {'mango' in fruits}")        # False
print(f"'World'  in text            → {'World' in text}")          # True
print(f"'world'  in text            → {'world' in text}")          # False (case-sensitive)
print(f"'Alice'  in grades          → {'Alice' in grades}")        # True (checks keys)
print(f"90       in grades.values() → {90 in grades.values()}")   # True (check values)

# ── Tricky: membership on string vs list of chars ──
print("\n-- String Substring vs List Membership --")
print(f"'an' in 'banana'      → {'an' in 'banana'}")              # True (substring)
print(f"'an' in ['b','an','a']→ {'an' in ['b','an','a']}")        # True (exact element)
print(f"'an' in ['b','a','n'] → {'an' in ['b','a','n']}")         # False (no exact 'an')


# ── 6. IDENTITY OPERATORS ───────────────────────────────────
print("\n" + "=" * 55)
print("  6. IDENTITY OPERATORS  (is / is not)")
print("=" * 55)

a = [1, 2, 3]
b = [1, 2, 3]
c = a                        # c points to SAME object as a

print(f"a == b  : {a == b}")     # True  — same VALUE
print(f"a is b  : {a is b}")     # False — different objects in memory
print(f"a is c  : {a is c}")     # True  — same object
print(f"id(a)={id(a)}, id(b)={id(b)}, id(c)={id(c)}")

# ── Tricky: Small integer caching ──
print("\n-- Small Integer Cache (CPython quirk) --")
p = 100;  q = 100
r = 1000; s = 1000
print(f"p=100, q=100 → p is q : {p is q}")    # True  (cached -5 to 256)
print(f"r=1000,s=1000→ r is s : {r is s}")    # False (outside cache range)

# ── Always use 'is' for None, True, False ──
print("\n-- Correct None / Bool Checks --")
value = None
print(f"value is None     → {value is None}")         # Correct ✅
print(f"value == None     → {value == None}")         # Works but not recommended
flag = True
print(f"flag is True      → {flag is True}")          # Correct ✅


# ── 7. BITWISE OPERATORS ────────────────────────────────────
print("\n" + "=" * 55)
print("  7. BITWISE OPERATORS")
print("=" * 55)

x, y = 0b1010, 0b1100   # 10 and 12 in binary
print(f"x  = {x:>4}  →  {x:08b}")
print(f"y  = {y:>4}  →  {y:08b}")
print(f"x & y  (AND)        = {x&y:>3}  →  {x&y:08b}")
print(f"x | y  (OR)         = {x|y:>3}  →  {x|y:08b}")
print(f"x ^ y  (XOR)        = {x^y:>3}  →  {x^y:08b}")
print(f"~x     (NOT)        = {~x:>3}  →  {~x}")
print(f"x << 1 (left shift) = {x<<1:>3}  →  {x<<1:08b}  (×2)")
print(f"x >> 1 (right shift)= {x>>1:>3}  →  {x>>1:08b}  (÷2)")

# ── Tricky: Fast multiply/divide by powers of 2 ──
print("\n-- Bit Shift = Fast ×2 / ÷2 --")
n = 6
print(f"n      = {n}")
print(f"n << 1 = {n << 1}   (n × 2)")
print(f"n << 2 = {n << 2}   (n × 4)")
print(f"n >> 1 = {n >> 1}   (n ÷ 2)")

# ── Real-world: Check if a number is a power of 2 ──
print("\n-- Is N a Power of 2? (Bitwise Trick) --")
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

for n in [1, 2, 3, 4, 5, 8, 16, 100, 128]:
    print(f"  {n:>4} → power of 2? {is_power_of_two(n)}")

# ── Real-world: Toggle / Set / Clear a bit ──
print("\n-- Bit Manipulation: Set, Clear, Toggle --")
flags = 0b0000
print(f"Initial flags   : {flags:08b}")
flags |= (1 << 2)      # SET   bit 2
print(f"After SET   bit2: {flags:08b}")
flags &= ~(1 << 2)     # CLEAR bit 2
print(f"After CLEAR bit2: {flags:08b}")
flags ^= (1 << 3)      # TOGGLE bit 3
print(f"After TOGGLE bit3:{flags:08b}")


# ── 8. OPERATOR PRECEDENCE ──────────────────────────────────
print("\n" + "=" * 55)
print("  8. OPERATOR PRECEDENCE  (tricky examples)")
print("=" * 55)

# Without parentheses
r1 = 2 + 3 * 4 ** 2        # 4**2=16, 3*16=48, 2+48=50
r2 = (2 + 3) * 4 ** 2      # 4**2=16, (5)*16=80
r3 = (2 + 3) * (4 ** 2)    # same: 80
r4 = not 3 > 2 and 5 < 10  # (not (3>2)) and (5<10) = False and True = False
r5 = not (3 > 2 and 5 < 10)# not (True and True) = not True = False

print(f"2 + 3 * 4 ** 2          = {r1}")   # 50
print(f"(2 + 3) * 4 ** 2        = {r2}")   # 80
print(f"not 3>2 and 5<10        = {r4}")   # False
print(f"not (3>2 and 5<10)      = {r5}")   # False

# ── Really tricky: mixing / // % ──
print("\n-- Tricky Precedence Mix --")
print(f"10 - 4 * 2 + 1    = {10 - 4 * 2 + 1}")    # 3
print(f"2 ** 2 ** 3        = {2 ** 2 ** 3}")        # 256 (right-assoc: 2**(2**3))
print(f"(2 ** 2) ** 3      = {(2 ** 2) ** 3}")      # 64
print(f"-2 ** 2            = {-2 ** 2}")             # -4  (not 4! ** before unary -)
print(f"(-2) ** 2          = {(-2) ** 2}")           # 4


# ── 9. COMPLEX REAL-WORLD EXPRESSIONS ───────────────────────
print("\n" + "=" * 55)
print("  9. REAL-WORLD COMPLEX EXPRESSIONS")
print("=" * 55)

# ── BMI Calculator ──
print("-- BMI Calculator --")
weight_kg = 70
height_m  = 1.75
bmi       = weight_kg / height_m ** 2
category  = ("Underweight" if bmi < 18.5 else
             "Normal"      if bmi < 25   else
             "Overweight"  if bmi < 30   else
             "Obese")
print(f"BMI = {bmi:.2f}  →  {category}")

# ── Grade Calculator ──
print("\n-- Grade from Score --")
scores = [45, 55, 65, 75, 85, 95]
for s in scores:
    grade = ("F" if s < 50 else
             "D" if s < 60 else
             "C" if s < 70 else
             "B" if s < 80 else
             "A")
    print(f"  Score {s} → Grade {grade}")

# ── Leap Year (compound logic) ──
print("\n-- Leap Year Check --")
def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

for yr in [1900, 2000, 2023, 2024, 2100]:
    print(f"  {yr} → leap year? {is_leap(yr)}")

# ── Caesar Cipher (arithmetic + membership) ──
print("\n-- Caesar Cipher (shift=3) --")
def caesar(text, shift=3):
    result = ""
    for ch in text:
        if ch.isalpha():
            base  = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch
    return result

msg       = "Hello, World!"
encrypted = caesar(msg, 3)
decrypted = caesar(encrypted, -3)
print(f"  Original : {msg}")
print(f"  Encrypted: {encrypted}")
print(f"  Decrypted: {decrypted}")

# ── XOR Swap (no temp variable!) ──
print("\n-- XOR Swap (no temp variable) --")
p, q = 42, 99
print(f"  Before: p={p}, q={q}")
p ^= q
q ^= p
p ^= q
print(f"  After : p={p}, q={q}")

# ── Counting set bits (Brian Kernighan's algorithm) ──
print("\n-- Count Set Bits in a Number --")
def count_bits(n):
    count = 0
    while n:
        n &= n - 1      # clears lowest set bit
        count += 1
    return count

for n in [0, 1, 7, 255, 1023]:
    print(f"  {n:>5} = {n:010b}  →  {count_bits(n)} set bits")