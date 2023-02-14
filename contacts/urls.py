from django.urls import path
from .views import ContactViewSet, ContactPhoneList, create_contact_with_multiple_numbers, create_PhoneNumber, PhoneNumberViewSet, create_contact

urlpatterns = [path('getcontact/',ContactViewSet),
path('getphoneNumber/',PhoneNumberViewSet),
path('createContact/',create_contact),
path('createPhoneNumber/',create_PhoneNumber),
path('createContactMultiple/',create_contact_with_multiple_numbers),
path('contactPhoneList/',ContactPhoneList),

]