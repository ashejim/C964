#!/usr/bin/env python
# coding: utf-8

# (sup_reg_ex: develop)=
# ## Data product Model Development (part 1)
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


# (sup_reg_ex: develop: train)=
# ### Train Model
# 
# Recall, splitting the data into training and testing sets is not required, but it is good practice. Furthermore, it provides content for part D. 
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


# 
# Review sklearn's nice [supervised learning library](https://scikit-learn.org/stable/supervised_learning.html). Note that many of these models have both classification and regression extensions.

# In[4]:


from sklearn.linear_model import LinearRegression 


# Our data is mostly quantitative and the scatterplots do indicate the variables may be linearly related. So linear regression isn't a bad place to start. Once we've trained and tested a linear regression model, we'll easily be able to experiment with different algorithms. 
# 
# ```{margin}Is linear regression ML?
# It depends who you ask. Google "Is linear regression machine learning?" and you'll see some interesting (and enterntaining) discussion. For the purposes of the capstone, the answer is -yes.  
# ```

# In[5]:


linear_reg_model = LinearRegression()
linear_reg_model.fit(X_train,y_train)


# *Wait what happened!?!* This error returns a lot of output, but one line makes things clear:
# 
# > ValueError: could not convert string to float: 'Iris-virginica' 
# 
# The algorithm expected numbers; it does not know what to do with the flower types (strings). So how do we fix this?
# 
# (sup_reg_ex: develop: train: categorical_1)=
# #### Processing Categorical Data -option 1
# 
# One way to fix a problem is to avoid it. You are not required to use all the data -only some of it. Sometimes choosing the right variables is the real trick. [Dimensionality reduction](https://en.wikipedia.org/wiki/Dimensionality_reduction) is an important part of the data sciences. Here, those flower types DO matter, and it would be best to include that data -but goal #1 is to get things working. Improving things is step #2 and step #3 and step #4 and ... step $\# \infty$.
# 
# So let's remove the column with categorical data:

# In[ ]:


#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.333, random_state=41)
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html

X_train_no_type = X_train.drop(columns = ['type'])
X_test_no_type =  X_test.drop(columns = ['type'])

display(X_test_no_type)


# Now the models will train fine:

# In[ ]:


linear_reg_model.fit(X_train_no_type, y_train)


# And the model can make predictions for an entire set:

# In[ ]:


y_pred_no_type = linear_reg_model.predict(X_test_no_type)
y_pred_no_type


# Or a single input:

# In[ ]:


# The model was trained with a dataframe, so you can only predict on dataframes
# Recall we removed the petal type, and we are predicting the sepal-length
column_names_short = ['sepal-width', 'petal-length', 'petal-width']
input_df = pd.DataFrame(np.array([[3.2, 1.3, .2]]), columns = column_names_short)

print(linear_reg_model.predict(input_df))


# ```{note}
# Your model can only predict on data simliar to what it was trained with. Since this model was trained with a dataframe, a matching new dataframe, 'input_df' needed to be created to predict a single input. Alternatively, we could have converted the original data to an array (see the [previous example](sup_class_ex:develop:train).                       
# ```

# (sup_reg_ex: develop: accuracy)=
# ### Accuracy Analysis
# 
# As we are trying to predict a continuous number, even the very best model will have errors in almost every prediction. So we need a way to measure how much those predictions deviate from actual values. See sklearn's list of [metrics and scoring](https://scikit-learn.org/stable/modules/model_evaluation.html) for regression. Which metric is best depends on the needs of your project. However, any accuracy metric appropriate to your model will be accepted. 
# 
# (sup_reg_ex: develop: accuracy: MSE)=
# ##### Mean Squared Error
# 
# The mean square error (MSE) measures the average of the squares of errors (difference between predicted and actual values). See details in the next section [below](sup_reg_ex: develop: accuracy: MSE_example). Applying the MSE to the *test* data, we have:

# In[ ]:


from sklearn.metrics import mean_squared_error

mean_squared_error(y_test, y_pred_no_type)


# (sup_reg_ex: develop: accuracy: MSE_example)=
# ###### MSE explanation and example in 2D 
# Using just the *petal-length* to predict the *sepal-length* with linear regression on 15 random values, the regression line looks like this: 

# In[ ]:


import matplotlib.pyplot as plt

x = X_train[['petal-length']]
x = x[-15:]
y = y_train[-15:]

# Create linear regression object
regr_ex = LinearRegression()
# Train the model using the training sets
regr_ex.fit(x, y)
y_pred_ex = regr_ex.predict(x)

fig, ax = plt.subplots()

plt.scatter(x, y, color="black")
plt.scatter(x, y_pred_ex, color="blue")
plt.plot(x, y_pred_ex, color="blue", linewidth=3);
plt.figtext(0.5, 0.01, "Black dots = actual values; blue dots = predicted value", wrap=True, horizontalalignment='center', fontsize=8);


