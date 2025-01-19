from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services.currency_converter import CurrencyConverter

class CurrencyConversionView(APIView):
    """
    Vista para convertir divisas.
    """
    def get(self, request):
        """
        Solicitud GET para convertir una cantidad de dinero de una moneda a otra.
        Parámetros:
        request (Request): El objeto de solicitud HTTP que contiene los parámetros 
                            'amount', 'from_currency' y 'to_currency' en la consulta.
        Retorna:
        Response: 
            - 200 OK con el monto convertido en formato JSON.
            -  HTTP 400 Bad Request para campos inválidos.        
        Excepciones:
            - serializers.ValidationError: Si algún parámetro está ausente o no se puede procesar.
            - ValueError: Si ocurre un error en la conversión.
        Ejemplo de uso:
             Para realizar una solicitud de conversión de 100 USD a EUR:
             GET /convert/?amount=100&from_currency=USD&to_currency=EUR
        """
        print("Incoming parameters:", request.GET)
        amount = request.GET.get('amount', None)
        from_currency = request.GET.get('from_currency', None)
        to_currency = request.GET.get('to_currency', None)

        if not amount or not from_currency or not to_currency:
            return Response(
                {"error": "Debe proporcionar los parámetros 'amount', 'from_currency' y 'to_currency'."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            print(f"Converting {amount} {from_currency} to {to_currency}...")
            converter = CurrencyConverter()
            converted_amount = converter.convert(amount, from_currency, to_currency)
            print(f"Converted amount: {converted_amount}")
            return Response(
                {"converted_amount": converted_amount},
                status=status.HTTP_200_OK
            )

        except ValueError as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )