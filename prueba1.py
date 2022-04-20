

import websockets
import asyncio
import json
import math

#determinar numero primo
def esprimo(num):
    a=2
    while a<=math.sqrt(num):
        if num%a<1:
            return False
        a=a+1
    return num>1

#defino la funcion asincrona
async def listen():
    #asigno a la variable url el ws
    url = "ws://209.126.82.146:8080"
    # conexion al servidor
    async with websockets.connect(url) as ws:
        min_number=1000000000000
        max_number=0
        number_of_even_numbers=0
        number_of_odd_numbers=0
        number_of_prime_numbers=0
        for x in range(9999):
            msg = await ws.recv()
            #print(msg)
            y = json.loads(msg)
            #guardo el primer numero
            if y['a']==1 and x==0:
                first_number=y['b']
            #guardo el ultimo numero
            if y['a']==(100):
                last_number=y['b']
            #determino el numero minimo
            if y['b']<min_number:
                min_number=y['b']
            #determino el maximo numero
            if y['b']>max_number:
                max_number=y['b']
            #determino la cantidad de pares
            if (y['b']%2)==0:
                number_of_even_numbers+=1
            #etermino la cantidad de primos
            if (y['b']%2)!=0:
                number_of_odd_numbers+=1
            
            if esprimo(y['b']):
                number_of_prime_numbers+=1

            
        resultados = {'maxNumber':max_number, 'minNumber':min_number,'firstNumber':first_number,'lastNumber':last_number,
        'numPrimos':number_of_prime_numbers,'numpares':number_of_even_numbers,'numimpares':number_of_odd_numbers}
        print(resultados)
        
# inicio la conexion
for bloques in range(5):
    print('bloque numero: ',bloques+1)
    asyncio.get_event_loop().run_until_complete(listen())

