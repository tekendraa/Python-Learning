# Arithmetic Operators
a = 10
b = 3

addition = a + b        # Addition: 13
subtraction = a - b     # Subtraction: 7
multiplication = a * b  # Multiplication: 30
division = a / b        # Division: 3.3333...
floor_division = a // b # Floor Division: 3
modulus = a % b         # Modulus: 1
exponentiation = a ** b # Exponentiation: 1000

# Comparison Operators
equal = (a == b)        # Equal: False
not_equal = (a != b)    # Not Equal: True
greater_than = (a > b)  # Greater Than: True
less_than = (a < b)     # Less Than: False
greater_equal = (a >= b)# Greater Than or Equal To: True
less_equal = (a <= b)   # Less Than or Equal To: False

# Logical Operators
x = True
y = False

logical_and = x and y   # Logical AND: False
logical_or = x or y     # Logical OR: True
logical_not = not x     # Logical NOT: False

# Bitwise Operators
c = 5  # 0b0101
d = 3  # 0b0011

bitwise_and = c & d     # Bitwise AND: 1 (0b0001)
bitwise_or = c | d      # Bitwise OR: 7 (0b0111)
bitwise_xor = c ^ d     # Bitwise XOR: 6 (0b0110)
bitwise_not = ~c        # Bitwise NOT: -6 (0b...1010)
left_shift = c << 1     # Left Shift: 10 (0b1010)
right_shift = c >> 1    # Right Shift: 2 (0b0010)

# Assignment Operators
e = 5
e += 3  # e = e + 3: 8
e -= 2  # e = e - 2: 6
e *= 2  # e = e * 2: 12
e /= 3  # e = e / 3: 4.0
e %= 3  # e = e % 3: 1.0
e **= 2 # e = e ** 2: 1.0
e //= 2 # e = e // 2: 0.0

# Identity Operators
f = [1, 2, 3]
g = [1, 2, 3]
h = f

identity_is = (f is h)      # Identity: True
identity_is_not = (f is not g) # Identity: True

# Membership Operators
membership_in = (1 in f)    # Membership: True
membership_not_in = (4 not in f) # Membership: True