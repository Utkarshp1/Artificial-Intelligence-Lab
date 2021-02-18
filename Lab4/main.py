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
ant = AntColony(alpha=3, beta=3, rho=0.1, Q=0.2, city_distances=city_distances, max_iter=100, num_ants=num_cities, sigma=num_cities)
ant.optimisation()
print(time.time()-start_time)
print(ant.best_cost)
print(ant.best_tour)
print(ant.tours)

# sum = 0
# for i, city in enumerate(ant.best_tour[:-1]):
    # sum +=city_distances[city][ant.best_tour[(i+1)%num_cities]]

# print(sum)

plt.figure()
plt.plot(ant.tours)
plt.savefig("graph.png")