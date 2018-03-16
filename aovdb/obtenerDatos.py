# -*- coding: utf-8 -*-
# Sitio: http://www.pythondiario.com
# Autor: Diego Caraballo

# Haciendo pruebas con BeautifulSoup y requests

# Importamos las librerias
from bs4 import BeautifulSoup
import sqlite_DB
from personajes import Personaje
import requests
import time
import os
import nltk
import sqlite_DB
from PIL import Image


def __init__(self, dataFrame_subscriber_content):
    self.dataFrame_subscriber_content = dataFrame_subscriber_content

def dar_alta_personajes(test):


    # Capturamos la url
    url = "https://mobilegamerhub.com/arena-of-valor/character/"+test

    # Capturamos el hml de la pagina web y creamos un objeto Response
    r = requests.get(url)
    data = r.text

    # Creamos el objeto soup y le pasamos lo capturado con request
    soup = BeautifulSoup(data, 'lxml')

    # Buscamos el div para sacar los grados



    nombre= soup.find_all('h1', class_="gold-foil text-left")
    apodo = soup.find_all('p', class_="grey")
    precio = soup.find_all('span', class_="cost")
    rol = soup.find_all('div', class_="specialty")
    datos = soup.find_all('div', class_="attribute")


    # Con [0] saco el primer elemento y con [1] el segundo
    print "Nombre "+ nombre[0].text
    print "Apodo "+ apodo[0].text
    print "Rol "+ rol[0].text


    print "Precio Oro " + precio[0].text +" Oros"
    print "Precio Vouchers " + precio[1].text+" Vouchers"

    #Max HP
    print datos[0].text
    #Max Mana
    print datos[5].text
    #MovSpeed
    print datos[6].text
    #Armor
    print datos[1].text
    #MagicDefense
    print datos[2].text


    test = Personaje(nombre[0].text ,apodo[0].text, rol[0].text, precio[0].text, precio[1].text, datos[0].text, datos[5].text, datos[6].text, datos[1].text, datos[2].text)
    sqlite_DB.insert_per(test)