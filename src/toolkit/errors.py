class ValidationError(Exception):
    """
    Базовая ошибка валидации.
    нужно, чтобы разделять свои ошибки от ошибок программы
    """
    pass


class EmptyInputError(ValidationError):
    """Пустой ввод"""
    pass


class BadCharacterError(ValidationError):
    """Недопустимый символ"""
    pass


class UnknownUnitError(ValidationError):
    """Единица измерения не распознана"""
    pass


class IncompatibleUnitsError(ValidationError):
    """Единицы из разных групп"""
    pass


class AbsolutZeroError(ValidationError):
    """температура ниже абсолютного нуля"""
    pass


class BinOperatorsError(ValidationError):
    """2 бинарных оператора подряд"""
    pass


class UncorrectValueError(ValidationError):
    """больше одной точки в числе"""
    pass

class NoBinOperatorError(ValidationError):
    """"""
    pass