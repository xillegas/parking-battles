class Street():
    spots = [None, None, None, None, None]
    cars = [None, None, None, None, None]
    def spotChange(self, spot, color):
        self.spots[spot] = color
    
    def printStreet(self):
        for i in self.spots:
            if i is None:
                i = ""
            print("|{:^8}".format(i), end ="|")
        print()
        for i in self.cars:
            if i is None:
                i = "__"
                print("|{:^8}".format(i), end ="|")
            else:
                print("|{:^7}".format(i.shape), end ="|")
        print()
        for i in self.cars:
            if i is None:
                i = ""
                print("|{:^8}".format(i), end ="|")
            else:
                print("|{:^8}".format(i.color), end ="|")
            
    def parkCar(self, spot, car):
        self.cars[spot] = car
        
        
# mi_calle = Street()
# mi_calle.spotChange(0,"blue")

# mi_calle.printStreet()
