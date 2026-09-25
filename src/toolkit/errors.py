class ValidationError(Exception):
    """
    Базовая ошибка валидации.
    нужно, чтобы разделять свои ошибки от ошибок программы
    """



class EmptyInputError(ValidationError):
    """Пустой ввод"""



class BadCharacterError(ValidationError):
    """Недопустимый символ"""



class UnknownUnitError(ValidationError):
    """Единица измерения не распознана"""



class IncompatibleUnitsError(ValidationError):
    """Единицы из разных групп"""



class AbsolutZeroError(ValidationError):
    """температура ниже абсолютного нуля"""



class BinOperatorsError(ValidationError):
    """2 бинарных оператора подряд"""



class UncorrectValueError(ValidationError):
    """больше одной точки в числе"""