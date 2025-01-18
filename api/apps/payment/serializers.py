import requests
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

    def validate_amount(self, data):
        """
        Valida que los montos de origen y destino sean valores positivos.

        Parámetros:
            self: La instancia del serializador.
            data: Un diccionario que contiene los datos del pago a validar.
        
        Retorna:
            data: El mismo diccionario de entrada si los montos son válidos.
        
        Excepciones:
            serializers.ValidationError: Si alguno de los montos es no positivo.
        """
        if data['source_amount'] <= 0:
            raise serializers.ValidationError("El monto de origen debe ser un valor positivo.")
        if data['target_amount'] <= 0:
            raise serializers.ValidationError("El monto de destino debe ser un valor positivo.")
        return data

    def validate_source_country(self, value):
        """
        Valida que el código de país de origen sea un ISO2 válido.

        Parámetros:
            self: La instancia del serializador.
            value: valor de entrada de codigo de pais a validar.
        
        Retorna:
            value: El mismo valor si el código ISO2 es válido.
        
        Excepciones:
            serializers.ValidationError: Si alguno de los montos es no positivo.

        """
        if not self.is_valid_country_code(value):
            raise serializers.ValidationError(f"El código de país de origen '{value}' no es válido.")
        return value
    
    def validate_target_country(self, value):
        """
        Valida que el código de país de destino sea un ISO2 válido.

        Parámetros:
            self: La instancia del serializador.
            value: valor de entrada de codigo de pais a validar.
        
        Retorna:
            value: El mismo valor si el código ISO2 es válido.
        
        Excepciones:
            serializers.ValidationError: Si alguno de los montos es no positivo.

        """
        if not self.is_valid_country_code(value):
            raise serializers.ValidationError(f"El código de país de destino '{value}' no es válido.")
        return value
    
    def is_valid_country_code(self, country_code):
        """
        Verifica si el código de país proporcionado es válido.

        Esta función realiza una solicitud a la API de `countriesnow.space` para obtener
        una lista de códigos ISO2 de los países. Luego, verifica si el código de país
        proporcionado (`country_code`) está presente en esa lista.

        Parámetros:
            - country_code (str): El código de país que se desea validar (código ISO2).

        Retorna:
        - bool: Devuelve True si el código de país es válido (existe en la lista de códigos ISO2),
        de lo contrario devuelve False.

        Excepciones:
         - `serializers.ValidationError`: Se lanza si hay un error en la solicitud a la API,
        si la respuesta no contiene los datos esperados, o si el formato de la respuesta es inesperado.

       """
        url = f"https://countriesnow.space/api/v0.1/countries/iso"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if 'data' not in data:
                raise serializers.ValidationError("The API response does not contain 'data'.")
            iso2_codes = [country.get("Iso2") for country in data["data"] if country.get("Iso2")]
            return country_code in iso2_codes
        except requests.exceptions.RequestException as e:
            raise serializers.ValidationError(f"Unable to verify country code due to API error: {e}")
        except KeyError as e:
            raise serializers.ValidationError(f"Unexpected response format: {e}")