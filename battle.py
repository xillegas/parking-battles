from street import Street
from car import Car

mi_calle = Street()
mi_calle.spotChange(0,"blue")
mi_calle.spotChange(3,"blue")

carro1 = Car()
carro2 = Car()
carro1.newColor()
carro2.newColor()

mi_calle.parkCar(0,carro1)
mi_calle.parkCar(4,carro2)

mi_calle.printStreet()
