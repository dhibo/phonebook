from rest_framework import serializers
from .models import Contact, PhoneNumber

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name']

class PhoneNumberSerializer(serializers.ModelSerializer):
    contact_id = serializers.IntegerField(required=True)

    class Meta:
        model = PhoneNumber
        fields = ['id','contact_id','phone']
        
        
        
        
        
        
        
        
        
        
 