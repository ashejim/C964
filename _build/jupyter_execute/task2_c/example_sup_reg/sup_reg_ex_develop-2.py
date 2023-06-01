#!/usr/bin/env python
# coding: utf-8

# (sup_reg_ex: develop-2)=
# ## Data product Model Development (part 2)

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

#Choosing sepal-length as the independent variable. 
X = df.drop(columns=['sepal-length']) #indpendent variables
y = df[['sepal-length']].copy() #dependent variables


# In [LINK GOES HERE] the previous section, we avoided using categorical data removing and ignoring it. While this sped things along, it also dropped potentially valuable insight from our analysis. Now that the code is working, we'll rebuild our models using that categorical data, the 'type' feature.

# In[2]:


df_sample = df.sample(n=10, random_state = 152)
# df_sample_highlight = pd.concat([df_sample.iloc[:5,:], df_sample.iloc[-5:,:]]).style.format().set_properties(subset=['type'], **{'background-color': 'yellow'})

# function definition
def highlight_cols(s):
    color = 'null'
    if s == 'Iris-virginica': color = 'limegreen'
    elif s == 'Iris-setosa': color = 'lightblue'
    elif s == 'Iris-versicolor': color = 'orange'
    # color = 'red' if s == 'Iris-virginica' or 'blue' if s == 'Iris-setosa'
    return 'background-color: % s' % color
  
# highlighting the cells
df_sample.style.applymap(highlight_cols)


# We have three unique flower types, equally distributed, in this feature:

# In[3]:


df.groupby('type').size().plot(kind='pie',colors = ['lightblue', 'orange', 'limegreen']);


# Recall, a coding error [LINK HERE] was returned because the algorithm could not process categorical independent variables. Most machine learning models can only interpret numerical data. Thus *feature encoding*, processing data into numerical form, is an essential data analytical skill. To do this properly you should understand your data before preceding. For example, we could simply re-label the types as follows:
# 
# $$ 
#   \text{Iris-setosa} \rightarrow 1 \\
#   \text{Iris-versicolor} \rightarrow 2 \\
#   \text{Iris-virginica} \rightarrow 3
# $$   
# 
# and hand this off to the algorithm. But while this would fix the coding error, any mathematical interpretation of this re-labeling would be meaningless, e.g., 'Iris-setosa' is not twice as much as 'Iris-versicolor,' nor does 'setosa' + 'versicolor' = 'virginica' -the type is just a name. We call this type of categorical data *nominal.* Categories with an inherent order, e.g., grades, pay grades, bronze-silver-gold, etc., are called *ordinal.* But that doesn't apply here either. A flower either is an 'Iris-setosa' OR it isn't. Each type is similarly binary so we can interpret *each unique type as a unique mutually exclusive feature*, with a 1 or 0, indicating whether the category applies or not, respectively. 
# 
# Most machine learning libraries are well equipped with built-in preprocessing functions; see the available options in the docs: [sklearn.preprocessing](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.preprocessing). For simplicity, we'll start with Pandas' built-in [get_dummies](https://pandas.pydata.org/docs/reference/api/pandas.get_dummies.html). However, it will often be best to use functions written for your model's library, such as sklearn's [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder). 

# In[4]:


after_pd_dummy = pd.get_dummies(df_sample)


# In[5]:


#highlight values according to column names and values. 
def highlight_cols_dummy(col):
    if col.name == 'type_Iris-setosa':
        return ['background-color: lightblue' if c == 1 else '' for c in col.values]
    elif col.name == 'type_Iris-versicolor':
        return ['background-color: orange' if c == 1 else '' for c in col.values]
    elif col.name == 'type_Iris-virginica':
        return ['background-color: lightgreen' if c == 1 else '' for c in col.values]
    else:
        return ['background-color: null' for c in col.values]

# #Nice displays are nice but not required. 
from IPython.display import display_html 
before_styler = df_sample.style.set_table_attributes("style='display:inline'").set_caption('Before <em>get_dummy</em>').applymap(highlight_cols).format(precision = 1)
after_styler = after_pd_dummy.style.set_table_attributes("style='display:inline'").set_caption('After <em>get_dummy</em>').apply(highlight_cols_dummy).format(precision = 1)
# space = "\xa0" * 10 #space between columns
arrow = "<html> <huge>&#x21e8;</huge> </html>"

# displays dataframes side by side
display_html(before_styler._repr_html_() + arrow + after_styler._repr_html_(), raw=True)


# In[6]:


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_squared_error

