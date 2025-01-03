class User:
    def __init__(self, name=None, email=None, drivers_license=None):
        self.name = name
        self.email = email
        self.drivers_license = drivers_license
    

alice = User(name="Alice", email="alice@yahoo.com", drivers_license="1234567")
print(alice)