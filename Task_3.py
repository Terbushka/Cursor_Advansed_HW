"""
class Profile:
    Create regular class taking 8 params on init - name, last_name, phone_number, address, email, birthday, age, sex
    Override a printable string representation of Profile class and return: list of the params mentioned above
"""


class Profile:
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex
        self.parameters = [self.name, self.last_name, self.phone_number, self.address, self.email, self.birthday,
                           self.age, self.sex]
        print(f"{self.name}  your profile created successfully")

    def __str__(self):
        return f' It is {self.name} profile: {self.parameters}'


person = Profile('Anton', 'Ukhin', '+380986745341', 'Yampil/Ukraine', 'antonUkhin@gmail.com', '09.02.1996', '25',
                 'male')

print(person)