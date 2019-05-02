import Multiply

def main():
    firstNumber = input("Enter First Number:")
    secondNumber = input("Enter Second Number:")
    try:
        answer = Multiply.multiply(int(firstNumber), int(secondNumber))
        print ("The answer is: %d" %(answer))
    except ValueError:
        print("Those are not integers.")

if __name__ == '__main__':
    main()