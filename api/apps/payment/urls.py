from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.payment_view import PaymentViewSet
from .views.currency_conversion_view import CurrencyConversionView

router = DefaultRouter()
router.register(r'payments', PaymentViewSet, basename='payment')

urlpatterns = [
    path('', include(router.urls)),
    path('convert/', CurrencyConversionView.as_view(), name='currency-conversion'),
]