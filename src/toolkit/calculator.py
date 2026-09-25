import sys

from .tokenization import OPN, tokenize


def score(operation, num1, num2):
    """
        функция, проверяющая какую операцию мы встретили,
        выполняет действие и возвращает результат
    """
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    else:
        try:
            return num1 / num2
        except ZeroDivisionError:
            print("ошибка: деление на ноль")
            sys.exit(2)


def ans(example): # функция, которая по обратной польской нотации считает выражение
    token = tokenize(example)
    opn = OPN(token)
    
    stack = []
    for i in opn:
        if i[-1].isdigit(): # число записываем в стек
            stack.append(i)
        else:
            """
                для операции достаем 2 последних значения
                с помощью score() находим результат этой операции
                для этих двух значений
            """
            if i == '-' and len(stack) == 1:
                stack[0] = -float(stack[0])
                """
                    если мы ввели '-(2+3)',
                    то в стеке останется одно значение для минуса,
                    значит надо при встрече минуса при одном числе в стеке
                    сделать это число отрицательным
                """
            elif i == '+' and len(stack) == 1:
                
                """
                    при вводе +(2+3), аналогично, 
                    только число менять не надо, 
                    надо просто выйти из этой ветки условия
                """
            else:
                num1 = stack[-2]
                num2 = stack[-1]
                stack.pop()
                stack.pop()
                stack.append(str(score(i, float(num1), float(num2))))
                """вызов функции score"""
    return float(stack[0]) # возвращение результата