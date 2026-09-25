# toolkit
Python-пакет с CLI, содержащий калькулятор и конвертер величин.

# Структура

lab_1/                  
├── pyproject.toml
├── pytest.ini
├── README.md
├── src/
│   └── toolkit/
│       ├── __init__.py
│       ├── __main__.py
│       ├── calculator.py
│       ├── converter.py
│       ├── errors.py     
│       ├── tokenization.py
│       └── validation.py               
└── tests/
    ├── __init__.py
    ├── test_calculator.py
    ├── test_cli.py
    └── test_converter.py


# Функции:
1) калькулятор, вычисляющий введённое выражение например:
 2+2*2 или 6 * 4 - (3+5)
2) конвертер единиц, который переводит значения из одной единицы измерения в другую
среди единиц длины, массы, температуры например: 
 20 см = 0.2 м
3) Сообщения, помогающие правильно ввести выражение


# Установка
Требуется python 3.9 или новее
git clone https://github.com/Micle156/lab_1.git
cd lab_1
python -m venv .venv
source .venv/bin/activate       (для Linux/MacOS)
.venv\Scripts\activate          (для Windows cmd)
.\.venv\Scripts\Activate.ps1    (для Windows PowerShell)
pip install -e
pip install pytest
pip install ruff


# Использование
1) калькулятор:
    python -m toolkit calc "22-1"         (21)
    python -m toolkit calc "2+2*(14-9)"   (12)

Особенности:

- операции '+ - * /';
- скобки '( )';
- унарный минус: '-5', '-(2+3)', '3*-2';
- десятичные целые и дробные числа: '1.5 + 2.5'.
- проелы игнорируются


2) Конвертер
    python -m toolkit convert 100 --from km --to m  (100000)
    python -m toolkit convert 25 --from c --to f    (77.0)
    python -m toolkit convert 1.5 --from kg --to g  (1500)


Поддерживаются:
- длина (cm, m, km, mm)
- масса (kg, g)
- температура (c, f, k)

Особенности:
- регистр не учитывается
- можно переводить только из данных единиц в данные из одной группы
- температура допустима не меньше абсолютного нуля


# Справка
python -m toolkit --help
python -m toolkit calc --help
python -m toolkit convert --help


# Обработка ошибок
Программа проверяет данные и выводит понятные сообщения об ошибках, например:
- деление на ноль
- температура ниже абсолютного нуля
- неизвестная единица измерения

коды выхода:
0 - успешно завершённая программа
2 - ошибка программы

# Тестирование

python -m pytest                                       (все тесты)
python -m pytest test/test_calculator.py               (конкретный файл)
python -m pytest test/test_calculator.py::test_1       (конкретный тест)
python -m pytest tests/ -k "test_1"                    (по шаблону)
python -m pytest -v                                    (подробный)
python -m pytest -x                                    (остановиться на первой ошибке)
python -m pytest  --maxfail=N                          (остановится после N ошибок)
python -m pytest -1                      (показатьь локальные переменные при ошибках)
python -m pytest --1f                    (запустить неудачные тесты из последнего запуска)
python -m pytest --ff                    (запустить сначала неудачные, потом все остаьные)

# ruf

ruff check .          (проверить код)
ruff check --fix .    (исправить безопасные проблемы)
ruff format .         (отформатировать)

# Зависимости

- Python 3.9+
- стандартная библиотека (argparse, sys)
- pytest
- ruff