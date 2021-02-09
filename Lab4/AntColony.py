from Ant import Ant

class AntColony:
    def __init__(self, alpha, beta, rho, Q, city_distances, max_iter, num_ants, init_pheromone=0.1):
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.Q = Q
        self.city_distances = city_distances
        self.max_iter = max_iter
        self.num_ants = num_ants
        
        self.num_cities = len(city_distances)
        self.pheromones = [[init_pheromone for i in range(self.num_cities)] for j in range(self.num_cities)]
        self.best_cost = float('inf')
        self.best_tour = None
        self.best_index = None
        
    def optimisation(self):
        for i in range(self.max_iter):
            ants = [Ant(self.num_cities) for i in range(self.num_ants)]
            
            tour_costs = [ant.construct_tour(self.pheromones, self.city_distances, 
                          self.alpha, self.beta) for ant in ants]
            
            [self.set_best_index(i) for i in range(len(tour_costs)) if tour_costs[i] > self.best_cost]
            
            print(self.best_index)
            self.best_cost = tour_costs[self.best_index]
            self.best_tour = ants[self.best_index].path
            
            for ant in ants:
                delta_pheromone = [[0 for i in range(self.num_cities)] for j in range(self.num_cities)]
                for k, i in enumerate(ant.path):
                    j = ant.path[(k+1)%self.num_cities]
                    delta_pheromone[i][j] += self.Q/self.distances[i][j]
                    
            for u in range(self.num_cities):
                for v in range(self.num_cities):
                    self.pheromones[u][v] = (1-self.rho)*self.pheromones[u][v] + delta_pheromone[u][v]
                    
    def set_best_index(i):
        self.best_index = i
            