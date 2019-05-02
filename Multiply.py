# Recursive multiplication without using the multiplication or division operator
def multiply(a, b):

    # Raise value error for invalid input
    if type(a) != int or type(b) != int:
        raise ValueError()

    # return 0 if a is 0
    if a == 0:
        return 0

    # Flip a's sign if a is negative
    if a < 0:
        return -multiply(-a, b)

    # recursively add b
    if a > 0:
        return b + multiply(a-1, b)

# Multiplication using bit manipulation
def multiplyShift(a, b):

    # Raise value error for invalid input
    if type(a) != int or type(b) != int:
        raise ValueError()

    # Swap a and b if a is negative and b is positive
    if a < 0 and b > 0:
        a, b = b, a

    # take absolute values if both a and b are positive
    elif a < 0 and b < 0:
        a, b = -a, -b

    answer = 0
    shiftValue = 0

    # While first number is not 0
    while (a):

        #Check if bit is set, and left shift b and add value to answer
        if (a & 1):
            answer += b << shiftValue

        # Update place value for shifting, and right shift a
        shiftValue += 1
        a >>= 1

    return answer



