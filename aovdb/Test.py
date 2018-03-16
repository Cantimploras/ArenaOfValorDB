# -*- coding: utf-8 -*-
import obtenerDatos
import sqlite_DB


#print sqlite_DB.buscar_todo()
print

print("Nombre del campeón")
nombre = "xeniel"

#obtenerDatos.dar_alta_personajes(nombre)


# print sqlite_DB.buscar_todo()

print sqlite_DB.buscar_por_nombre(nombre.capitalize())