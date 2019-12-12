#!/usr/bin/env python
# coding: utf-8

# In[117]:


import os #import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
os.chdir("C:\\Users\\russe\\Downloads") #set directory
df = pd.read_csv("movies_metadata2.csv") #read csv
df_t = df.dropna() #drop na's
df_p = df_t.drop(df_t[df_t.budget < 1].index) #if budget is less than 1, drop
df_s = df_p.drop(df_p[df_p.release < 2000].index)
df_s.budget.plot(kind='hist',color='orange',edgecolor='black',figsize=(10,7), bins = 50) #create histogram
plt.title('budget', size=24) #create title
plt.xlabel('budget', size=18) #create x axis label
plt.ylabel('Frequency', size=18) #create y axis label
scatter = df_s.plot(kind = "scatter", x = "budget", y = "revenue", color = "blue", alpha = .5, figsize = (10,7)) #create scatter
dfr_fit = np.polyfit(dfr.budget,dfr.revenue,1) #create fit with independant and dependant
plt.plot(df.budget,dfr_fit[0]*df.budget+dfr_fit[1], color='darkblue', linewidth=2) #create regression line
plt.text(60,230,'y={:.2f}+{:.2f}*x'.format(dfr_fit[1],dfr_fit[0]),color='black',size=12) #find regression equation
def predictor(r):
    y = 11078796.18 + 4.03 * r
    print(y, "is the expected revenue of a movie with a budget of", r) #function allows users to input budget
predictor(50000) #print result


    


# In[ ]:




