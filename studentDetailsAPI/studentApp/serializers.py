from rest_framework.serializers import ModelSerializer
from studentApp.models import student

class studentSerializer(ModelSerializer):
    class Meta:
        model=student
        # fields=['name','age','standard']
        fields='__all__'
