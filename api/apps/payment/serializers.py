import requests # type: ignore
from .models import Payment
from rest_framework import serializers

class PaymentSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Payment.

    Este serializador es responsable de validar, serializar y deserializar
    instancias del modelo `Payment`. Asegura que solo se acepten códigos de país
    en ISO2 válidos para los países de origen y destino, y valida que el monto 
    del pago sea no negativo.

    """
    class Meta:
        model = Payment
        fields = '__all__'

    def validate(self, data):
        """
        Método de validación personalizado para realizar validaciones adicionales.
        """
        if data['source_amount'] <= 0:
            raise serializers.ValidationError("El monto de origen debe ser un valor positivo.")
        
        if data['target_amount'] <= 0:
            raise serializers.ValidationError("El monto de destino debe ser un valor positivo.")
        
        if not self.is_valid_country_code(data["source_country"]):
            raise serializers.ValidationError(f"El código de país de origen {data['source_country']} no es válido.")
        
        if not self.is_valid_currency_code(data["source_currency"]):
            raise serializers.ValidationError(f"El código de moneda de origen {data['source_currency']} no es válido.")
        
        if not self.is_valid_country_code(data["target_country"]):
            raise serializers.ValidationError(f"El código de país de destino {data['target_country']} no es válido.")
        
        if not self.is_valid_currency_code(data["target_currency"]):
            raise serializers.ValidationError(f"El código de moneda de destino {data['target_currency']} no es válido.")

        return data

    def is_valid_country_code(self, country_code):
        """
        Verifica si el código de país proporcionado es válido.

        Parámetros:
            - country_code (str): El código de país que se desea validar (código ISO2).

        Retorna:
        - bool: Devuelve True si el código de país es válido (existe en la lista de códigos ISO2),
        de lo contrario devuelve False.

        Excepciones:
         - `serializers.ValidationError`: Se lanza si hay un error en la solicitud a la API,
        si la respuesta no contiene los datos esperados, o si el formato de la respuesta es inesperado.

       """
        url = "https://countriesnow.space/api/v0.1/countries/iso"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if 'data' not in data:
                raise serializers.ValidationError("The API response does not contain 'data'.")
            iso2_codes = [country.get("Iso2") for country in data["data"] if country.get("Iso2")]
            return country_code in iso2_codes
        except requests.exceptions.RequestException as e:
            raise serializers.ValidationError(f"No se verificó error el código de país debido a\
                                              error en API: {e}")
        except KeyError as e:
            raise serializers.ValidationError(f"Formato de respuesta inesperado: {e}")
        
    def is_valid_currency_code(self, currency_code):
        """
        Verifica si el código de moneda proporcionado es válido.

        Parámetros: currency_code (str): El código de moneda que se desea validar.

        retorna: bool: Devuelve True si el código de moneda es válido (existe en la lista de 
        códigos de moneda),
        """
        url = "https://countriesnow.space/api/v0.1/countries/currency"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if 'data' not in data:
                raise serializers.ValidationError("La respuesta de la API no contiene 'data'.")
            currencies_codes = [country.get("currency") for country in data["data"] if country.get("currency")]
            if currency_code in currencies_codes:
                return True
            return False
        except requests.exceptions.RequestException as e:
                raise serializers.ValidationError(f"No se verificó error el código de país debido a \
                                                  error en API: {e}")
        except KeyError as e:
                raise serializers.ValidationError(f"Formato de respuesta inesperado: {e}")