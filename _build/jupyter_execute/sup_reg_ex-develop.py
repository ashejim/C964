#!/usr/bin/env python
# coding: utf-8

# (sup_reg_ex:develop)=
# ## Data product Model Development
# 
# Supervised algorithms use inputs (independent variables) and labeled outputs (dependent variable -the "answers") to create a model that can measure its performance and learn over time. Splitting the data into independent and dependent variables, we have the following (again, this will be very similar to the [previous example](sup_class_ex:develop)):

# In[1]:


#Note: we only repeat this step from before, because this is a new .ipyb page.
#   it only needs to be executed once per file.

#We'll import libraries as needed, but when submitting, having them all at the top is best practice
import pandas as pd

# Reloading the dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
df = pd.read_csv(url) #read CSV into Python as a dataframe

column_names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'type']
df = pd.read_csv(url, names = column_names) #read CSV into Python as a dataframe

#Choosing the variables. 
X = df.drop(columns=['sepal-length']) #indpendent variables
y = df[['sepal-length']].copy() #dependent variables


# Supervised methods tend to perform well (or too well) when tested on their training data, but you want your model to perform well on *unseen* data. So while it's not required, separating data used to train and test the model (validation) is good practice. Furthermore, it provides content for part D. 
# 
# As with the previous example [previous example](sup_class_ex:develop)), we'll use [scikit-learn aka sklearn](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html) built-ins for this.

# In[2]:


import numpy as np
from sklearn.model_selection import train_test_split

#split the variable sets into training and testing subsets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.333, random_state=41)


# In[3]:


#Nice displays are nice but not required. 
from IPython.display import display_html 
X_train_styler = X_train.head(5).style.set_table_attributes("style='display:inline'").set_caption('Independents variables')
y_train_styler = y_train.head(5).style.set_table_attributes("style='display:inline'").set_caption('Dependents variables')
space = "\xa0" * 10 #space between columns
display_html(X_train_styler._repr_html_()+ space  + y_train_styler._repr_html_(), raw=True)


# we'll stick with sklearn has a deep [supervised learning library](https://scikit-learn.org/stable/supervised_learning.html). Note that many of these models have both classification and regression extensions. 
