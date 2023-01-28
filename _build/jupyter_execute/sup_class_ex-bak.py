#!/usr/bin/env python
# coding: utf-8

# # Example: Supervised Classification App
# 
# This will be a very simple example. Simple data. Simple model. Simple interface. However, it does demonstartes the minimum requirements for [part C](task2c). We'll also demonstrate how things can progressively be improved in a [part 2], always building on working code. Simple is a great place to start -scaling up is typically easier than going the other direction.
# 
# Supervised classification fits the project requirments well, and is also a good place to start. The nature of your Data and organizational need dictate which methods you can use. So what type of data do we need? 
# [](TODO ADD LINK)
# 
# - One of those features is the category you want to predict (the dependent variable).
# - At least one other features (the independent variable(s)).
# 
# ## Data Processing
# 
# Let's look at some data.

# In[1]:


#We'll import libraires as needed, but when submitting, having them all at the top is best practice
import pandas as pd
# Load this well worn dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
df = pd.read_csv(url) #read CSV into Python as a dataframe
df # displays the dataframe


# Opps. We've got the first row being used as headers. Some data sets have headers already -this one doesn't. How do I do that? Google ["how to python add headers to dataframe"](https://www.google.com/search?q=how+to+python+add+headers+to+dataframe&rlz=1C1GCEA_enUS995US997&ei=7TuSY7TmGsyJggfflr3YCg&ved=0ahUKEwj0kK_X4er7AhXMhOAKHV9LD6sQ4dUDCA8&uact=5&oq=how+to+python+add+headers+to+dataframe&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIGCAAQCBAeMgUIABCGAzIFCAAQhgMyBQgAEIYDMgUIABCGAzoKCAAQRxDWBBCwAzoHCAAQgAQQDToICAAQCBAeEA06CAgAEAgQBxAeSgQIQRgASgQIRhgAULgCWMkIYMEfaAFwAXgAgAFPiAH1A5IBATeYAQCgAQHIAQjAAQE&sclient=gws-wiz-serp). You'll need to learn a lot of micro skills -pick them up when needed. 
# 
# Following [Iris flower data set](https://en.wikipedia.org/wiki/Iris_flower_data_set) we name the columns:

# In[2]:


column_names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'type']
df = pd.read_csv(url, names = column_names) #read CSV into Python as a dataframe
df # displays the dataframe


# ```{alarm}
# **Your data doesn't look like this?** Different data might need different code. Don't *paste and pray*; adjust what you do according to what you have and need.    
# ```
# 
# Supervised methods use the answers in the data to supervise the model. Does our data contain the answer? If we want to predict the Iris 'type', than yes. It's the only categorical feature so that's what we'll go with. However, a supervised method could also predict any other feature, e.g., 'sepal-length.' A supervised method can't predict what it doesn't have, say plant height or petal color. 
# 
# Enough processing for now. 
# 
# ```{margin}
# What? That's it for data processing? We didn't do much becasue the data didn't need much. Liek a lot od data out there, it was pretty much ready to go. No minimal processing is required. It's only required that your data processing meet the needs of your project, i.e., if it works, you've done enough. [TODO ADD LINK TO DATA REQS](brokenLink-ex-class-sup-desc) 
# ```
# 
# (sup_class_ex: descriptive)=
# ## Descriptive Methods and Visualizations
# 
# Let's explore the data a little. How many different Iris categories do we have?

# In[3]:


num_types = df.groupby(by='type').size();
display(num_types); #another display option.


# Let's *visualize* that.

# In[4]:


num_types.plot.bar(color=['red','blue','green'],rot=0);


# ```{margin}
# Want to do something similar but different? Go to the [libary's docs](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.bar.html). You're going to see lots of different libraries and functions with lots of different options. Don't just copy and paste. Read the docs and understand the parameters.
# ```
# 
# Three evenly distributed categories. What about the distrubtion of the petal widths? As with most things in nature, we might expect it to be somewhat normal.

