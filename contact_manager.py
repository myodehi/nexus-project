#contact manager
#create a class that models a contact in your address book
#take in user input tp construct a new contact
#push your code to github and send link to Andrew through mail
"""
class ContactManager:

    def __init__(self, name, phone_number, gender, email_address, postal_address):

        self.name = name
        self.phone_number = phone_number
        self.gender = gender
        self.email_address = email_address
        self.postal_address = postal_address

    def __repr__(self):

        return "Name is {} phone {} gender {} email {} postal {}".format(self.name, self.phone_number, self.gender, self.email_address, self.postal_address )

name = input('name: ')
phone_number = input('phone: ')
gender = input('gender: ')
email_address = input('email: ')
postal_address = input('postal: ')

new_contact = ContactManager(name, phone_number, gender, email_address, postal_address)
print(new_contact)
"""
#add contact, search contact, delete contact

class ContactList:

    def __init__(self, contacts = []):
        self.contacts = contacts

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Successfully added")

    def search_contact(self, name=''):
        name = input('Enter a name to search')
        for contact in self.contacts:
            if contact.name == name:
                return print(contact.name, contact.age, contact.phone, contact.gender)
            else:
                return print('Sorry {} is not found'.format(name))

    def delete_contact(self, name=''):
        name = input("Enter a name to delete")
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                return print('contact removed')
            else:
                return print('Sorry {} is not found'.format(name))

    def get_contact(self):

        for contact in self.contacts:
            print(contact.name, contact.age, contact.phone, contact.gender)
        # else:
        #     return print('sorry no contact found')

class Contact:

    def __init__(self, name='', age='', phone='', gender=''):
        self.name = input('Enter name: ')
        self.age = input('Enter age: ')
        self.phone = input('Enter Phone: ')
        self.gender = input('Enter gender: ')

def main():

    while True:
        new_contact = ContactList()
        answer = int(input('Press 1 to add, 2 to search, 3 to delete and 4 to view all contact'))

        if answer == 1:
            contact = Contact()
            new_contact.add_contact(contact)
        elif answer == 2:
            new_contact.search_contact()
        elif answer == 3:
            new_contact.delete_contact()
        elif answer == 4:
            new_contact.get_contact()
        else:
            print("End here")
            break

main()

