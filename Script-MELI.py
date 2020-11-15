import os
import requests

def buscador():
    opcion = int(input("Si desea averiguar 1 usuario, Presione 1, caso contrario, Presione 2."))
    listado_productos = []
    productos = {}
    if opcion == 1:
        try:
                        
            SELLER_ID = input("Ingrese el número de ID que desea buscar: ")
            url = (f"https://api.mercadolibre.com/sites/MLA/search?seller_id={SELLER_ID}")

            payload = {}
            headers= {}

            response = requests.request("GET", url, headers=headers, data = payload)

            data = response.json()
            cantidad = len(data['results'])

            for i in range(cantidad):
                    
                productos['ID'] = data['results'][i]['id']
                productos['TITLE'] = data['results'][i]['title']
                productos['CATEGORY_ID'] = data['results'][i]['category_id']

                url = (f"https://api.mercadolibre.com/categories/{productos['CATEGORY_ID']}")
                response = requests.request("GET", url, headers=headers, data=payload)
                productos['NAME'] = response.json()['name']
                listado_productos.append(productos)
                try:
                    archivo = SELLER_ID + ".log"
                    archivo_existe = os.path.isfile(archivo)
                    with open(archivo,'a+') as file:

                        if not archivo_existe:
                            open(archivo, 'w')
                        file.writelines(str(listado_productos))
                except IOError:
                    print("Ocurrio un error con el archivo")

        except IOError:
            print ("Opción ingresada Incorrecta !")

    elif opcion == 2:
        try:

            cantidad_users = int(input("Ingrese la cantidad de usuarios que desea buscar: "))
            IDS= ""
            contador = 0
            for i in range (1, cantidad_users+1):
                SELLER_ID = input(f"Ingrese el número del {i} ID que desea buscar, para ello ingrese MLA seguido del ID: ")
                contador += 1
                if contador != cantidad_users:
                    coma = ","
                else:
                    coma = ""
                IDS += SELLER_ID + coma
                url = ("https://api.mercadolibre.com/items?ids="+IDS+"&attributes={id,title,category_id,name}&access_token=$ACCESS_TOKEN")
                payload = {}
                headers= {}

                response = requests.request("GET", url, headers=headers, data = payload)

                data = response.json()
                cantidad = len(data['results'])

                for i in range(cantidad):
                        
                    productos['ID'] = data['results'][i]['id']
                    productos['TITLE'] = data['results'][i]['title']
                    productos['CATEGORY_ID'] = data['results'][i]['category_id']

                    url = (f"https://api.mercadolibre.com/categories/{productos['CATEGORY_ID']}")
                    response = requests.request("GET", url, headers=headers, data=payload)
                    productos['NAME'] = response.json()['name']
                    listado_productos.append(productos)
                    try:
                        archivo = input("Ingrese el nombre del archivo: ") + ".log"
                        archivo_existe = os.path.isfile(archivo)
                        with open(archivo,'a+') as file:

                            if not archivo_existe:
                                open(archivo, 'w')
                            file.writelines(str(listado_productos))
                    except IOError:
                        print("Ocurrio un error con el archivo")
        
        except IOError:
                print("Ocurrio un error con el archivo")

buscador()