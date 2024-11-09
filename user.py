class User:
    def __init__(self, name: str, last_name: str, birth_year: int):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year

    def get_info(self):
        return f"Name: {self.name}, Last name: {self.last_name}, Birth year: {self.birth_year}"
    
    def get_age(self, current_year):
        return f"{current_year - self.birth_year} years old"

class Student(User):
    def __init__(self, name: str, last_name: str, birth_year: int, id_card: str, address: str):
        super().__init__(name, last_name, birth_year)
        self.id_card = id_card
        self.step = 1 
        self.address = address

    def get_id(self):
        return self.id_card
    
    def get_step(self):
        return self.step 
    def get_info(self):
        return f"Name: {self.name}, Last name: {self.last_name}, Birth year: {self.birth_year}, Id number: {self.id_card}, step: {self.step}"
class Address:
    def __init__(self, region, district, street, home):
        self.region = region
        self.district = district
        self.street = street
        self.home = home
    def get_address(self):
        address =  f"{self.region} region, {self.district} district, {self.street} street, {self.home} - house"
        return address
student1_address = Address('Samarkand', 'Pastdarg\'om', 'Amir Temur', 168)
student1 = Student('Bobur', 'Boboyev', 2008, 'N000011', student1_address)
print(student1.get_info())
print(student1.address.get_address())
print(student1.get_age(2024))
print(student1.get_id())
print(student1.get_step())
