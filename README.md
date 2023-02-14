Base:
    Contact:
        id
        name
    PhoneNumber
        id
        contact_id (foreign key Contact.id)
        phone
===================
path:
/api/getcontact >> contact name list
/api/getphoneNumber >> get phone numbers
/api/contactPhoneList >> get contacts with all related phones
/api/createContact >> create new contact
/api/createPhoneNumber >> create new phone number
api/createContactMultiple >> create contact with multiple numbers (error)