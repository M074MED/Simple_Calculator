num1 = float(input("enter num1: "))
operator = input("enter the operator: ")
num2 = float(input("enter num2: "))


def nums(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    elif operator == "^":
        result = 1    # or return num1**num2 or print(num1**num2) or print(pow(num1, num2))
        for index in range(int(num2)):
            result = result * num1
        return result
    else:
        print("""error!!(wrong operator)!!
            please, enter root correct operator""")


print(nums(num1, operator, num2))
