from abc import ABC, abstractmethod
from .addressbook import AddressBook

class MyFirstAbstarctClass(ABC):
    @abstractmethod
    def display_contacts(self, contacts):
        pass  
    
    
    @abstractmethod
    def display_one_contact(self, name):
        pass


    # @abstractmethod
    # def display_added_inf(self, name):
    #     pass  



class AddressBookConsoleInterface(MyFirstAbstarctClass):
    def __init__(self, address_book:AddressBook):
        self.address_book = address_book



    def display_contacts(self):
        for contact in self.address_book.data:
            selected_contact = self.address_book.find(contact)
            result = "Name: {}\nPhones: {}\nBirthday: {}\n".format(
                selected_contact.name.value,
                ', '.join(str(phone) for phone in selected_contact.phones.phones),
                selected_contact.birthday
            )
            print(result)

        
    def display_one_contact(self, name):
        selected_contact = self.address_book.find(name)
        if selected_contact:
            result = "Name: {}\nPhones: {}\nBirthday: {}\n".format(
                selected_contact.name.value,
                ', '.join(str(phone) for phone in selected_contact.phones.phones),
                selected_contact.birthday
            )
            print(result)
        else:
            return f"Contact with name {name} not found."
        
    # def display_added_inf(self, name, phones):
    #     selected_contact = self.address_book.find(name)
        
    #     return 



# def main():
#     record1 = Record(Name("John"))
#     record1.phones.phones = ["123-456-7890", "987-654-3210"]
#     record1.birthday = "01/01/1990"  
#     address_book = AddressBook()
#     address_book.add_record(record1)
#     console_interface = AddressBookConsoleInterface(address_book)

#     print(console_interface.display_one_contact('John'))


# if __name__ == '__main__':
#     main()