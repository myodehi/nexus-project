#contact manager
#create a class that models a contact in your address book
#take in user input tp construct a new contact
#push your code to github and send link to Andrew through mail

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