# In[ ]:





# In[5]:


hist_petal_lengths = df['petal-length'].hist(grid = False,bins=10)


# Not so normal. However, we are looking at all the petal lengths. Let's look at a single type.

# In[6]:


df_typeA = df[df['type'] == 'Iris-setosa']
df_typeA['petal-length'].hist(grid = False, color = 'red');


# Aesthetics are not assessed, but Pandas visualizations are a bit limited compared to others. Below we get a much better picture of what's going on, and we can clealry see the three different types.

# In[7]:


import matplotlib.pyplot as plt
import seaborn as sns

A = df[df['type'] == 'Iris-setosa']['petal-length']
B = df[df['type'] == 'Iris-versicolor']['petal-length']
C = df[df['type'] == 'Iris-virginica']['petal-length']

sns.histplot(A, color = 'red', kde=True, bins = 10)
sns.histplot(B, color ='blue', kde=True, bins = 10)
sns.histplot(C, color = 'green', kde=True, bins = 10)
plt.show()


# In[8]:


sns.lmplot(x='sepal-length', y='sepal-width', data=df, fit_reg=False, hue='type')
# Move the legend to an empty part of the plot
#plt.legend(loc='lower right')
plt.show()


# In[9]:


#correlogram
sns.pairplot(df, hue='type')
plt.show()


# Each images is a descriptive method, and each is a visualization ($\geq3$ meet the requirements). And here is a non-visual description of the data.
# 
# (sup_class_ex: descriptive: describe)=

# In[10]:


df.describe(include='all')


# Play around -*explore*. 
# 
# ## Data product Model Development
# 
# Using inputs and labeled outputs (the "answers"), supervised algoirthms create a model can measure its accuracy and learn over time.
# 
# ### Train Model(s)
# 
# Studying for a test when you have all the answers beforehand will likely yield a good grade. But that grade wouldn't provide a good metric of understanding. Similarly, supervised methods tend to do very well on data their trained with (called overfitting), but you want your model to perform well on *unseen* data. So while it's not required, separating data used to train and test the model (validation) is good practice. Furthermore, it provides content for part D. 
# 
# Fortunately, most libraires have builtin functions for this. Here we'll stick with [sklearn](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html). Validation processes We'll need to split the data into independent (input values) and dependent (output, i.e., the answers) variables. There are many ways to get this done; we'll keep things as dataframes.
# 
# 

# In[11]:


y = df[['type']].copy()
X = df.drop(columns=['type'])

from IPython.display import display_html 
X_styler = X.style.set_table_attributes("style='display:inline'").set_caption('Independents variables')
y_styler = y.style.set_table_attributes("style='display:inline'").set_caption('Dependents variables')
space = "\xa0" * 10 #space between columns
display_html(X_styler._repr_html_()+ space  + y_styler._repr_html_(), raw=True)
#TODO add note about having BOTH as arrays OR dataframes? check compatiability


# In[12]:


import numpy as np
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.333, random_state=41)

from IPython.display import display_html 
X_train_styler = X_train.style.set_table_attributes("style='display:inline'").set_caption('Independents variables')
y_train_styler = y_train.style.set_table_attributes("style='display:inline'").set_caption('Dependents variables')
space = "\xa0" * 10 #space between columns
display_html(X_train_styler._repr_html_()+ space  + y_train_styler._repr_html_(), raw=True)


# Read the [docs](sklearn_link)! By default *train_test_split*, "randomly" splits the sets. Setting the seed or state controls the experiments. See [should you use a random seed](https://datascience.stackexchange.com/questions/78109/should-you-use-random-state-or-random-seed-in-machine-learning-models).

# Other ways to break the data input subsets:

# In[13]:


example = ['A','B','C','D','E','F'];

# first element
print(example[0])
# everything before the 4th element
print(example[:3])
# last element
print(example[-1])
# everything except the last two elements
print(example[:-2])


