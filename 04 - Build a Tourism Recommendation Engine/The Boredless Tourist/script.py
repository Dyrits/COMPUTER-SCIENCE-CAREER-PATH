destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ["Erin Wilkes", "Shanghai, China", ["historical site", "art"]]

def get_destination_index(destination):
  return destinations.index(destination)

# print(get_destination_index("Los Angeles, USA"))

# print(get_destination_index("Paris, France"))

# print(get_destination_index("Hyderadab, Inda"))

def get_traveler_location(traveler):
  return get_destination_index(traveler[1])

test_destination_index = get_traveler_location(test_traveler)

# print(test_destination_index)

attractions = [[] for iteration in range(5)]

# print(attractions)

def add_attraction(destination, attraction):
  try: 
    destination_index = get_destination_index(destination)
  except:
    return
  #attractions[destination_index] = [destination]
  attractions[destination_index].append(attraction)
  
add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

# print(attractions)

def find_attractions(destination, interests):
  try: 
    destination_index = get_destination_index(destination)
    return [possible_attraction[0] 
          for interest in interests 
          for possible_attraction in attractions[destination_index] 
          if interest in possible_attraction[1]]
  except:
    return

la_arts = find_attractions("Los Angeles, USA", ["art"])

# print(la_arts)

def get_attractions_for_traveler(traveler):
  traveler_attractions = find_attractions(traveler[1], traveler[2])
  interests_string = ", and the ".join(traveler_attractions)
  return f"Hi {traveler[0]} we think you'll like these places around {traveler[1]}: the {interests_string}."

print(get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']]))
  
  


