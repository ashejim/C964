#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm
# Reloading this well worn dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
df = pd.read_csv(url) #read CSV into Python as a dataframe

column_names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'type']
df = pd.read_csv(url, names = column_names) #read CSV into Python as a dataframe

X = df.drop(columns=['type']) #indpendent variables
y = df[['type']].copy() #dependent variables
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.333, random_state=41)
y_train_array, y_test_array = y_train['type'].values, y_test['type'].values
y_train_array
X_train_array, X_test_array = X_train.values, X_test.values
X_train_array

svm_model = svm.SVC(gamma='scale', C=1) #Creates a svm model object. Mote, 'scale' and 1.0 are gamma and C's respective defaults 
svm_model.fit(X_train_array,y_train_array);



# (sup_class_ex:user_interface)=
# ## User Interface
# 
# We've made an application. Now we need a way for the user to apply it. There are *no specific requirements for how this must be done.* Following the [User Guide](task2d:userguide) in your documentation, the evaluator must be able to quickly get it to work and meet the needs of the problem described in the documentation. We'll present a few options. Remember that simpler interfaces need a more detailed [User Guide](task2d:userguide). 
# 
# (sup_class_ex:ui:code)=
# ### User inputs and runs code
# 
# The user can be instructed to input and run code. If you do this, provide explicit instructions and provide an example that can be copied and pasted.
# 
# > To make a prediction for varaibles x1, x2, x3 and x4, type 
# >
# >- 'print(svm_model.predict([[x1,x2,x3,x4]]))' 
# >
# > into the code cell below and press the 'Run' button in the menu. 
# > Example:
# >
# >- 'print(svm_model.predict([[1,2,3,2]]))'

# In[2]:


print(svm_model.predict([[5,4,1,.5]]))


# ```{note}
# When making predictions, the input data needs to look *exactly* like the data the model as trained with. In this example, 'svm_model' was trained with a 2d-array. Hence the need for the double brackets, '[[5,4,1,.5]]'.
# ```
# 
# ### User inputs from Widget text boxes & buttons
# 
# Using Jupyter Widgets, a more user-friendly (and less error-prone) interface can be implemented. 
# <!-- TODO ADD CONDA/PIP install instructions -->
# 
# ```{warning}
# Running Python code requires a running Python kernel. Click the {fa}`rocket` --> {guilabel}`Live Code` button above on this page, and run the code below.
# 
# 🚧 This site is under construction! As of now, the Python kernel may not run on the page or have very long wait times.👷🏽‍♀️
# ```
# 
# 
# Click the {fa}`rocket` --> {guilabel}`Live Code` button above on this page, and run the code below.
# 
# Recall, the feature names:

# In[3]:


list(df.columns)
df.head()


# In[4]:


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

#Displays the text boxes and buttons inside a VBox 
vb=widgets.VBox([sl_widget, sw_widget, pl_widget, pw_widget, button_predict,button_ouput])
print('\033[1m' + 'Enter values in cm and make a prediction' + '\033[0m')
display(vb)

# According to the widget docs, 
# https://ipywidgets.readthedocs.io/en/7.6.3/examples/Widget%20Styling.html
# you cannot adjust the description length. For adjusting widget display behavior, 
# you can use a labeled HBox contained in the VBox.


# ### User inputs with Widget sliders
# 
# Sliders provide a user-friendly experience that can easily be modified to control input range and increments. While sliders might not be the best choice here (text entry might be easier for selecting precise values), we'll present an example as, in many cases, sliders work great. 
# 
# Implementation is almost identical to that of text entry. Reviewing the [data's statistics](sup_calls_ex:descriptive:describe), we set the sliders' ranges to capture approximately 95% of the flower's parameter values:
# 
# $\text{range}= \text{mean)\pm 2(\text{standard deviation})$
# 
# Assuming it's normally distributed (it's close enough). Capturing 99.7% of the data using 3 standard deviations might've been better -but you get the idea. 
# 
# For example, 
# 
# ```{margin} 
# See [widget slider docs](https://ipywidgets.readthedocs.io/en/7.6.3/examples/Widget%20List.html#FloatSlider) for more details and options.
# ```

# In[5]:


df.describe()


# In[6]:


feature = 'petal-width'
r_max = str(df[feature].describe()['mean']+2*df[feature].describe()['std'])
r_min = str(df[feature].describe()['mean']-2*df[feature].describe()['std'])

print('min='+r_min +', min='+r_max)


# Similarly, finding ranges for each independent variable, the sliders are set up.

# In[7]:


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


# To automatically update values from a Widget, see [get the current value of a widget](https://discourse.jupyter.org/t/is-it-possible-to-get-the-current-value-of-a-widget-slider-from-a-function-without-using-multithreading/15524) and [automatically run code after altering widgets](https://stackoverflow.com/questions/54412449/ipywidgets-automatically-update-variable-and-run-code-after-altering-widget-val#:~:text=import%20ipywidgets%20as%20widgets%20class%20Updated:%20def%20__init__,(v):%20update_class.update%20(v)%20slider.observe%20(on_change,%20names='value')%20display%20(slider)).
# 
# ### Other Input Methods
# 
# What are user interface approaches allowed? Anything the evaluator (playing the role of the client) can get to work following your instructions. Consider user-friendliness when choosing your interface. With four independent variables, four input boxes or sliders work fine. But what if your model uses 400 variables? Or say the client needed to classify not one but hundreds of flowers? In such cases, the user could be directed to copy or upload their data, say a .xlsx or .csv file, to a location the model can retrieve and analyze. Whatever method you choose, don't make things difficult for the evaluator. Provide explicit instructions, examples, or (when appropriate) example data files. 