# In[14]:


# import numpy as np
# from sklearn.model_selection import train_test_split
X_option_b = df.iloc[:, :-1].values
y_option_b = df.iloc[:,4].values
# y_option_b
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
#print(X_train)


# In[15]:


from sklearn import svm

svm_model = svm.SVC(gamma='scale', C=1) #Creates a svm model object. Mote, 'scale' and 1.0 are gamma and C's respective defaults 
svm_model.fit(X_train,y_train) 


# Oh no! What happened? You're learngin a lot of new stuff and errors happen. Just get used to it.
# ```{python}
# DataConversionWarning: A column-vector y was passed when a 1d array was expected. 
# ```
# The sklearn function expected the 'y' data as a 1d array, but I gave it a dataframe. Let's fix that. 
# 
# <!-- TODO? will this margin render in a notebook? -->
# ```{margin}
# [What's that 'gamma' and 'C' for?](https://scikit-learn.org/stable/auto_examples/svm/plot_rbf_parameters.html), read the docs!
# ```

# In[16]:


y_train_array, y_test_array = y_train['type'].values, y_test['type'].values
y_train_array

X_train_array, X_test_array = X_train.values, X_test.values
X_train_array

svm_model.fit(X_train_array,y_train_array) 
#Note: You can use X_train (dataframe) or X_train_array (2d array to fit the model.


# The model is trained! What does that mean? Using the provided data, sklearn's SVM algorithm creates an equation representating the relationship between the indepdendent variables. 
# 
# $$F_{\text{predict}}(X)=\text{prediction(s)}$$
# 
# Here's the code:

# In[17]:


predictions = svm_model.predict(X_train_array)
predictions
#Note: using 'X_train' here, a dataframe, causes the following warning: 
#'UserWarning: X has feature names, but SVC was fitted without feature names...'


# How good are these predictions? Let's check.   

# ### Accuracy Analysis (testing)
# 
# The metric for measuring a classification model's accuracy is straightforward. 
# 
# Most libraries have builtins for this, see [sklearn metrics](https://scikit-learn.org/stable/modules/model_evaluation.html). Again, we'll keep things simple and use [ratio of correct to total predictions](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score):
# 
# $$\text{Accuracy}=\frac{\text{correct predictions}}{\text{total predictions}}$$

# In[18]:


from sklearn import metrics
score = metrics.accuracy_score(y_train_array, predictions)
score


# 96% is pretty good (actually too goo), but we tested the model using the *same* data used to train the model.
# > svm_model.fit(X_train,y_train_array)
# 
# This is *not* good practice. Recall, the *test* data was set aside for this purpose.

# In[19]:


#y_test_array = y_test['type'].values #Converts the dataframe to an array.
predictions2 = svm_model.predict(X_test_array)
score2 = metrics.accuracy_score(y_test_array,predictions2)
score2


# $94\%$ of the predictoins are correct. A *confusion matrix* futher breaksdown the predictions by categories. This helps develop better models and alos provides another visualization.
# 
# ```{margin} Why is it called a confusion matrix?
# As it makes things less confusing, it would seem to be a misnomer. The name comes from making it easier to see whether the system is confusing two categories (i.e. commonly mislabeling one as another). Another (maybe less confusing) name is an *error matrix*.
# 
# ```

# In[20]:


cm = metrics.confusion_matrix(y_test, predictions2, labels=svm_model.classes_)
disp = metrics.ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=svm_model.classes_)
disp.plot();


# 94%, which still seems fairly good ([but what is "good" accuracy?](TODO add link), but if selecting the test data randomly (try 'random_state=42') accuracy may actually *improve* on the test data because the the set is realtively small and the model fairly accurate. Using these results, the model can be further refined. However, continually tweaking parameters according to the test data results means we are back to studying from the answers, i.e., the risk of overfititng has been reintroduced. To deal with this, a *third set* can be withheld, called a “validation set," to analyze final results. 
# 
# But Partitioning available data into three sets, reduces the avaialble data for training the model. Making results more dependent on the random selection of training, testing, and validation sets. [Cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html) addresses this issue by resampling the data. Again, this not required, but could be very useful, particaularly for small data sets. 

