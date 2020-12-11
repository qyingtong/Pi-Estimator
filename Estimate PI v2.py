#%% Import Cellpi
import random
import numpy as np
import matplotlib.pyplot as plt

#%% Esimate pi sim class
class estimate_pi:
    
    def __init__(self, num_points=10): 
        self.num_points = num_points
            
    def sim_est(self):
        circle_points = 0
        
        for __ in range(self.num_points):
            x = random.uniform(0,1)
            y = random.uniform(0,1)
            if (x**2 + y**2) <=1:
                circle_points += 1
            
        sim_est_pi = 4 * (circle_points/self.num_points)
                
        self.sim_est_pi = sim_est_pi
        
        return sim_est_pi
    
    def sim_results(self):
        sim_pi_list = []
        
        for __ in range(10):
            sim_pi_list.append(self.sim_est())
        
        ave_sim_pi = np.mean(sim_pi_list)
        sim_var = np.var(sim_pi_list)
        
        self.sim_pi_list = sim_pi_list
        self.ave_sim_pi = ave_sim_pi
        self.sim_var = sim_var
    
        print("Num Points: " + str(self.num_points) + "\n"
          "Average Estimated Pi: " + str(self.ave_sim_pi) + "\n"
          "Variance: " + str(self.sim_var) + "\n")
    
    def goalseek(self, error_tolerance = 0.00001):
        sim_pi_nested_list = []
        num_points_list = []
        
        while self.num_points < 10000000:
            num_points_list.append(str(self.num_points))
            sim_pi_nested_list.append(self.sim_pi_list)
            if self.sim_var > error_tolerance:
                self.num_points = self.num_points*10
                self.sim_est()
                self.sim_results()
            else:
                break
            
        print("End")
        
        self.sim_pi_nested_list = sim_pi_nested_list
        self.num_points_list = num_points_list
    
    def goalseek_boxplot(self):
        plt.boxplot(self.sim_pi_nested_list)
        plt.xlabel("Num of Points Randomly Generated")
        plt.ylabel("Estimated Pi Value")
        plt.xticks(range(1,len(self.num_points_list)+1), self.num_points_list)
        plt.show
            
#%% Testing
get_pi = estimate_pi()
get_pi.sim_results()
get_pi.goalseek()
get_pi.goalseek_boxplot()
