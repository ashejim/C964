#!/usr/bin/env python
# coding: utf-8

# (sup_class_ex:develop)=
# ## <a id='toc1_1_'></a>[Model Development](#toc0_)
# 
# Supervised algorithms use inputs (independent variables) and labeled outputs (dependent variable -the "answers") to create a model that can measure its performance and learn over time. Splitting the data into independent and dependent variables, we have the following:

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

X = df.drop(columns=['type']) #indpendent variables
y = df[['type']].copy() #dependent variables


# ```{note}
# The focus of [Task 2 part D *Data Product*] (task2d:dataproduct) will be the what, how, and why of your model's development.
# ```

# (sup_class_ex:develop:train)=
# ### <a id='toc1_1_1_'></a>[Train Model(s)](#toc0_)
# 
# ```{margin}
# A model can learn the details and noise particular to the training data so well that it doesn't perform well on new data. This is called [*overfitting*](https://en.wikipedia.org/wiki/Overfitting). Overcomplicated non-linear and nonparametric models are more susceptible to this. The term *overtraining* can be used synonymously or to mean too much training as a cause of overfitting. 
# ```
# 
# Studying for a test when you have all the answers beforehand will likely yield a good grade. But how well would that grade measure understanding of material outside those answers? Similarly, supervised methods tend to perform well when tested on their training data, but you want your model to perform well on *unseen* data. So while it's not required, separating data used to train and test the model (validation) is good practice. Furthermore, it provides content for part D. 
# 
# Fortunately, most libraries have built-in functions for this. Here we'll stick with [scikit-learn aka sklearn](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html). Validation processes We'll need to randomly split the data into independent (input values) and dependent (output, i.e., the answers) variables. For now, we'll keep things as DataFrames, but later convert them to 2-d arrays

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


# Read the [docs](sklearn_link)! By default *train_test_split*, "randomly" splits the sets. Setting the seed (or state) controls the experiments. See [should you use a random seed?](https://datascience.stackexchange.com/questions/78109/should-you-use-random-state-or-random-seed-in-machine-learning-models).
# 
# We can now train a model using the independent (usually denoted 'X') and dependent variables (usually denoted 'y') from the training data. Sklearn has a deep [supervised learning library](https://scikit-learn.org/stable/supervised_learning.html). Note that many of these models (including SVM) have both classification and regression extensions. 

# In[4]:


from sklearn import svm

svm_model = svm.SVC(gamma='scale', C=1) #Creates a svm model object. Mote, 'scale' and 1.0 are gamma and C's respective defaults 
svm_model.fit(X_train,y_train)


# What went wrong? The sklearn '.fit' function expected the 'y' data as a 1d array, but I gave it a DataFrame. Let's fix that. 
# 
# ```{margin}
# [What's that 'gamma' and 'C' for?](https://scikit-learn.org/stable/auto_examples/svm/plot_rbf_parameters.html), read the docs!
# ```

# In[5]:


y_train_array, y_test_array = y_train['type'].values, y_test['type'].values
y_train_array

X_train_array, X_test_array = X_train.values, X_test.values
X_train_array

svm_model.fit(X_train_array,y_train_array) 
#Note: You can use X_train (dataframe) or X_train_array (2d array to fit the model.


# Now we've trained the model! What does that mean? Sklearn's SVM algorithm creates an equation representing the relationship between the independent variables. 
# 
# $$F_{\text{predict}}(X)=\text{prediction(s)}$$
# 
# Here's the code:

# In[6]:


predictions = svm_model.predict(X_train_array)
np.set_printoptions(threshold=15) #truncates the print output
print(predictions)
#Note: using 'X_train' here, a dataframe, causes the following warning: 
#'UserWarning: X has feature names, but SVC was fitted without feature names...'


# How good are these predictions? Answering that question is our next step. 
