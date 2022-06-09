

from operator import le
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math 
import scipy.stats as st #from spicy import stats as st



class AnalyzeLinkTwoVars:
   
    def __init__(self,link,sn='Лист1',indexCol=0):
        self.data=pd.read_excel(link,sheet_name=sn, index_col=indexCol)
        

    #@staticmethod
    def getRegressionCoef(self,x,y):

        Yarr=np.array(self.data[y])
        Xarr=np.array(self.data[x])
        Xavr=Xarr.mean()
        Yavr=Yarr.mean()
        r=np.sum((Xarr-Xavr)*(Yarr-Yavr))/np.sqrt(np.sum((Xarr-Xavr)**2)*np.sum((Yarr-Yavr)**2))
        return r
    def StudentTest(self,x,y,SignLevel):
        #H0: in the model Y=bX+a, b=0
        #H1=HA: b!=0
        r=self.getRegressionCoef(x,y)
        t_test=r*math.sqrt((len(x)-2)/(1-r*r))
        t_crit=st.t.ppf(q=SignLevel,df=len(x)-2)
        return t_test<t_crit #0->accepth null, 1-> reject null
        #(solved)not working well as spicy stat is no available , df=n-2 and a=Sign level: damn it was scipy

         

path=''
model=AnalyzeLinkTwoVars(path,'Лист3')
print(model.getRegressionCoef('Time','Индекс реальных денежных доходов, %'))  
SL=0.05      
print('Thy hypothesis that Time does not affects Index of the real income is '+str(model.StudentTest('Time','Индекс реальных денежных доходов, %',SL))+' at '+str(SL)+'SL')
        
       