# Create 2 variables for future operations

x = 0b101001  # Here we create 2 variables with values  x = 41, y = 38
y = 0b100110  # We create bit numbers with the "0b" notation.

print(x, y)

# Bitwise AND -- "&"
# It returns 1 if two of the bits 1 and 0 if one of the bits 1 or both 0

z = x & y  # which makes z = 0b00100000, z = 32

print(bin(z))  # We can use format string to help us to print numbers in bit formation

# Bitwise OR -- "|"
# It returns 1 if one of the bits 1 and returns 0 in other cases

z = x | y  # which makes z = 0b00101111, z = 47

print(bin(z))  # We use built-in bin function to print numbers in bit format

# Bitwise XOR -- "^"
# It returns 1 if one of the bits 1 but not both

z = x ^ y  # which makes z = 0b00001111, z = 15

print(bin(z))

# Bitwise Shift left -- "<<"
# Shifts number by "" bits to left

z = x << 1  # shifts x by 1 bit and creates z = 0b1010010
            # x was                         x = 0b101001
z = x << 4  # which shifts x by 4 bits and  z = 0b1010010000

z = x >> 1  # we can also shift right       z = 0b10100

print(bin(z))
