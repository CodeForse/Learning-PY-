

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math 
#import spicy.stats as st


# data=pd.read_excel('D:/Users/Аслан/Desktop/программирование/PythonDanila/L&L project.xlsx',sheet_name='Лист3', index_col=0)
# #print(data)
# #print(data.to_dict())
# Xarr=np.array(data['Time']) #data.Time or data[0]
# Yarr=np.array(data['Индекс реальных денежных доходов, %'])
# n=len(Xarr)


# Xavr=np.average(Xarr)
# Yavr=Yarr.mean()
# r=np.sum((Xarr-Xavr)*(Yarr-Yavr))/np.sqrt(np.sum((Xarr-Xavr)**2)*np.sum((Yarr-Yavr)**2))
# #t_test=r*math.sqrt((n-2)/(1-r*r))
# #print('r=',round(r,3))

class AnalyzeLinkTwoVars:
   
    def __init__(self,link,sn='Лист1',indexCol=0):
        self.data=pd.read_excel(link,sheet_name=sn, index_col=indexCol)
        

    #@staticmethod
    def getRegressionCoef(self,x,y):
        print(self.data[(y)])

        Yarr=np.array(self.data[y])
        Xarr=np.array(self.data[x])
        Xavr=Xarr.mean()
        Yavr=Yarr.mean()
        r=np.sum((Xarr-Xavr)*(Yarr-Yavr))/np.sqrt(np.sum((Xarr-Xavr)**2)*np.sum((Yarr-Yavr)**2))
        return r
    def StudentTest(self,x,y,SignLevel):
        r=self.getRegressionCoef(x,y)
        t_test=r*math.sqrt((len(x)-2)/(1-r*r))
        return t_test
        #not working well as spicy stat is no available , df=n-1 and a=Sign level
         


model=AnalyzeLinkTwoVars('D:/Users/Аслан/Desktop/программирование/PythonDanila/L&L project.xlsx','Лист3')
print(model.getRegressionCoef('Time','Индекс реальных денежных доходов, %'))        

        
       