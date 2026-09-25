def tokenize(example):  # разбиение строки на отдельные токены
    example = example.replace(" ", "")
    token = []
    number = ""
    flag = 0
    for i in example:
        # если встреченный символ - число или точка, записываем в number
        if i.isdigit() and len(number) == 0:
            number = i
        elif i.isdigit() and len(number) != 0:
            number += i
        elif i == ".":
            number += "."
        elif i == "(":
            if number != "":
                token.append(number)
            token.append(i)
            number = ""
        elif i == ")":
            token.append(number)
            token.append(i)
            number = ""
            flag = 1
        else:
            if number != "":
                token.append(number)
                token.append(i)
                number = ""
            elif flag == 1:
                flag = 0
                token.append(i)
            else:
                number = i
        """
            если встреченный символ - операция, то:
            если это не унарный + или -, то:
            добавляем в token number и операцию
            иначе:
            записываем его в number 
            т.е. начинаем с него новое число
        """
    if number != "":
        token.append(number)  # добавляем последнее число
    return token


def OPN(token):  # перевод в обратную польскую нотацию
    stack = []
    opn = []

    # приоритеты операций
    priority = {"+": 2, "-": 2, "*": 1, "/": 1, "(": 3}
    """
        скобка добавляется в стек,
        все операции в скобках тоже должны записаться в стек
        чтобы записать их в стек делаем приоритет скобок = 3
    """

    for i in token:
        if i[-1].isdigit():  # если встретили число, добавили в список
            opn.append(i)
        elif i == "(":  # открывающуюся скобку добавляем в список
            stack.append(i)
        elif i == ")":
            while stack[-1] != "(":
                opn.append(stack[-1])
                stack.pop()
            stack.pop()
            """
                при встрече ')':
                достаем все операции до '(' из стека в список.
                '(' убираем из стека
            """
        else:
            while len(stack) != 0 and priority[i] >= priority[stack[-1]]:
                opn.append(stack[-1])
                stack.pop()
            stack.append(i)

        """
            если встретили операцию:
            пока в стеке операции ниже или равны по priority,
            из стека переносим их в массив.
            Потом добавляем операцию в стек
        """

    # в стеке остались операции, убираем их в список
    while len(stack) > 0:
        opn.append(stack[-1])
        stack.pop()
    return opn
