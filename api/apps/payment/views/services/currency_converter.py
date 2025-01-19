from forex_python.converter import CurrencyRates
from forex_python.converter import RatesNotAvailableError

class CurrencyConverter:
    def __init__(self):
        self.converter = CurrencyRates()

    def convert(self, amount, from_currency, to_currency):
        """
        Convierte una cantidad de dinero de una moneda a otra.
        
        :param amount: Cantidad a convertir (float).
        :param from_currency: Código de la moneda de origen (str), ej: 'USD', 'EUR'.
        :param to_currency: Código de la moneda de destino (str), ej: 'EUR', 'USD'.
        
        :return: Monto convertido (float).
        :raises: RatesNotAvailableError si no se pueden obtener las tasas de cambio.
        """
        try:
            converted_amount = self.converter.convert(from_currency,to_currency,amount)
            return converted_amount
        except RatesNotAvailableError as e:
            raise ValueError(
                f"No se pudo obtener la tasa de cambio entre {from_currency} y {to_currency}. Error: {str(e)}"
                )