#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Importing the modules
import pandas as pd
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy
pd.options.display.float_format = '{:.2f}'.format


# In[8]:


#reading in the CSV
df = pd.read_csv("movie_metadata.csv")


# In[ ]:





# In[10]:


#limiting the data to be movies released after 2000 only
df_sub = df[ df['title_year'] >= 2000.0 ]
#limiting the data to be movies released in the USA only
df_c = df_sub[df_sub['country'] == 'USA']

df_c['imdb_score'].count()


# In[11]:


#elements = numpy.array(df)
#mean = numpy.mean(elements, axis=0)
#sd = numpy.std(elements, axis=0)

#final_list = [x for x in arr if (x > mean - 3 * sd)]
#final_list = [x for x in final_list if (x < mean + 3 * sd)]
sns.jointplot(x='imdb_score', y='budget', data=df_c)


# In[ ]:





# In[ ]:





# In[14]:


sns.regplot(x='imdb_score', y='budget', data=df_c)
#There is a slight positive correltation between budget and imdb rating


# In[ ]:





# In[177]:


#Showing the mean rating
df_actor = df[ df['actor_1_name'] == 'Denzel Washington' ]
df_actor['imdb_score'].mean()


# In[155]:


df_actor = df[ df['actor_1_name'] == 'Channing Tatum' ]
df_actor['imdb_score'].mean()


# In[175]:


df_actor = df[ df['actor_1_name'] == 'Tom Hanks' ]
df_actor['imdb_score'].mean()


# In[44]:


df_new = pd.read_csv("movies_metadata.csv")
df_new.head()


# In[133]:


#Budget vs. Movie Rating regplot

#making release_date an INT type
df_new1 = df_new.astype({"release_date": int})
#making vote_count an INT type
df_new2 = df_new1.astype({"vote_count": int})
#limiting data to movies released the year 2000 and after
df_new3 = df_new2[ df_new2['release_date'] >= 2000 ]
#limiting data to movies with a budget greater than $0
df_new4 = df_new3[ df_new3['budget'] > 0]
#limiting data to movies with a vote_count greater than 10
df_new5 = df_new4[ df_new4['vote_count'] > 10]

#creating the Budget vs. Movie Rating regplot
sns.regplot(x='vote_average', y='budget', data=df_new5)
#naming the title, x-axis label, and y-axis label
plt.title('Budget vs. Movie Rating')
plt.xlabel('Movie Rating')
plt.ylabel('Budget (in Hundreds of Millions)')


# In[138]:


#Revenue v. Movie Rating regplot

#limiting data to include revenue over $0
df_new6 = df_new5[ df_new5['revenue'] > 0]
#creating the Revenue v. Movie Rating regplot
sns.regplot(x='vote_average', y='revenue', data=df_new6)
#naming the title, x-axis label, and y-axis label
plt.title('Revenue vs. Movie Rating')
plt.xlabel('Movie Rating')
plt.ylabel('Revenue (in Hundreds of Millions)')


# In[125]:


#the mean runtime for below average movies
df_below_avg_rating1 = df_new5[df_new5['vote_average'] <= 6.061279669762635]
df_below_avg_rating1['runtime'].mean()


# In[124]:


#the mean runtime for above average movies
df_above_avg_rating1 = df_new5[df_new5['vote_average'] >= 6.061279669762635]
df_above_avg_rating1['runtime'].mean()


# In[131]:


#Budget and Revenue Linear Regression

#Importing the statsmodels module
import statsmodels.formula.api as smf
#Running a linear regression with budget and revenue
df_t_test = smf.ols(formula = 'budget ~ revenue', data = df_new5).fit()
print(df_t_test.summary())


# In[141]:


#T-Test

from scipy import stats
#running the t-test to see the statistical difference between ratings for 2015 movies and 2016 movies
df_w = df_new5[ df_new5['release_date'] == 2015]['vote_average']
df_m = df_new5[ df_new5['release_date'] == 2016]['vote_average']
stats.ttest_ind(df_w, df_m)   


# In[ ]:




