#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 16:27:52 2018

@author: Samuel_Clarin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from plotnine import *
#data for fun

crimes=pd.read_csv("crimes.txt", header=0, sep="\t")
d=ggplot(crimes, aes(x='Population', y='Violent_crime'))
d+geom_point()+geom_smooth(method = "lm")+ggtitle("Crime vs Population")




#making data.txt into hecka graphs


data2 = pd.read_csv('data.txt', header = 0, sep=',' )

North=data2[data2.region.str.contains("north")]
Nobsm=(np.mean(North.observations))
Nreg=(North.region)
South=data2[data2.region.str.contains("south")]
Sobsm=(np.mean(South.observations))
Sreg=(South.region)
East=data2[data2.region.str.contains("east")]
Eobsm=(np.mean(East.observations))
Ereg=(East.region)
West=data2[data2.region.str.contains("west")]
Wobsm=(np.mean(West.observations))
Wreg=(West.region)
means = [Wobsm, Nobsm, Sobsm, Eobsm]
regions = ['West', 'North', 'South', 'East']
data3 = pd.DataFrame({'Mean_Observation' : means, 'Region': regions })
plt.bar(data3.Region, data3.Mean_Observation)
plt.xlabel('region')
plt.ylabel('observations')
plt.title('Bar graph of mean observations by region')

ggplot(data2)+geom_jitter(aes(x="region", y="observations"))+ggtitle("Jittered Data")


#the graphs tell different stories, because the graph of just means makes the observations appera
#similar but when the data is visualized the spread of the data is not equal. The south region especially
#has a different range
