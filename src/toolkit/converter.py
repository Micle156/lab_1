def conv(value: str, from_unit: str, to_unit: str):  # функция конвертации
    value = float(value)

    # перевод в нижний регистр единиц (конвертер не восприимчив к регистру)
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    """
        в зависимости от единицы, из которой конвертируем, создаем словарь,
        в котором считаем конвертированное значение во всех единицах
        из соответствующей группы
    """
    if from_unit[-1] == "m":
        if from_unit == "mm":
            slovar = {
                "mm": float(value),
                "cm": float(value) / 10,
                "m": float(value) / 1000,
                "km": float(value) / 10 ** (6),
            }
        elif from_unit == "cm":
            slovar = {
                "mm": float(value * 10),
                "cm": float(value),
                "m": float(value) / 100,
                "km": float(value) / 10 ** (5),
            }
        elif from_unit == "m":
            slovar = {
                "mm": float(value * 1000),
                "cm": float(value * 100),
                "m": float(value),
                "km": float(value) / 10 ** (3),
            }
        else:
            slovar = {
                "mm": float(value * 10 ** (6)),
                "cm": float(value * 10 ** (5)),
                "m": float(value) * 1000,
                "km": float(value),
            }
    elif from_unit[-1] == "g":
        if from_unit == "g":
            slovar = {"g": float(value), "kg": float(value) / 1000}
        elif from_unit == "kg":
            slovar = {"g": float(value) * 1000, "kg": float(value)}
    else:
        if from_unit == "c":
            slovar = {
                "c": float(value),
                "f": float(value) * 1.8 + 32,
                "k": float(value) + 273.15,
            }
        elif from_unit == "f":
            slovar = {
                "c": (float(value) - 32) / 1.8,
                "f": float(value),
                "k": (float(value) - 32) / 1.8 + 273.15,
            }
        elif from_unit == "k":
            slovar = {
                "c": float(value) - 273.15,
                "f": (float(value) - 273.15) * 1.8 + 32,
                "k": float(value),
            }

    return slovar[to_unit]