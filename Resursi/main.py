from classes import *

r1 = Resource("Laptop","Acer",10)
r2 = Resource("PC","MSI",10)
r3 = Resource("Tablet","Apple",10)

list_resources = [r1,r2,r3]
for item in list_resources:
    item.get_resources()



u1 = User("Viktor","Grozdanovski",[])

while True:
    question = input("Do you want to lend a resource? ")
    if question.lower() == "yes":
        print("Available Resources.")
        for item in list_resources:
            item.get_resources()

        resource = input("Choose type of resource: ")

        if resource.lower() == "laptop":
            u1.set_iznajemni_resursi(r1)
            u1.up_br_resursi()
            r1.take_resource()

        elif resource.lower() == "pc":
            u1.set_iznajemni_resursi(r2)
            u1.up_br_resursi()
            r2.take_resource()
        elif resource.lower() == "tablet":
            u1.set_iznajemni_resursi(r3)
            u1.up_br_resursi()
            r3.take_resource()




    elif question.lower() == "no":
        if u1.br_resursi > 0:
            last_question = input("Do you want to reutrn a resource? ")
            if last_question.lower() == "yes":
                u1.get_iznajmeni_resursi()
                vrati_resurs = input("Odberete resurs za vrakanje: ")
                if vrati_resurs.lower() == "laptop":
                    u1.vrati_resurs(r1)
                    r1.return_resource()
                    u1.down_br_resursi()


                elif vrati_resurs.lower() == "pc":
                    u1.vrati_resurs(r2)
                    r2.return_resource()
                    u1.down_br_resursi()


                elif vrati_resurs.lower() == "tablet":
                    u1.vrati_resurs(r3)
                    r3.return_resource()
                    u1.down_br_resursi()



            elif last_question.lower() == "no":
                quit()

        if u1.br_resursi == 0:
            quit()