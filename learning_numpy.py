
import numpy as np
import math 
import matplotlib.pyplot as plt

dataset1=np.array([1,2,3])
dataset2=np.array([1,5,10])
means_arr=np.array(np.mean(dataset1),dataset2.mean())
sem_arr=np.array(np.std(dataset1,ddof=1)/math.sqrt(len(dataset1)),dataset2.std(ddof=1)/math.sqrt(dataset2.size))
plt.bar(x=['dataset1','dataset2'],height=means_arr, yerr=sem_arr,capsize=4)
plt.show()

def PERT(t_lik,t_pes,t_opt,itterations):
    mu=(t_lik*4+t_pes+t_opt)/6
    mu=(mu-t_lik)/(t_pes-t_opt)
    sigma=math.sqrt((t_pes-t_opt)**2/36)
    sigma/=(t_pes-t_opt)
    chi=mu*(1-mu)/sigma**2-1
    alfa=mu*chi
    betta=(1-mu)*chi
    return(np.random.beta(alfa,betta,itterations)*(t_pes-t_opt)+t_opt)

freq_PERT=PERT(15,12.5,30,int(1e6))
print(int(1e6))
plt.hist(freq_PERT,bins=1000)
plt.ylabel('Y')
plt.xlabel('X')
plt.show()
 

print('probability that duration will be <=20: '+str(sum(1 for x in freq_PERT if x<=20)/int(1e6)))