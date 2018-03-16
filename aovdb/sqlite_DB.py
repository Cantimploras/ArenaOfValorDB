import sqlite3
from personajes import Personaje

conn = sqlite3.connect('jDbArena.db')




c = conn.cursor()
'''
# CREACION DE LA TABLA
c.execute("""CREATE TABLE personajes (
            nombre text,
            apodo text,
            rol text,
            precioOro real,
            precio real,
            maxHP real,
            maxMana real,
            movSpeed real,
            armor real,
            magicDefense real
            )""" )
'''


def __init__(self, dataFrame_subscriber_content):
    self.dataFrame_subscriber_content = dataFrame_subscriber_content

def insert_per(per):
    with conn:
        c.execute("INSERT INTO personajes VALUES (:nombre, :apodo, :rol, :precioOro, :precio, :maxHP, :maxMana, :movSpeed, :armor, :magicDefense)",{'nombre': per.nombre, 'apodo': per.apodo, 'rol': per.rol , 'precioOro': per.precioOro, 'precio': per.precio, 'maxHP': per.maxHP, 'maxMana': per.maxMana, 'movSpeed': per.movSpeed, 'armor': per.armor, 'magicDefense': per.magicDefense})


def buscar_por_precioOro(precioOro):
    c.execute("SELECT * FROM personajes WHERE precioOro=:precioOro", {'precioOro': precioOro})
    return c.fetchall()


def buscar_por_nombre(nombre):
    c.execute("SELECT * FROM personajes WHERE nombre=:nombre", {'nombre': nombre})
    return c.fetchall()



def buscar_todo():
    c.execute("SELECT * FROM personajes")
    return c.fetchall()

'''
# CREACION DE PERSONAJES
ejLaurie = Personaje('Lauriel','The Archangel','Mage','18888 Monedas',' 1199 TR','3019','490','340','87 / 12.6%','50 / 7.6%')

insert_per(ejLaurie)

ejRaz = Personaje('Raz','Asesino','13888 Monedas',' 999 TR','3235','0','390','89 / 12.9%','50 / 7.6%')

insert_per(ejRaz)
'''

'''
#Buscar por Nombre
test = buscar_por_nombre('Raz')
print(test)
'''

#conn.close()