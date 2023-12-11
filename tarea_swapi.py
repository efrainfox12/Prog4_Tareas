import requests
import re

# Pregunta a) ¿En cuántas películas aparecen planetas cuyo clima sea árido?
planet_count_with_arid_climate = 0
planet_url = "https://swapi.dev/api/planets/"
while planet_url:
    planet_response = requests.get(planet_url)
    planet_data = planet_response.json()

    for planet in planet_data['results']:
        if 'arid' in planet['climate']:
            planet_count_with_arid_climate += 1

    planet_url = planet_data['next']

print(f"a) En cuántas películas aparecen planetas cuyo clima sea árido: {planet_count_with_arid_climate}")

# Pregunta b) ¿Cuántos Wookies aparecen en la sexta película?
film_url = "https://swapi.dev/api/films/6/"
film_response = requests.get(film_url)
film_data = film_response.json()

wookies_count = 0
for character_url in film_data['characters']:
    character_response = requests.get(character_url)
    character_data = character_response.json()
    if 'Wookiee' in character_data['species']:
        wookies_count += 1

print(f"b) Cuántos Wookies aparecen en la sexta película: {wookies_count}")

# Pregunta c) ¿Cuál es el nombre de la aeronave más grande en toda la saga?
starship_url = "https://swapi.dev/api/starships/"
starship_response = requests.get(starship_url)
starships_data = starship_response.json()

# Corregir la conversión a entero eliminando las comas
largest_starship = max(starships_data['results'], key=lambda x: int(re.sub('[^0-9]', '', x['length'])))

print(f"c) El nombre de la aeronave más grande en toda la saga es {largest_starship['name']} con una longitud de {largest_starship['length']} metros.")
