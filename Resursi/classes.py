class Resource:
    def __init__(self,type,name,quanity):
        self.type = type
        self.name = name
        self.quantity = quanity



    def get_type(self):
        return self.type
    def get_name(self):
        return self.name
    def get_quantity(self):
        return self.quantity

    def get_resources(self):
        print(self.type,self.name,self.quantity)

    def get_resources_without_quantity(self):
        print(self.type,self.name)

    def take_resource(self):
        self.quantity -= 1
    def return_resource(self):
        self.quantity += 1

class User:

    def __init__(self,ime,prezime,iznajmeni_resursi):
        self.ime = ime
        self.prezime = prezime
        self.iznajmeni_resursi = iznajmeni_resursi
        self.br_resursi = 0

    def get_user(self):
        print(self.ime,self.prezime)

    def get_br_resursi(self):
        return self.br_resursi

    def set_iznajemni_resursi(self,resurs):
        self.iznajmeni_resursi.append(resurs)


    def vrati_resurs(self,resurs):
        self.iznajmeni_resursi.remove(resurs)

    def get_iznajmeni_resursi(self):
        for item in self.iznajmeni_resursi:
            item.get_resources_without_quantity()

    def up_br_resursi(self):
        self.br_resursi += 1

    def down_br_resursi(self):
        self.br_resursi -= 1






