class MyFamily:
    ''' Building a template for an average family '''
    def __init__(self, name, nkids, ncars, npets):
        ''' Standard family stuff '''
        self.name = name
        self.kids = nkids
        self.cars = ncars
        self.pets = npets

    def add_pets(self):
        ''' What if you buy more pets? '''
        self.pets += 1

    def remove_pets(self):
        ''' What if you lose a pet? '''
        self.pets -= 1

    def add_cars(self):
        ''' You need more cars '''
        self.cars += 1


def main():
    family_name = input('What is your family name? ')
    kids = int(input('How many kids? '))
    pets = int(input('How many Pets? '))
    cars = int(input('How many cars? '))

    # Let's set the first blue print.
    family_name = MyFamily(family_name, kids, cars, pets)

    # Print
    print('You have {} kids, {} pets and {} cars.'.
          format(family_name.kids, family_name.pets, family_name.cars))

    # Options
    family_name.add_pets()

    # What now?
    print('You added a pet')

    print('You have {} kids, {} pets and {} cars.'.
          format(family_name.kids, family_name.pets, family_name.cars))    

if __name__ == '__main__':
    main()
