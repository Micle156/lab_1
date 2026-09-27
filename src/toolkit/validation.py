from .errors import (
    AbsolutZeroError,
    BadCharacterError,
    BinOperatorsError,
    EmptyInputError,
    IncompatibleUnitsError,
    UncorrectValueError,
    UnknownUnitError,
    ValidationError,
    NoBinOperatorError,
)

UNITS = {"length": {"mm", "cm", "m", "km"},
               "mass": {"g", "kg"},
               "temp": {"c", "f", "k"},
               }

CHARS_CALC = set("0123456789.+-*/() ")

CHARS_CONV = set("0123456789.-")


def check_calc(expression: str) -> None:
    """ Проверяет выражение для calc на ошибки"""

    if expression.strip() == "":
        raise EmptyInputError("Выражение пустое")

    expr_new = expression.replace('/', '+').replace('*', '+')
    expr_new = expr_new.replace('-', '+')
    expr_new = expr_new.split('+')
    for numeral in expr_new:
        if numeral.strip().count(' ') > 0:
            raise NoBinOperatorError("пропущен оператор")

    expression = expression.replace(' ', '')

    bad = set(expression) - CHARS_CALC
    if bad:
        raise BadCharacterError(
            f"Недопустимые символы: {' '.join(sorted(bad))}"
        )

    # заменяем, чтобы писать меньше условий
    expression_new = expression.replace('-', '+').replace('/', '*')
    if expression_new.count("+++") != 0 \
            or expression_new.count("+*") != 0 \
            or expression_new.count("**") != 0:
        raise BinOperatorsError("лишний оператор")
    
    # заменяем для отдельной проверки двух операторов в начале строки
    expression_new = expression_new.replace('*', '+')
    if len(expression_new) > 1 and expression_new[:2] == '++':
        raise BinOperatorsError("лишний оператор")
    
    expr_new = expression.replace('-', '+')
    expr_new = expr_new.replace('/', '+').replace('*', '+')
    if expr_new[-1] == '+' \
            or expr_new.count("+)") > 0:
        raise ValidationError("пропущен(ы) операнд(ы)")
    """число не заканчивается на +"""

    expr_new = expression.replace('/', '+').replace('*', '+')
    expr_new = expr_new.replace('-', '+')
    if expr_new[0] == '.' \
            or expr_new.count("+.") > 0 \
            or expr_new.count(".+") > 0 \
            or expr_new[-1] == '.':
        raise UncorrectValueError("некорректное число")

    expr_new = expr_new.split('+')
    for numeral in expr_new:
        if numeral.count('.') > 1:
            raise UncorrectValueError("некорректное число")
    """проверяем, что в числах не больше одной точки"""


def check_convert(value: str, unit1: str, unit2: str) -> None:
    """Проверяет аргументы для convert на ошибки"""

    # проверка на ввод выражения без лишних символов
    bad = set(value) - CHARS_CONV
    if bad:
        raise BadCharacterError(
            f"Недопустимые символы: {' '.join(sorted(bad))}"
        )

    if value == "":
        raise EmptyInputError("Выражение пустое")

    for ind in range(len(value)):
        if value[ind] == '-' and ind != 0:
            raise UncorrectValueError("некорректное число")

    if value.count('.') > 1 \
            or (len(value) > 0 and (value[0] == '.' or value[-1] == '.')):
        raise UncorrectValueError("некорректное число")
    """>1 точки или точки с краю числа"""

    # проверка на то, что указаны все единицы
    if not unit1 or not unit2:
        raise ValidationError("Не указаны единицы (--from / --to)")

    unit1 = unit1.lower()
    unit2 = unit2.lower()

    # проверка на то, что единицы известны и из одной группы
    group1 = _find_group(unit1)
    group2 = _find_group(unit2)

    # если функция вернула None
    if group1 is None:
        raise UnknownUnitError(f"Неизвестная единица: {unit1!r}")
    if group2 is None:
        raise UnknownUnitError(f"Неизвестная единица: {unit2!r}")

    # если функция вернула группу, но группы не совпали
    if group1 != group2:
        raise IncompatibleUnitsError(
            f"Нельзя перевести {unit1} ({group1}) "
            f"в {unit2} ({group2})."
        )

    # проверка на ввод числа не ниже абсолютного нуля
    if unit1 == 'c' and float(value) < -273.15 or \
            unit1 == 'k' and float(value) < 0 or \
            unit1 == 'f' and float(value) < -459.67:
        raise AbsolutZeroError("температура ниже абсолютного нуля")


def _find_group(unit: str):
    """
        функция проверяет 
        есть ли в словаре доступных единиц введенная единица
        если есть, то возвращает нужную группу
        если нет, то возваращает None
    """
    for group, units in UNITS.items():
        if unit in units:
            return group
    return None