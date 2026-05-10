import random
import datetime
import json

tiempo = []
for i in range(5):
    tiempo.append(random.randint(13,20))

maxima = minima = tiempo[0]
media = 0
for tiempi in tiempo:
    if tiempi > maxima:
        maxima = tiempi
    if tiempi < minima:
        minima = tiempi
    media += tiempi

media = media/5

# Esto prepara la fecha : AAAAMMDD
data = datetime.date.today()
data_format = data.strftime("%Y%m%d")

# Esto prepara los datos para que sean un JSON 
resultados = {
    "maxima": maxima,
    "minima": minima,
    "media": media
}

# Guardamos el archivo .json
with open(f"temp_{data_format}.json", "w", encoding='utf-8') as fitx:
    json.dump(resultados, fitx, indent=4)

print(f"Hecho! Archivo temp_{data_format}.json creado.")
