from coefficients_and_categorys import conversion_rates
import requests
import xml.etree.ElementTree as ET
from datetime import datetime

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

                value = value - 273.15
            elif unit_1 == "Кельвины" and unit_2 == "Фаренгейты":


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



class Currency_operations:
    def __init__(self):
        self.rates = {}
        self.update_exchange_rates()

    def update_exchange_rates(self):
        url = "https://www.cbr.ru/scripts/XML_daily.asp"

        # Делаем запрос
        response = requests.get(url)
        response.encoding = 'windows-1251'  #кодировка ЦБ РФ
        
        if response.status_code == 200:
            # Парсим XML
            root = ET.fromstring(response.text)
            
            for valute in root.findall('Valute'):
                char_code = valute.find('CharCode').text
                value = float(valute.find('Value').text.replace(',', '.'))
                nominal = int(valute.find('Nominal').text)
                
                # Рассчитываем курс за 1 единицу
                rate = value / nominal
                self.rates[char_code] = rate
            
            # Добавляем RUB
            self.rates['RUB'] = 1.0
            
        
        else:
            print(f"Ошибка HTTP: {response.status_code}")

    def convert_currency(self, unit_1: str, unit_2: str, value: float):
        unit_1 = unit_1.split(' ')[1]
        unit_2 = unit_2.split(' ')[1]
        value_in_RUB = value * self.rates[unit_1]
        edited_value = value_in_RUB / self.rates[unit_2]
        return edited_value

a = Currency_operations()
a.update_exchange_rates()
print(a.convert_currency('🇺🇸 USD - Доллар США', '🇪🇺 EUR - Евро', 1))



   
