import argparse  # модуль, разбирающий аргументы cmd

from . import calculator, converter

"""
    относительный импорт из пакета toolkit
    (с обычным импортом выходит ошибка No module named ...)
"""

import sys

from .validation import (
    ValidationError,  # отличает ошибки пользователя от ошибок программы
    check_calc,  # ловит ошибки при вводе calc
    check_convert,  # ловит ошибки при вводе converter
)


def build_parser():
    """
    конструктор командной строки:
    здесь описываются все
    комманды, флаги, аргументы, действия при -h
    """

    parser = argparse.ArgumentParser(prog="toolkit")
    """
        prog="toolkit" - имя программы
        parser - место, куда потом складывается описание комманд
    """

    sub = parser.add_subparsers(dest="command", required=True)
    """
        создаем группу подкомманд
        делаем ее обязательной
    """

    calc = sub.add_parser("calc", help="вычислить выражение")
    conv = sub.add_parser("convert", help="конвертировать единицы")
    """
        создаются новые команды.
        всё, что добавляется к calc или conv, 
        относится только к команде,
        к которой добавляется
    """

    calc.add_argument("expression", help="например 5*6")
    calc.set_defaults(func=run_calc)
    """
        добавление огрумента и задание функции по умолчанию, 
        которую надо вызывать при вводе calc:
        без префикса -- это позиционный аргумент, 
        попадет в args.expression
        в arg.func положится функция run_calc
    """

    conv.add_argument("value", help="число")
    conv.add_argument("--from", dest="from_unit", required=True, help="исход единица")
    conv.add_argument("--to", dest="to_unit", required=True, help="результ единица")
    conv.set_defaults(func=run_convert)
    """
        аналогичные действия как с calc:
        задаются аргументы и функция run_convert, 
        которую вызовет args.func(args)
        from зарезервированно, 
        следовательно используется from_unit и аналогично to_unit
        с -- начианается флаг, 
        dest указывает, куда складываем аргумент после флага
    """

    return parser  # парсер сконструирован, дальше все в main


def run_calc(args):
    """
    выполняется при вводе команды calc
    аргументом подается args,
    куда argparse сложил введенные данные
    """
    try:
        check_calc(args.expression)
    except ValidationError as e:
        print(f"Ошибка ввода: {e}", file=sys.stderr)
        sys.exit(2)

    """
        при нахождении ошибки, 
        программа выводит ошибку e в stderr
        и выходит с кодом 2
    """
    result = calculator.ans(args.expression)
    print(result)


def run_convert(args):
    """
    выполняется при вводе команды convert
    аргументами подается args,
    куда argparse сложил введенные данные
    """
    try:
        check_convert(str(args.value), args.from_unit, args.to_unit)
        result = converter.conv(args.value, args.from_unit, args.to_unit)
        print(result)
    except ValidationError as e:
        print(f"Ошибка ввода: {e}", file=sys.stderr)
        sys.exit(2)

    # вызов функции из converter и вывод результата


def main():
    parser = build_parser()  # создание описания комманд
    args = parser.parse_args()
    """
        считывание из cmd и возвращения пространнства с
        полями и введенными данными
    """

    try:
        args.func(args)

        """
            в зависимости от ввода, 
            функция вызовет run_calc или run_convert
        """
    except ValidationError as e:
        """
            сюда попадёт всё, что вылетело из run_*,
            если там нет своего try
        """
        print(f"Ошибка ввода: {e}", file=sys.stderr)
        sys.exit(2)
    # проверка ошибок программы, не заданных в error
    except ValueError:  # проверка конвертера на число с лишними символами
        print("Ошибка: Некорректное числовое значение", file=sys.stderr)
        sys.exit(2)
    except ZeroDivisionError:
        print("Ошибка: деление на ноль", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
