
<html>
<h1>Base:</h1>

<h3>Contact:</h3>
<li>id</li>
<li>name</li>
<h3>PhoneNumber</h3>
<li>id</li>
<li>contact_id (foreign key Contact.id)</li>
<li>phone</li>
 
===================
<h1>path:</h1>

<li>-/api/getcontact >> contact name list</li>
<li>-/api/getphoneNumber >> get phone numbers</li>
<li>-/api/contactPhoneList >> get contacts with all related phones</li>
<li>-/api/createContact >> create new contact</li>
<p>{"name": "Ism Abed"}</p>
<li>-/api/createPhoneNumber >> create new phone number</li>
<p>{
                "contact_id": 3,
                "phone": 12345678
            }</p>
<li>-/api/createContactMultiple >> create contact with multiple numbers (error)</li>
<p></p>
</html>