# In[21]:


from sklearn.model_selection import KFold, cross_val_score
# Our 'y' is a datafram but this functions requires the indepenent variables ot be a 1d array.
y_array = np.ravel(y.values)

k_folds = KFold(n_splits = 5, shuffle=True)
# The number of folds determines the test/train split for each iteration. 
# So 5 folds has 5 different mutually exclusive training sets. 
# That's a 1 to 4 (or .20 to .80) testing/training split for each of the 5 iterations.

scores = cross_val_score(svm_model, X, y_array)
# This shows the average score. Print 'scores' to see an array of individual iteration scores.
print("Average Score: ", scores.mean())


# #### Logistic Regression (a classification method)
# 
# You should experiemt and try different alogirthms. Logistic regression preidcts a probability of something being in a category (hence it's "regression" name), and then that probability can used to predict whether it's in that categort (so it's also a classification method). We'll use [sklearn logistic regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) to do the latter.  

# In[22]:


from sklearn.linear_model import LogisticRegression

log_model = LogisticRegression(random_state=0).fit(X_train, y_train_array)


# That's right, a whole new model in just two lines of codes. This is typical if you stay within the same library.   

# In[23]:


predictions_log = log_model.predict(X_test)
score = metrics.accuracy_score(y_test, predictions_log)
score


# Machine learnign is a mix of art and science requiring a balance of knowledge, intuition, and lots of *experimentation*. Do some research, play around, make lots of tweaks, and constantly re-run code. 

# ## User Interaction
# 
# We've made an application. Now we only need to implement a way for the user to apply it. There are no specifc requirements for how this done. Following the [User Guide](task2d:userguide) in your documentation, evalautor must be able to easily get it to work and meet the needs of the problem descried in the documentation. We'll present a few options. Keep in mind that simpler interfaces need a more detailed [User Guide](task2d:userguide).   
# 
# **Detail how the user inputs and runs code:**
# 
# The user can be instructed to input and run code. If you do this provide explicit instructions and provide an example that can copied and pasted.
# 
# > To make a prediction for varaibles x1, x2, x3 and x4, type 
# >
# >- 'print(svm_model.predict([[x1,x2,x3,x4]]))' 
# >
# > into the code cell below and press the 'Run' button in the menu. 
# > Example:
# >
# >- 'print(svm_model.predict([[1,2,3,2]]))'

# In[24]:


print(svm_model.predict([[5,4,1,.5]]))


# ```{note}
# When making predictions, the input data needs to look *exactly* like the data the model as trained with. In this example, 'svm_model' was trained with a 2d-array. Hence the need for the double brackets, '[[5,4,1,.5]]'.
# ```
# 
# **User input from widget button:**
# 
# Using widgets, we can 
# TODO ADD CONDA/PIP install instuctions
# Recall, the feaure names:

# In[25]:


list(df.columns)
df.head()


# In[26]:


from ipywidgets import widgets

#The text boxes where the user can input values.
sl_widget = widgets.FloatText(description='sepal L:', value='0')
sw_widget = widgets.FloatText(description='sepal W:', value='0')
pl_widget = widgets.FloatText(description='petal L:', value='0')
pw_widget = widgets.FloatText(description='petal W:', value='0')

#A button for the user to get predictions using input valus. 
button_predict = widgets.Button( description='Predict' )
button_ouput = widgets.Label(value='Enter values and press the \"Predict\" button.' )

#Defines what happens when you click the button 
def on_click_predict(b):
    prediciton = svm_model.predict([[
        sl_widget.value, sw_widget.value, pl_widget.value, pw_widget.value]])
    button_ouput.value='Prediction = '+ str(prediciton[0])
