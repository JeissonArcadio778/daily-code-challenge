"""
Agenda telefónica:
Crea una pequeña agenda telefónica donde se pueda agregar, editar y eliminar contactos. Usa un diccionario para guardar la información de los contactos.
"""

contacts: dict = {}

class Contact:
    def __init__(self, name, mobile_phone) -> None:
        self.name = name
        self.mobile_phone = mobile_phone
    
    def show_phone_phone(self):
        return f"{self.mobile_phone}"
    
    def show_name(self):
        return f"{self.name}"


class TelephoneAgend:
    
    def agregate_to_contacts(contact: Contact) -> None:
        contacts[contact.name] = contact.mobile_phone
        
    def show_contacts() -> list:
        return [name for name in contacts.keys()]


lokita: Contact = Contact(name="Sara", mobile_phone="318")

print(lokita.show_name())
print(lokita.show_phone_phone) # Print my method
print(lokita.show_phone_phone())


TelephoneAgend.agregate_to_contacts(contact=lokita)

print(TelephoneAgend.show_contacts())