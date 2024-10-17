# Add your program code here.
print("Welcome to Practicando Diccionarios Octubre 16 2024!")

#  Cambiar valoresPuede cambiar el valor de un elemento específico consultando su nombre clave:
# Cambie el "año" a 2018:
thisdict =    {  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)
# Actualizar diccionario
# El método update() actualizará el diccionario con los elementos del argumento dado.
# El argumento debe ser un diccionario o un objeto iterable con pares clave:valor.
# Actualice el "año" del automóvil utilizando el método update():
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)
#  Eliminar elementos
# Existen varios métodos para eliminar elementos de un diccionario:
#El método pop() elimina el elemento con el nombre de clave especificado:
thisdict =    {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
# El método popitem() elimina el último elemento insertado (en versiones anteriores a la 3.7, se elimina un elemento aleatorio):
thisdict =    {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
# La palabra clave: "DEL"  elimina el elemento con el nombre de clave especificado:
thisdict =    {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
#  DEL  también puede eliminar el diccionario por completo:
thisdict =    {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
# El método clear() vacía el diccionario:
thisdict =    {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

print(" ")

# programa que genere un diccionario con la información del directorio, donde cada elemento corresponda a un cliente y tenga por clave su nif y por valor otro diccionario con el resto de la información del cliente.

# Cadena con los datos de los clientes de la empresa
datos_clientes = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"
# Dividimos la cadena por el caracter de cambio de línea \n y creamos una lista con las subcadenas
lista_clientes = datos_clientes.split('\n')
# Inicializamos el diccionario que va a contener el directorio de clientes a vacío.
directorio = {}
# Dividimos la cadena del primer elemento de la lista de clientes (que contienen los 
# nombres de los campos) por el caracter ; y creamos una lista con los campos.
lista_campos = lista_clientes[0].split(';') 
# Bucle iterativo para recorrer los elementos de la lista lista_clientes.
# la variable cliente recorre desde el segundo elemento hasta el último elemento de la lista 
# (el primer elemento contiene los nombres de campo así que no corresponde a un cliente)
for i in lista_clientes[1:]:
    # Inicializamos el diccionario que va a contener los datos del cliente actual a vacío.
    cliente = {}
    # Dividimos la cadena i por el caracter ; y creamos una lista con las subcadenas con la
    # información del cliente
    lista_info = i.split(';') 
    # Bucle iterativo para recorrer los campos y añadir los pares al diccionario del cliente.
    # j toma valores de 1 al número de campos menos 1. El primer elemento (posición 0) corresponde 
    # al nif y no se añade al diccionario porque se utilizará después como clave en el diccionario
    # principal
    for j in range(1,len(lista_campos)):
        # Condicional. Si el campo actual es descuento convertimos su valor en real
        if lista_campos[j] == 'descuento':
            lista_info[j] = float(lista_info[j])
        cliente[lista_campos[j]] = lista_info[j]
    # Añadirmos un par al diccionario del directorio con la clave el nif del cliente y valor
    # el diccionario que acabamos de crear con el resto de sus datos.
    directorio[lista_info[0]] = cliente
# Mostramos el diccionario por pantalla
print(directorio)

print(" ")

meses = {
'01': 'enero',
'02': 'febrero',
'03': 'marzo',
'04': 'abril',
'05': 'mayo',
'06': 'junio',
'07': 'julio',
'08': 'agosto',
'09': 'septiempre',
'10': 'octubre',
'11': 'noviembre',
'12': 'diciembre'
}
fecha = input("Ingrese la fecha en formato dd/mm/aaaa: ")
dia, mes, ano = fecha.split("/")
print(f"{dia} de {meses.get(mes)} del {ano}")

print(" ")
# diccionario que almacena a los ganadores de la Copa Mundial de la FIFA de 1990 a 2014
# los índices de objetos son números enteros que representan los años de los corazones
vencedores_copas = {1990: 'Alemania', 1994: 'Brasil', 1998: 'Francia',\
                    2002: 'Brasil', 2006: 'Itália', 2010: 'Espana',\
                    2014: 'Alemania', 2018: 'Francia'}

print(vencedores_copas[2002])

print(" ")

# diccionario que almacena masas molares de tres sustancias
# los índices de objetos son cadenas que contienen fórmulas de sustancias
masas_molares = {'H20': 18, 'CO2': 44, 'H2': 2}

print (masas_molares['CO2'])

print(" ")



