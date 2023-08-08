def division(num1,num2):
    if type(num1) not in [int, float] or type(num2) not in [int, float]:
        return "Type Error"
    if num2 == 0:
        return "Division by Zero"
    return round (num1 / num2, 8)
