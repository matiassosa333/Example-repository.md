#Configuracio del juego
VIDAS_DISPONIBLES = 6
PALABRA_WIN = list('logica')

def obtener_fila_verificada(PALABRA_WIN, palabra_ingresada):
    cant_palabra_encontrar = len(PALABRA_WIN)
    letras_verificadas= []
    for posicion in range(cant_palabra_encontrar): #este bucle repite el proceso para comparar letra por letra y posicion
        
         # es igual el indice 0 de Palabra win a indice 0 de palabra_ingresada
        las_letras_son_iguales = PALABRA_WIN[posicion] == palabra_ingresada[posicion]

        # la letra del indice 0 de palabra_ingresada en la palabra_win
        la_letra_existe_en_la_palabra = palabra_ingresada[posicion] in PALABRA_WIN

        if las_letras_son_iguales:
            # si se cumple guardamos en la lista de letras verificadas
            letras_verificadas.append('['+palabra_ingresada[posicion]+']')

        elif la_letra_existe_en_la_palabra:
            letras_verificadas.append('('+palabra_ingresada[posicion]+')') 

        else:
            letras_verificadas.append(palabra_ingresada[posicion])

        
    return letras_verificadas

# bucle principal (Utilizamos bucle while para que termine si la vida es menor a 0)
while VIDAS_DISPONIBLES > 0:
    print(f'te quedan {VIDAS_DISPONIBLES} intentos') #tanto print como la palabra que ingresa el usuario dentro para que python determine si seguir o terminar
    palabra_ingresada = list(input('ingrese una palabra con 6 letras: '))

    VIDAS_DISPONIBLES -=1
    resultado = obtener_fila_verificada(PALABRA_WIN, palabra_ingresada)
    print(resultado)