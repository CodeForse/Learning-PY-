import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math 
#import spicy.stats as st


data=pd.read_excel('D:/Users/Аслан/Desktop/программирование/PythonDanila/L&L project.xlsx',sheet_name='Лист3', index_col=0)
#print(data)
#print(data.to_dict())
Xarr=np.array(data['Time']) #data.Time or data[0]
Yarr=np.array(data['Индекс реальных денежных доходов, %'])
n=len(Xarr)


Xavr=np.average(Xarr)
Yavr=Yarr.mean()
r=np.sum((Xarr-Xavr)*(Yarr-Yavr))/np.sqrt(np.sum((Xarr-Xavr)**2)*np.sum((Yarr-Yavr)**2))
#t_test=r*math.sqrt((n-2)/(1-r*r))
#print('r=',round(r,3))

class AnalyzeLinkTwoVars:
    r=0 #reg coef
    n=0 #sample size
    X=0 #explanatory var
    Y=0 #dependent var
    def __init__(self,link,y,x):
        data=pd.read_excel(link)
        self.X=data[y]
        self.Y=data[x]
        self.n=len(data[x])

    @staticmethod
    def getRegressionCoef(Yarr,Xarr):
        Xavr=np.average(Xarr)
        Yavr=Yarr.mean()
        r=np.sum((Xarr-Xavr)*(Yarr-Yavr))/np.sqrt(np.sum((Xarr-Xavr)**2)*np.sum((Yarr-Yavr)**2))
        return r

model=AnalyzeLinkTwoVars('D:/Users/Аслан/Desktop/программирование/PythonDanila/L&L project.xlsx','Time','Индекс реальных денежных доходов, %')
print(model.getRegressionCoef('Time','Индекс реальных денежных доходов, %'))        

        
       