button_predict.on_click(on_click_predict)

#Displays the text boxes and button inside a VBox 
vb=widgets.VBox([sl_widget, sw_widget, pl_widget, pw_widget, button_predict,button_ouput])
print('\033[1m' + 'Enter values in cm and make a prediction' + '\033[0m')
display(vb)

# According to the widget docs, 
# https://ipywidgets.readthedocs.io/en/7.6.3/examples/Widget%20Styling.html
# you cannot adjust the description length. For adjusting widget display behavior, 
# you can use a labeled HBox contained in the VBox.


# **User types input with slider widgets:**
# 
# Sliders provide a user-frendly experience which cen easily be modified to control input range and increments. While sliders might not be the best choice here (selecting precise values might be easier via text entry), we'll present an example as in many cases sliders work great. 
# 
# Implmentation is almost identical to that of text entry. Reviewing the [data's statistics](sup_calls_ex:descriptive:describe), we set the sliders' ranges. See [widget slider docs](https://ipywidgets.readthedocs.io/en/7.6.3/examples/Widget%20List.html#FloatSlider) for more details and options.

# In[27]:


df.describe()


# In[28]:


feature = 'petal-width'

r_max = str(df[feature].describe()['mean']+2*df[feature].describe()['std'])
r_min = str(df[feature].describe()['mean']-2*df[feature].describe()['std'])

print('min='+r_min +', min='+r_max)


# In[29]:


#The sliders where the user can input values. Min and max are set by using the complete datasets' 
sl_widget = widgets.FloatSlider(description='sepal L:',min=4.19, max=7.4)
sw_widget = widgets.FloatSlider(description='sepal W:', min=2.19, max=3.9)
pl_widget = widgets.FloatSlider(description='petal L:', min=0.23, max=7.29)
pw_widget = widgets.FloatSlider(description='petal W:', min=0.0, max=2.72)

#A button for the user to get predictions using input valus. 
button_predict = widgets.Button( description='Predict' )
button_ouput = widgets.Label(value='Enter values and press the \"Predict\" button.' )

#Defines what happens when you click the button 
def on_click_predict(b):
    prediciton = svm_model.predict([[
        sl_widget.value, sw_widget.value, pl_widget.value, pw_widget.value]])
    button_ouput.value='Prediction = ' + str(prediciton[0])
button_predict.on_click(on_click_predict)

#Displays the text boxes and button inside a VBox 
vb=widgets.VBox([sl_widget, sw_widget, pl_widget, pw_widget, button_predict,button_ouput])
print('\033[1m' + 'Enter parameter values (in cm) and make a prediction:' + '\033[0m')
display(vb)


# To automatically update values from widget see [get the current value of a widget](https://discourse.jupyter.org/t/is-it-possible-to-get-the-current-value-of-a-widget-slider-from-a-function-without-using-multithreading/15524) and [automatically run code after altering widget](https://stackoverflow.com/questions/54412449/ipywidgets-automatically-update-variable-and-run-code-after-altering-widget-val#:~:text=import%20ipywidgets%20as%20widgets%20class%20Updated:%20def%20__init__,(v):%20update_class.update%20(v)%20slider.observe%20(on_change,%20names='value')%20display%20(slider)).
# 
# **Other Input Methods**
# 
# What other methods are allowed? Anything the evaluator (playing the role of the client) can get to work follwoign your instructions. Consider user-friendliness when choosing your interface. With four independent vaeraibles, four input boxes or sliders works fine. But what if your model uses 400 varaibels? Or say the client needed to classify, not one, but hundreds of flowers? In such cases, the user could be directed to copy or upload their data, say a .xlsx or .csv file, to location the  model can retrieve and analyze. Whatever method you choose, don't make things difficult for the evaluator. Provide explicit instructions, examples, or (when appropiate) example data files. 
# 
# 
