import sys
from AntColony import AntColony 

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
    
# print(city_distances[-1])
# print(len(city_distances))
ant = AntColony(alpha=4.0675, beta=6, rho=0.6, Q=1, city_distances=city_distances, max_iter=100, num_ants=100)
ant.optimisation()
print(ant.best_cost)
print(ant.best_tour)