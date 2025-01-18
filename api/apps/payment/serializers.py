from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        
    def validate_source_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("El monto de origen debe ser un valor positivo.")
        return value

    def validate_target_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("El monto de destino debe ser un valor positivo.")
        return value