# The error squared looks like:

# In[ ]:


from matplotlib.patches import Rectangle

fig, ax = plt.subplots()

i = 0
while i < len(x):
    a = float(x.values[i])
    b = float(y.values[i])
    c = float(y_pred_ex[i])
    error = float(y_pred_ex[i])-float(y.values[i])
    ax.add_patch(Rectangle((a, b), 
                           error, 
                           error,
                           fc=(1,0,0,0.5), ec=(0,0,0,1), lw=1)
                 )
    i = i+1

plt.scatter(x, y, color="black")
plt.scatter(x, y_pred_ex, color="blue")
plt.plot(x, y_pred_ex, color="blue", linewidth=3);
plt.figtext(0.5, 0.01, "Black dots = actual values; blue dots = predicted value", wrap=True, horizontalalignment='center', fontsize=8);


# The MSE just takes the average of these squares. The math:
# 
# $$\text{MSE} = \frac{1}{n} \sum^{n}_{i=1} (Y_i - \hat{Y}_i)^{2}$$
# 
# Where $Y_i$ and $\bar{Y}_i$ are the $i^{\text{th}}$ actual and predicted values respectively.

# In addition to giving positive values, squaring in the MSE emphasizes larger differences. Which can be good or bad depending on your needs. If your data has many or very large outliers, consider removing outliers or using the [mean absolute error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html#sklearn.metrics.mean_absolute_error). See the [sklearn MSE docs](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error) for more info and examples. 
# 
# Increasing the number of variables uses the same concept only the regression line becomes multi-dimensional. For example, additionally, including 'sepal-length' and 'petal-length' creates a *4-dimensional* line. So it's a little hard to visualize. Using the squares of the errors is standard but ME is sometimes easier for non-technical audiences to understand. 
# 
# (sup_reg_ex: develop: accuracy: R)=
# ##### $R^{2}$ the coefficient of determinaiton
# 
# ```{Margin} $R^{2}$, $r^{2}$, $R$, and $r$:
# $R^{2}$ is *not* necessarily $r^{2}$. For simple linear regression, [$R^{2}=r^{2}$](https://stats.stackexchange.com/questions/99669/the-equivalence-of-sample-correlation-and-r-statistic-for-simple-linear-regressi), but when the model lacks an intercept [things get more complicated](https://stats.stackexchange.com/questions/134167/is-there-any-difference-between-r2-and-r2#:~:text=In%20the%20case%20of%20simple%20linear%20regression%20specifically%2C,this%20means%20that%20R%20%3D%20%7C%20r%20%7C.), and unfortunately there are some inconsistencies in the notation. 
# 
# - $r$: the *(sample) correlation coefficient* measuring the statistical relationship between two variables, e.g., $X$ and $Y$; sometimes denoted $R$. There are different types (usually [Pearson](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient) when not specified) all having values in $[-1,1]$, with $\pm 1$ indicating the strongest possible negative/positive relationship and $0$ no relationship. Confusingly (maybe sloppily), sometimes $r$ denotes the non-multiple correlation between $Y$ and $\hat{Y}$ (values fitted by the model), in which case $r\geq 0$. 
# 
# - $R$: the *coefficient of multiple correlation* or *correlation coefficient* measuring the Pearson correlation between observed, $Y$, and predicted values, $\hat{Y}$. $R=\sqrt{R^{2}}$ and $R\geq 0$ (assuming the model has an intercept) with higher values indicating better predictability of a linear model.
# 
# - $R^{2}$: the *coefficient of determination* measures the proportion of the variation in the dependent variable  predictable (by the linear model) from the independent variable(s). The most general definition is: $R^{2}= 1 -\frac{SS_{\text{res}}}{SS_{\text{tot}}}$ where $SS_{\text{res}}=\sum_{i}(y_i-\hat{y}_i)^2$ (the [residual sum of squares](https://en.wikipedia.org/wiki/Residual_sum_of_squares)) and $SS_{\text{tot}}=\sum_{i}(y_i-\bar{y})^2$ (the [total sum of squares](https://en.wikipedia.org/wiki/Total_sum_of_squares)). The former sums squared differences of actual and model output, and the latter sums squared differences of actual outputs and the mean. When $SS_{\text{tot}}<SS_{\text{res}}$, i.e., the mean is a better predictor than the linear model, it's possible for $R^{2}$ to be negative.  
#   
# ```
# 
# $R^{2}$, the *coefficient of determination*, measures the proportion of the variation in the dependent variable that is predictable by the linear model from the independent variable(s). While the [mean squared error](https://en.wikipedia.org/wiki/Mean_squared_error) and similar metrics, e.g., [MAE](https://en.wikipedia.org/wiki/Mean_absolute_error), [MAPE](https://en.wikipedia.org/wiki/Mean_absolute_percentage_error), and [RMSE](https://en.wikipedia.org/wiki/Root-mean-square_deviation) have arbitrary ranges; $R^{2} can (usually) be expressed as more intuitive to understand percentage. 
# 
# ```{note}
# While it can be computed, $R^{2}$ is not defined for non-linear models and hence not a good metric for comparing linear models to other regression models [nor for measuring goodness of fit in general](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2892436/).  
# ```

