import sys
from AntColony import AntColony
import time
import matplotlib.pyplot as plt

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
start_time = time.time()
ant = AntColony(alpha=8, beta=9, rho=0.18, Q=10, city_distances=city_distances, max_iter=num_cities, num_ants=2*num_cities//5)
ant.optimisation()
print(time.time()-start_time)
print(ant.best_cost)
print(ant.best_tour)
print(ant.tours)

plt.figure()
plt.plot(ant.tours)
plt.savefig("graph.png")