import math

side_ab = float(input("Введите длинну стороны AB:"))
side_bc = float(input("Введите длинну стороны BC:"))
side_ca = float(input("Введите длинну стороны CA:"))
corner = float(input("Введите градус угла:"))

semiperimeter = (side_ab+side_bc+side_ca) / 2
radius = (semiperimeter - side_bc) * math.tan(corner/2)
square = math.pi * pow(radius, 2)
print (square)




