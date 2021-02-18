import sys
from AntColony import AntColony
import time
import matplotlib.pyplot as plt
import random

file = open(sys.argv[1], "r") 
type = file.readline()

num_cities = int(file.readline())

city_coordinates = []

for i in range(num_cities):
    city = file.readline().split()
    city = (float(coordinate) for coordinate in city)
    city_coordinates.append(city)
    
city_distances = []

for i in range(num_cities):
    distances = file.readline().split()
    distances = [float(distance) for distance in distances]
    city_distances.append(distances)
    
start_node = random.randint(0, num_cities-1)
visited_cities = set()
visited_cities.add(start_node)
tour = []
tour.append(start_node)
current_node = start_node
cost = 0
 
for i in range(num_cities-1):
    distances = city_distances[current_node]
    
    sorted_distances = sorted(range(len(distances)), key=distances.__getitem__)
    j = 0
    
    while (sorted_distances[j] in visited_cities):
        j += 1
        
    visited_cities.add(sorted_distances[j])
    tour.append(sorted_distances[j])
    current_node = sorted_distances[j]
    print(sorted_distances[j], distances[sorted_distances[j]])
    cost += distances[sorted_distances[j]]
    
print(cost)