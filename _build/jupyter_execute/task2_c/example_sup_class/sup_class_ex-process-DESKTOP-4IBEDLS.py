#!/usr/bin/env python
# coding: utf-8

# 
# 
# (sup_class_ex:data)=
# 
# ## Data Exploring and Processing
# 
# Here we'll do two essential things. 
# 1. Process the data.
# 2. Analyze the data.
# 
# Processing will involve importing, cleaning, and sorting raw data; preparing it to be analyzed. Exploring the data builds an understanding of it and the problem you're trying to solve, equipping you to choose a machine-learning application.       
# 
# Before doing anything with raw data, you must import it.

# In[1]:


# We'll import libraries as needed, but when submitting, 
# it's best to have them all at the top.
import pandas as pd

# Load this well-worn dataset:
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
df = pd.read_csv(url) #read CSV into Python as a DataFrame
df # displays the DataFrame



# Oops. The first row of data has been set as headers. Some data sets have headers already -this one doesn't. How do we fix that? Google ["how to python add headers to dataframe"](https://www.google.com/search?q=how+to+python+add+headers+to+dataframe&rlz=1C1GCEA_enUS995US997&ei=7TuSY7TmGsyJggfflr3YCg&ved=0ahUKEwj0kK_X4er7AhXMhOAKHV9LD6sQ4dUDCA8&uact=5&oq=how+to+python+add+headers+to+dataframe&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIGCAAQCBAeMgUIABCGAzIFCAAQhgMyBQgAEIYDMgUIABCGAzoKCAAQRxDWBBCwAzoHCAAQgAQQDToICAAQCBAeEA06CAgAEAgQBxAeSgQIQRgASgQIRhgAULgCWMkIYMEfaAFwAXgAgAFPiAH1A5IBATeYAQCgAQHIAQjAAQE&sclient=gws-wiz-serp). You'll need to learn a lot of micro-skills -pick them up when needed. Reading up on the data set, [Iris flower data set](https://en.wikipedia.org/wiki/Iris_flower_data_set), we name the columns:

# In[2]:


column_names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'type']
df = pd.read_csv(url, names = column_names) #read CSV into Python as a DataFrame
df # displays the DataFrame


# ```{alarm}
# **Your data doesn't look like this?** Different data might need different code. Don't *paste and pray*; adjust what you do according to what you have and need.    
# ```
# 
# Supervised methods use "answers" in the data to supervise the model. Does our data contain the "answers"? If we want to predict the Iris 'type,' then yes. It's the only categorical feature, so we'll go with it. However, a supervised method could predict *any* of the features, e.g., 'sepal-length.' A supervised method can't predict what it doesn't have, say, plant height or petal color. 
# 
# ```{margin}
# What? That's it for data processing? We didn't do much becasue the data didn't need much. Like a lot of data out there, it was (mostly) ready to go. No minimal processing is required. The project's needs determine the required data processing, i.e., if it works, you've done enough. See [Data Requirements](task2c:data_requirements). 
# ```
# 
# That's all the processing needed for now. 
# 
# (sup_class_ex:descriptive_methods_and_visualizations)=
# 
# ### Descriptive Methods and Visualizations
# 
# Let's explore the data. A good starting question: how many different Iris categories do we have?

# In[3]:


num_types = df.groupby(by='type').size();
display(num_types); 


# (sup_class_ex:descriptive:visuals)=
# Let's *visualize* that.
# <!-- NOTE: Alt text for Python generated images added using Jupyter notebook cell's "img alt": "A bar plot is displayed. The x-axis are the type categories, and the y-axis is the number in the categories. Three bars Iris-setosa (red), Iris-versicolor (blue), and Iris-virginica (green) are each equal to 50",
#      "output_type": "display_data"-->

# In[4]:


num_types.plot.bar(color=['red','blue','green'],rot=0);


# In[5]:


from numpy import random
import matplotlib.pyplot as plt

x = random.randint(10, size=(10))
y = random.randint(10, size=(10))

plt.scatter(x, y)
img_fn = 'example.png'
plt.savefig(img_fn)

img2 = Image(filename=img_fn, alt="another image")
# _repr_html_() returns None
assert img2._repr_html_() == None


# ```{margin}
# Want to do something similar but different? Go to the [libary's docs](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.bar.html). You'll see lots of libraries and functions with lots of options. Don't just copy, paste, and pray. Read the docs and understand the parameters.
# ```
# 
# Three evenly distributed categories. What about the distribution of the petal widths? As with most things in nature, we might expect it to be somewhat normal.
# 
# (sup_class_ex:descriptive:visuals:histograms)=

# In[6]:


hist_petal_lengths = df['petal-length'].hist(grid = False,bins=10)


# Not so normal. However, we are looking at the petal lengths of all three types. So let's look at a single type.

# In[7]:


df_typeA = df[df['type'] == 'Iris-setosa']
df_typeA['petal-length'].hist(grid = False, color = 'red');


# They don't assess aesthetics, but Pandas' visualizations are limited compared to others. Below we get a much better picture of what's going on, and we can clearly see the three different types.
# 
# A **bar plot** to visualize distributions:

# In[8]:


import matplotlib.pyplot as plt
import seaborn as sns

A = df[df['type'] == 'Iris-setosa']['petal-length']
B = df[df['type'] == 'Iris-versicolor']['petal-length']
C = df[df['type'] == 'Iris-virginica']['petal-length']

sns.histplot(A, color = 'red', kde=True, bins = 10)
sns.histplot(B, color ='blue', kde=True, bins = 10)
sns.histplot(C, color = 'green', kde=True, bins = 10)
plt.show()


# A **scatterplot** to visualize correlations: 

# In[9]:


sns.lmplot(x='sepal-length', y='sepal-width', data=df, fit_reg=False, hue='type')
# Move the legend to an empty part of the plot
#plt.legend(loc='lower right')
plt.show()


# A **correlogram** to visualize distributions and correlations of and between multiple variables.

# In[10]:


#correlogram
sns.pairplot(df, hue='type')
plt.show()


# Each image is a descriptive method *and* a visualization ($\geq3$ meets the requirements). And here are some non-visual descriptions of the data:

# In[11]:


df.describe(include='all')


# Play around -*explore*. 
