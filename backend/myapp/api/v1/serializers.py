from rest_framework import serializers
from myapp.models import Ficha

class FichaSerializer(serializers.Serializers):
    class Meta:
        model = Ficha
        fields = '__all__'
        read_only_fields = ['user']