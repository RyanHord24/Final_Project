class ContactList:
    lists = []

    def __init__(self, name, contacts=None):
        self._name = name
        self.contacts = []
        ContactList.lists.append(self._name)

    @property
    def name(self):
        print(self._name)

    @name.setter
    def name(self, new_name):
        self._name = new_name
        print(new_name)

    #Add contact function
    def add_contact(self, new_contact):
        self.contacts.append(new_contact)

    def get_contacts(self):
        print(self.contacts)
