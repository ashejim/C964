#!/usr/bin/env python
# coding: utf-8

# Running Python code requires a running Python kernel. Click the {fa}`rocket` --> {guilabel}`Live Code` button above on this page, and run the code below.
# 
# ```{warning}
# 🚧 This site is under construction! As of now, the Python kernel may not run on the page or have very long wait times. Also, expect typos.👷🏽‍♀️
# ```
# (sup_class_ex)=
# # Example: Supervised Classification App
# 
# Supervised classification fits the project requirements well, and is also a good place to start. The nature of your Data and organizational needs dictate which methods you can use. So what type of data do we need? 
# 
# - One of those features is the category you want to predict (the dependent variable).
# - At least one other feature (the independent variable(s)).
# 
# This will be a simple example. Simple data. Simple model. Simple interface. However, it does demonstrate the minimum requirements for [part C](task2c). We'll also show how things can progressively be improved in [part 2], building on the *working* code. Simple is a great place to start -scaling up is typically easier than going in the other direction. 
# 
# <p float="center">
#   <img src='https://raw.githubusercontent.com/ashejim/C964/main/url_images/iris_dim.png' height="250" />
#   <img src='https://raw.githubusercontent.com/ashejim/C964/main/url_images/plot_iris_svc.png' height="250" /> 
# </p>
# 
# Let's look at the famous [Fisher's Iris data set](https://en.wikipedia.org/wiki/Iris_flower_data_set): 

# In[1]:


#We'll import libraries as needed, but when submitting, 
# it's best having them all at the top.
import pandas as pd

# Load this well-worn dataset:
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
df = pd.read_csv(url) #read CSV into Python as a DataFrame
df # displays the DataFrame

column_names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'type']
df = pd.read_csv(url, names = column_names) #read CSV into Python as a DataFrame
pd.options.display.show_dimensions = False #suppresses dimension output
display(df)
#Code hide and toggle managed with Jupyter meta-code 'tags.'


# Though we described everything as "simple," we'll also see that this dataset is quite *rich* with angles to investigate, and we have many options now. However, a classification project must use a categorical feature as its independent variable, and for this, the only immediate choice is 'type.'

# In[2]:


##preserves Jupyter preview style after applying .style
##preserves Jupyter preview style (the '...') after applying .style
def display_df(dataframe, column_names, highlighted_col, precision=2):
    pd.set_option("display.precision", 2)
    columns_dict = {}
    for i in column_names:
        columns_dict[i] ='...'
    df2 = pd.concat([dataframe.iloc[:5,:],
                       pd.DataFrame(index=['...'], data=columns_dict),
                       dataframe.iloc[-5:,:]]).style.format(precision = precision).set_properties(subset=[highlighted_col], **{'background-color': 'yellow'})
    pd.options.display.show_dimensions = True
    display(df2)

#display df with highlighted column 
display_df(df, column_names, 'type', 1)


# 
# :::{sidebar} Watch
# <iframe src="https://wgu.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=ae4e4987-3196-4b67-9752-ae010137b64c&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=true&interactivity=all" title="Simple ML supervised classification example " style="border: 1px solid #464646;" class="center" allowfullscreen allow="autoplay">
# </iframe>
# :::
# 
# The highlighted column, 'type,' provides something to predict/classify (dependent variables), and the non-highlighted columns are something by which to make that prediction/classification (independent variables).
