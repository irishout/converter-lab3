from coefficients_and_categorys import conversion_rates, units_dict

#класс для конвертации физ величин
class Physical_operations:
    
    def convert_physical(self, category: str, unit_1: str, unit_2: str, value: float):

        #для температуры отдельная логика
        if category == 'Температура':
            if unit_1 == "Цельсии" and unit_2 == "Кельвины":
                value =  value + 273.15
            elif unit_1 == "Цельсии" and unit_2 == "Фаренгейты":
                value = (value * 9/5) + 32
            elif unit_1 == "Кельвины" and unit_2 == "Цельсии":
                if value < 0:
                    pass #0 по кельвину

                value = value - 273.15
            elif unit_1 == "Кельвины" and unit_2 == "Фаренгейты":
                if value < 0:
                    pass #0 по кельвину

                value = (value - 273.15) * 9/5 + 32
            elif unit_1 == "Фаренгейты" and unit_2 == "Цельсии":
                value = (value - 32) * 5/9
            elif unit_1 == "Фаренгейты" and unit_2 == "Кельвины":
                value = (value - 32) * 5/9 + 273.15
            else:  # Если единицы одинаковые
                value = value 
            return round(value, 4)

        coefficients = conversion_rates.get(category)
        basic_unit_coeff = coefficients.get(unit_1)
        converted_unit_coeff = coefficients.get(unit_2)

        converted_unit = value * basic_unit_coeff / converted_unit_coeff

        return round(converted_unit, 4)

