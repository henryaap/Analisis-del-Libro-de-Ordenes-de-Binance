import requests
import time

link_api= "https://fapi.binance.com"

def libro_ordenes(symbol, limit):
    endpoint= "/fapi/v1/depth"
    params = {
        "symbol": symbol,
        "limit": limit
    }
    resultado = requests.get(f'{link_api}{endpoint}', params = params)
    data = resultado.json()
    return data

while True: 
    try:
        symbol = input('Crypto: ') + 'usdt' # nombre de la criptomoneda futuros de binance
        limit = 500 # cantidad de ordenes 
        grupo = 10
        orden_book = libro_ordenes(symbol, limit)
    except:
        time.sleep(4.0)
        print('Ocurrió un error...')
        continue 

    # logica

    punto_compra = [[0,0],[0,0]]
    precioTotal = 0
    cantidadTotal = 0
    contador = 0
    print('Compra!')

    for bid in orden_book["bids"]:
        precioTotal+= float(bid[0])
        cantidadTotal+= float(bid[1])
        if contador<(grupo-1):
            contador+=1
        else:
            if punto_compra[0][1]<(cantidadTotal/grupo):
                punto_compra[0] = [precioTotal/grupo, cantidadTotal/grupo]
            elif punto_compra[1][1]<(cantidadTotal/grupo):
                punto_compra[1] = [precioTotal/grupo, cantidadTotal/grupo]
            precioTotal = 0
            cantidadTotal = 0
            contador = 0

    print(punto_compra[0][0], '---->cantidad de ordenes acumuladas: ', punto_compra[0][1])
    print(punto_compra[1][0], '---->cantidad de ordenes acumuladas: ', punto_compra[1][1]) 

# +++++++++++++++++++

    punto_venta = [[0,0],[0,0]]
    precioTotal = 0
    cantidadTotal = 0
    contador = 0
    print('Venta!')

    for ask in orden_book['asks']:
        precioTotal+= float(ask[0])
        cantidadTotal+= float(ask[1])
        if contador<(grupo-1):
            contador+=1
        else:
            if punto_venta[0][1]<(cantidadTotal/grupo):
                punto_venta[0] = [precioTotal/grupo, cantidadTotal/grupo]
            elif punto_venta[1][1]<(cantidadTotal/grupo):
                punto_venta[1] = [precioTotal/grupo, cantidadTotal/grupo]
            precioTotal = 0
            cantidadTotal = 0
            contador = 0

    print(punto_venta[0][0], '---->cantidad de ordenes acumuladas: ', punto_venta[0][1])
    print(punto_venta[1][0], '---->cantidad de ordenes acumuladas: ', punto_venta[1][1])   
    # fin                    