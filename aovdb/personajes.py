class Personaje:

    def __init__(self, nombre, apodo, rol, precioOro, precio, maxHP, maxMana, movSpeed, armor, magicDefense):
        self.nombre = nombre
        self.apodo = apodo
        self.rol = rol
        self.precioOro = precioOro
        self.precio = precio
        self.maxHP = maxHP
        self.maxMana = maxMana
        self.movSpeed = movSpeed
        self.armor = armor
        self.magicDefense = magicDefense

    def datosCompletos(self):
        return '{} {} {} {} {} {} {} {} {} {}'.format(self.nombre, self.apodo, self.rol, self.precioOro, self.precio, self.maxHP, self.maxMana, self.movSpeed, self.armor, self.magicDefense)
