import json
import os

#objeto persona##############
class Persona:
  def __init__(self, nombre, apellido,edad,email):
    self.nombre = nombre
    self.apellido = apellido
    self.edad = edad
    self.email = email

#funcion mostrar###################
def mostrar():
  with open('data.json') as file:
      data = json.load(file)
      for client in data['personas']:
          print('nombre:', client['nombre'])
          print('apellido:', client['apellido'])
          print('edad:', client['edad'])
          print('correo:', client['correo'])
          print('')

#funcion añadir#####################################
def añadir(persona_a):
  listObj = []
  

  with open('data.json') as fp:
    listObj = json.load(fp)
  
 
  
  listObj['personas'].append({
    'nombre': persona_añadir.nombre,
    'apellido': persona_añadir.apellido,
    'edad': persona_añadir.edad,
    'correo': persona_añadir.email
})
  
  with open('data.json', 'w') as json_file:
      json.dump(listObj, json_file, 
                          indent=4,  
                          separators=(',',': '))
#################################################
#funcion eliminar
def eliminar(n):
  listObj = []

  with open('data.json') as fp:
    listObj = json.load(fp)
    print('eliminaste la persona: ',n)
    listObj['personas'].pop(int(n)-1)

    with open('data.json', 'w') as file:
      json.dump(listObj, file, indent=4)


##########################creo un archivo json con personas############
data = {}
data['personas'] = []
data['personas'].append({
    'nombre': 'Sigrid',
    'apellido': 'Mannock',
    'edad': 27,
    'correo': 'sigrid@hotmail.com'})
data['personas'].append({
    'nombre': 'Joe',
    'apellido': 'Hinners',
    'edad': 31,
    'correo': 'joe@hotmail.com'})
data['personas'].append({
    'nombre': 'Theodoric',
    'apellido': 'Rivers',
    'edad': 36,
    'correo': 'theodo@hotmail.com'})
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

##########################menu############
while True:
  print('MENU: 1. AGREGAR PERSONA 2.ELIMINAR PERSONA 3.MOSTRAR PERSONAS')
  opcion=input()
  if opcion=='1':
    print('1')
    print('nombre')
    nombre=input()
    print('apellido')
    apellido=input()
    print('edad')
    edad=input()
    print('correo')
    correo=input()
    persona_añadir=Persona(nombre,apellido,edad,correo)
    añadir(persona_añadir)
  if opcion=='2':
    print('digite la persona a eliminar')
    persona_eliminar=input()
    eliminar(persona_eliminar)
  if opcion=='3':
    print('3')
    mostrar()

  if opcion!='1' and opcion!='2' and opcion!='3':
    print('OPCION INCORRECTA VUELVA A INTENTAR')