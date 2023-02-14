from rest_framework import viewsets
from .models import Contact, PhoneNumber
from .serializers import ContactSerializer, PhoneNumberSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def ContactViewSet(request):
    queryset = Contact.objects.values('name')
    serializer_class = ContactSerializer(queryset,many=True)
    return Response(serializer_class.data)

@api_view(['GET'])
def PhoneNumberViewSet(request):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerializer(queryset,many=True)
    return Response(serializer_class.data)

@api_view(['POST'])
def create_contact(request):
    contact_data = request.data
    contact_serializer = ContactSerializer(data=contact_data)
    if contact_serializer.is_valid(raise_exception=True):
        contact = contact_serializer.save()
    response_data = {
        'Contact': ContactSerializer(contact).data,
    }
    return Response(response_data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def create_PhoneNumber(request):
    phoneNumber_data = request.data
    phoneNumber_serializer = PhoneNumberSerializer(data=phoneNumber_data)
    if phoneNumber_serializer.is_valid():
        phoneNumber_serializer.save()
        return Response(phoneNumber_serializer.data, status=status.HTTP_201_CREATED)
    return Response(phoneNumber_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_contact_with_multiple_numbers(request):
    contact_data = request.data.get('contact')
    phone_numbers_data = request.data.get('phone_numbers')

    contact_serializer = ContactSerializer(data=contact_data)
    if contact_serializer.is_valid(raise_exception=True):
        contact = contact_serializer.save()

    phone_numbers = []
    print(contact.id)
    for phone_number_data in phone_numbers_data:    
        phone_number_data['contact_id'] = contact.id
        phone_number_serializer = PhoneNumberSerializer(data=phone_number_data)
        if phone_number_serializer.is_valid(raise_exception=True):
            phone_number = phone_number_serializer.save()
            phone_numbers.append(phone_number)

    response_data = {
        'contact': ContactSerializer(contact).data,
        'phone_numbers': PhoneNumberSerializer(phone_numbers, many=True).data
    }
    return Response(response_data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def ContactPhoneList(request):
    queryset = Contact.objects.all()
    serializer = ContactSerializer(queryset, many=True)
    contact_data = serializer.data

    for contact in contact_data:
        contact_id = contact['id']
        phone_numbers = PhoneNumber.objects.filter(contact_id=contact_id)
        phone_numbers_serializer = PhoneNumberSerializer(phone_numbers, many=True)
        contact['phone_numbers'] = phone_numbers_serializer.data

    return Response(contact_data)

