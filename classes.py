class Car():
    firm = None
    model = None
    color = None

    def print_car(self):
        print(self.firm, self.model, self.color)

class Plane():
    def __init__(self, firm="Boeing", model="737", company=None):
        pass
    #     print(firm, model, company)
    #
    #     self.firm = firm
    #     self.model = model
    #     self.company = company
    #
    # def __str__(self):
    #     # return "{} {} {}".format(self.firm, self.model, self.company)
    #     return f"{self.firm} {self.model} {self.company}"


def main():

    my_car = Car()
    my_car.firm = "Tesla"
    my_car.model = "S"
    my_car.color = "black"

    my_car.print_car()
    my_plane = Plane(firm='airbus', model='a330', company="Aeroflot")

    print(my_plane)

    a = 10
    print("variable a = {}".format(str(a)))

    print(f'variable a = {a}')

    s = 'can\'t\ncan'
    print(s)

if __name__ == '__main__':
    main()
    print('sdfsdfsdsdf')
    print('sdfsdfsdfsdfsdfsdf')