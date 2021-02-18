from Ant import Ant

class AntColony:
    def __init__(self, alpha, beta, rho, Q, city_distances, max_iter, num_ants, sigma, init_pheromone=0.1):
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.Q = Q
        self.city_distances = city_distances
        self.max_iter = max_iter
        self.num_ants = num_ants
        self.sigma = sigma
        
        self.num_cities = len(city_distances)
        self.pheromones = [[init_pheromone for i in range(self.num_cities)] for j in range(self.num_cities)]
        self.best_cost = float('inf')
        self.best_tour = None
        self.best_index = None
        self.tours = []
        self.omega = int(0.1*self.num_cities)
        
    def optimisation(self):
        for i in range(self.max_iter):
            ants = [Ant(self.num_cities) for j in range(self.num_ants)]
            
            tour_costs = [ant.construct_tour(self.pheromones, self.city_distances,
                          self.alpha, self.beta) for ant in ants]
                          
            sorted_tour_costs = sorted(range(len(tour_costs)), key=tour_costs.__getitem__)
                          
            [self.set_best_index(i) for i in range(len(tour_costs)) if tour_costs[i] < self.best_cost]
            
            if self.best_index:
                self.best_cost = tour_costs[self.best_index]
                self.best_tour = ants[self.best_index].path
                self.tours.append(tour_costs[self.best_index])
                
            self.set_best_index(None)
            
            delta_pheromone = [[0 for i in range(self.num_cities)] for j in range(self.num_cities)]
            for index in range(self.omega):
                ant = ants[sorted_tour_costs[index]]
                for k, i in enumerate(ant.path):
                    j = ant.path[(k+1)%self.num_cities]
                    delta_pheromone[i][j] += (self.sigma - index)*self.Q/tour_costs[sorted_tour_costs[index]]
            
            # delta_pheromone = [[0 for i in range(self.num_cities)] for j in range(self.num_cities)]
            # for index, ant in enumerate(ants):
                # for k, i in enumerate(ant.path):
                    # j = ant.path[(k+1)%self.num_cities]
                    # delta_pheromone[i][j] += self.Q/tour_costs[index]
                    
            elitist_pheromone = [[0 for i in range(self.num_cities)] for j in range(self.num_cities)]
            for k, i in enumerate(self.best_tour):
                j = ant.path[(k+1)%self.num_cities]
                elitist_pheromone[i][j] = self.sigma*self.Q/self.best_cost
                    
            for u in range(self.num_cities):
                for v in range(self.num_cities):
                    self.pheromones[u][v] = ((1-self.rho)*self.pheromones[u][v] + 
                                            delta_pheromone[u][v] + elitist_pheromone[u][v])
                    
    def set_best_index(self, i):
        self.best_index = i
            