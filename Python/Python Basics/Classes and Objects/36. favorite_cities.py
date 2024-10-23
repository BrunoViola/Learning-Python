class City:
   def __init__(self, name, country, population, landmarks):
      self.name = name
      self.country = country
      self.population = population
      self.landmarks = landmarks

new_york = City('New York', 'USA', 8468000, ['Central Park', 'Metropolitan Museum of Art', 'Times Square'])
paris = City('Paris', 'France', 2103000, ['Eiffel Tower','Arc de Triomphe', 'The Louvre'])

print(vars(new_york))
print(vars(paris))