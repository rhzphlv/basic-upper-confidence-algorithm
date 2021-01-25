import pandas as pd
import matplotlib.pyplot as plt
import math 

class UpperConfidenceBound:
    def __init__(self,n_round=None):
        self.n_round=n_round
        self.arm=None
        
    def fit(self,array,*n_round):
        self.arm=len(array.values[0])
        if self.n_round==None:
            self.n_round=len(array)
        ads_selected=[]
        numbers_of_selections=[0]*10
        sums_of_rewards=[0]*10
        total_reward=0  
        for n in range(0,self.n_round):
            ad=0
            max_upper_bound=0
            for i in range(0,self.arm):
                if(numbers_of_selections[i] > 0):
                    average_reward=sums_of_rewards[i]/numbers_of_selections[i]
                    delta_i=math.sqrt(3/2 * math.log(n+1) /numbers_of_selections[i])
                    upper_bound=average_reward+delta_i      
                else:
                    upper_bound=1e400     
                if(upper_bound > max_upper_bound):
                    ad=i
                    max_upper_bound=upper_bound
            ads_selected.append(ad)
            numbers_of_selections[ad]+=1
            reward=data.values[n,ad]
            sums_of_rewards[ad]=sums_of_rewards[ad]+reward
            total_reward+=reward
            self.result=collections.Counter(ads_selected)
            self.fig=ads_selected
            
    def plot(self):
        plt.hist(self.fig)
        return plt.show()