# In[ ]:


from sklearn.metrics import r2_score

r2_score(y_test, y_pred_no_type)


# $77\%$. Is that good? Here, as with most ML models, our goal is predicting the dependent variable. As opposed to explaining the relationship between the independent and dependent variable; a statistical question for which $R^{2}$ is mostly irrelevant. For demonstrating how well our model predicts, the closer to $1$ the better. But what's close enough? That depends on how precise you need to be. Some fields demand a standard as high as $95\%$. However, as a percentage of the dependent variable variation explained by the independent variables, `0.7741` is a big chunk. Here's a rough, totally unofficial guideline:
# 
# | **$R^{2}$** | Interpetaion |
# | -------- | ------- |
# | $\geq 0.75$  | Significant variance explained! |
# | $(0.75, .5]$ | Good amount explained. |
# | $(0.5, .25]$ | Meh, some explained. |
# | $(0.25, 0)$ | It's still better than nothing! |
# | $\leq 0$ | You'd be better off using the mean. |
# 
# Conveniently, I've defined my model's performance as a great success 😃.
# 
# ##### Margin of error
# 
# The best way to measure your model's success depends on what you're trying to do. Say my flower customers want to predict `sepal-length` (I have no idea why), but any prediction within `0.5` of an inch would be acceptable. That is a "good" prediction, would be any falling with the dashed lines:

# In[266]:


# import numpy as np
# import matplotlib.pyplot as plt

# linear_reg_model.fit(X_train_no_type, y_train)

reg_model = linear_reg_model.fit(X_train_no_type, y_train)

def findLinearRegressionLine(model_name):
    c = model_name.coef_
    b = model_name.intercept_
    x1 = X_test_no_type.values[2]
    y1 = reg_model.predict([x1])
    
    x2 = X_test_no_type.values[15]
    y2 = reg_model.predict([x2])
    
    
    x1 =(x1*c)[0][0]+(x1*c)[0][1]+(x1*c)[0][2]
    x2 =(x2*c)[0][0]+(x2*c)[0][1]+(x2*c)[0][2]
    
    m = (y2-y1)/(x2-x1)
    
    # y2 = 
    # m = 
    
    # y1, y2 =     
    print(m)
    # print(y2)
    # print(x2)
    # print(b)
    # print(c)

findLinearRegressionLine(reg_model)

# fig, ax = plt.subplots()

y = y_pred_no_type

plt.scatter(X_test_no_type, y, color="black");
# plt.scatter(x, y_pred_ex, color="blue");
plt.plot(x, y_pred_ex, color="blue", linewidth=3);

# # upper and lower margin of error of regression model
# y1 = y_pred_ex - .5
# y2 = y_pred_ex + .5

# # plt.plot(x, y_pred_ex+.5, color="gray", linestyle='dashed');
# # plt.plot(x, y_pred_ex-.5, color="gray", linestyle='dashed');
# # plt.figtext(0.5, 0.01, "Black dots = actual values; blue dots = predicted value", wrap=True, horizontalalignment='center', fontsize=8);

# # plt.xlabel(r'$x values$')
# # plt.ylabel(r'$y values$')


# x = np.array(X_train[['petal-length']]).ravel()
# plt.fill_between(x, 2*x+1, 2*x-1, color='grey', alpha=0.25);
# plt.legend(loc='center left')


# In[ ]:


x = np.arange(0,10,0.1)

# The lines to plot
y1 = 4 - 2*x
y2 = 3 - 0.5*x
y3 = 1 -x

# The upper edge of polygon (min of lines y1 & y2)
y4 = np.minimum(y1, y2)

# Set y-limit, making neg y-values not show in plot
# plt.ylim(0, 5)

# Plotting of lines
plt.plot(x, y1, label = 'y1')
plt.plot(x, y2, label = 'y2')
plt.plot(x, y3, label = 'y3')
plt.plot(x, y4, label = 'y4')

# Filling between line y3 and line y4
plt.fill_between(x, y3, y4, color='grey', alpha=0.25);
plt.legend(loc='center left')
print(x)


# ## TRAIN OTHER MODELS

# ## TEST OTHER MODELS