# X = df.drop(columns=['sepal-length']) #indpendent variables
# y = df[['sepal-length']].copy() #dependent variables

X = pd.get_dummies(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.333, random_state=41)
linear_reg_model_types = LinearRegression()
linear_reg_model_types.fit(X_train,y_train)
y_pred = linear_reg_model_types.predict(X_test)

sme = mean_squared_error(y_test, y_pred)
print('squared mean error using types is :' + str(sme))


# Without including the flower types, our linear model has a squared mean error of `X.XXXXX.` Wait what? It go worse, but why? Adding three `types` of features, added three dimensions. Moving from three to a *six-*dimensional space. Consider the change from just two to three dimensions, e.g.,$2^{2}$ to $2^{3}=8$. Adding dimensions can radically increase the volume of space making the available data relatively sparse -what's known as the [Curse of Dimensionality](https://en.wikipedia.org/wiki/Curse_of_dimensionality). -However, that's not the full story here. While, both `petal-length` and `petal-width` appear positively correlated with `sepal-length`for `versicolor` and `virginica` it does *not* for `setosa` (blue below), 

# In[7]:


import matplotlib.pyplot as plt
import seaborn as sns

#correlogram
sns.pairplot(df,x_vars = ['petal-length','petal-width'], y_vars=['sepal-length'], hue='type')
plt.show()


# The drop in accuracy is in part a limitation of our simple linear model trying to make use of a feature pulling the model in the wrong direction. Making the most out of your data involves a mix of understanding the data and the applied algorithm(s) (which don't understand anything). Using three different linear models yields better results:

# In[8]:


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_squared_error


df_dummy = pd.get_dummies(df)
df_dummy
df_s = df_dummy.loc[df_dummy['type_Iris-setosa'] == 1].drop(columns=['type_Iris-versicolor', 'type_Iris-virginica'])
df_v = df_dummy.loc[df_dummy['type_Iris-versicolor'] == 1].drop(columns=['type_Iris-setosa', 'type_Iris-virginica'])
df_g = df_dummy.loc[df_dummy['type_Iris-virginica'] == 1].drop(columns=['type_Iris-setosa', 'type_Iris-versicolor'])

def line_regression_pipe(df_list):
    for df in df_list:
        X = df.drop(columns=['sepal-length']) #indpendent variables
        y = df[['sepal-length']].copy() #dependent variables
        #split the variable sets into training and testing subsets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.333, random_state=41)
        linear_reg_model_a = LinearRegression()
        linear_reg_model_a.fit(X_train,y_train)
        y_pred = linear_reg_model_a.predict(X_test)
        sme = mean_squared_error(y_test, y_pred)
        print('sme of ' + df.columns[4] + ' is :' + str(sme) )

df_list = [df_s, df_v, df_g]
line_regression_pipe(df_list)


# In[9]:


from lineartree import LinearTreeRegressor, LinearForestRegressor, LinearBoostRegressor
# regr = LinearTreeRegressor(base_estimator=LinearRegression())
# regr = LinearForestRegressor(base_estimator=LinearRegression())
# regr = LinearBoostRegressor(base_estimator=LinearRegression())

regr.fit(X_train, y_train)
y_predict = regr.predict(X_test)
sme = mean_squared_error(y_test, y_predict)
print(str(sme))


# In[106]:


from sklearn.linear_model import SGDRegressor

sgd_reg = SGDRegressor(max_iter = 10000000, tol=1e-20)
sgd_reg.fit(X_train, y_train)
y_predict = sgd_reg.predict(X_test)
sme = mean_squared_error(y_test, y_predict)
print(str(sme))


# What've done is combine the  

# In[70]:


from sklearn.tree import DecisionTreeRegressor

tree_regressor = DecisionTreeRegressor(random_state=41)
tree_regressor.fit(X_train, y_train)

y_predict = tree_regressor.predict(X_test)
sme = mean_squared_error(y_test, y_predict)
print(str(sme))

# from sklearn.linear_model import LinearRegression
# from lineartree import LinearTreeRegressor

from sklearn.tree import export_graphviz 

export_graphviz(tree_regressor, out_file ='tree.dot')
import graphviz

# dot -Tps tree.dot -o outfile.pdf
from IPython.display import display
with open("tree.dot") as f:
    dot_graph = f.read()
display(graphviz.Source(dot_graph))


# In[39]:


# from sklearn.preprocessing import OneHotEncoder

#Instantiate OneHotEncoder (ohe). 
#Note Pandas get_dummies can also perform this function, but ohe has some ML application advantages.

ohe = OneHotEncoder(sparse = False) 

