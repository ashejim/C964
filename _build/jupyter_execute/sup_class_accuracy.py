#!/usr/bin/env python
# coding: utf-8

# ## Accuracy Analysis (testing)
# 
# The metric for measuring a classification model's accuracy is straightforward. 
# 
# Most libraries have builtins for this; see [sklearn metrics](https://scikit-learn.org/stable/modules/model_evaluation.html). Again, we'll keep things simple and use [ratio of correct to total predictions](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score):
# 
# $$\text{Accuracy}=\frac{\text{correct predictions}}{\text{total predictions}}$$

# In[1]:


#We'll import libraires as needed, but when submitting, having them all at the top is best practice
#Here's the minimum code needed from previsou sections. 
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
column_names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'type']
df = pd.read_csv(url, names = column_names) #read CSV into Python as a dataframe

X = df.drop(columns=['type']) #indpendent variables
y = df[['type']].copy() #dependent variables
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.333, random_state=41)

svm_model = svm.SVC(gamma='scale', C=1) #Creates a svm model object. Mote, 'scale' and 1.0 are gamma and C's respective defaults  
X_train_array, X_test_array = X_train.values, X_test.values
y_train_array, y_test_array = y_train['type'].values, y_test['type'].values

svm_model.fit(X_train_array,y_train_array)
predictions = svm_model.predict(X_train_array)


# In[2]:


from sklearn import metrics
score = metrics.accuracy_score(y_train_array, predictions)
score


# 96% is pretty good (actually too good), but we tested the model using the *same* data used to train the model.
# > svm_model.fit(X_train,y_train_array)
# 
# Testing with the training data is *not* good practice. Recall the *test* data was set aside for this purpose.

# In[3]:


#y_test_array = y_test['type'].values #Converts the dataframe to an array.
#predictions using test data
predictions_test = svm_model.predict(X_test_array)
score2 = metrics.accuracy_score(y_test_array,predictions_test)
score2


# Using the test data we set aside, $94\%$ of the predictions are correct. 
# 
# A *confusion matrix* further breaks down the predictions by categories, helping develop better models and providing another visualization.
# 
# ```{margin} Why is it called a confusion matrix?
# As it makes things less confusing, it would seem to be a misnomer. The name comes from making it easier to see whether the system is confusing two categories (i.e., commonly mislabeling one as another). Another (maybe less confusing) name is an *error matrix*.
# ```

# In[4]:


cm = metrics.confusion_matrix(y_test, predictions_test, labels=svm_model.classes_)
disp = metrics.ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=svm_model.classes_)
disp.plot();


# 94%, which still seems fairly good ([but what is "good" accuracy?](TODO add link), but if selecting the test data randomly (try 'random_state=42'), accuracy may actually *improve* on the test data because the set is relatively small and the model fairly accurate. Using these results, the model can be further refined. However, continually tweaking parameters according to the test data results means we are back to studying from the answers, i.e., reintroducing the risk of overfitting. To deal with this, a *third set* can be withheld, called a “validation set," to analyze the final results. 
# 
# But Partitioning available data into three sets reduces the available data for training the model, making results more dependent on the random selection of training, testing, and validation sets. [Cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html) addresses this issue by resampling the data. Again, this is optional but could be very useful, particularly for small data sets. 

# In[5]:


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


# ### More testing and development 
# 
# Now we can further develop the model until our heart's content. Refine the model through a cyclic process guided by knowledge and experimentation. Research, try different algorithms, and adjust. They've built the libraries for this so that the additional coding effort will be lite. These steps are optional and not required, but this is where things become more exciting and challenging. 
# 
# Machine learning is a mix of art and science, requiring a balance of knowledge, intuition, and lots of *experimentation*. Research, play around, tweak, and constantly re-run code. 
# 
# ### Logistic Regression
# 
# Logistic regression predicts the probability of something being in a category (hence its "regression" name). That probability indicates whether it's in that category, e.g., $.65 > .50 \Rightarrow \text{yes}$  (so it's also a classification method). We'll use [sklearn logistic regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) to do the latter.  

# In[6]:


from sklearn.linear_model import LogisticRegression
log_model = LogisticRegression(random_state=0).fit(X_train, y_train_array)


# That's right, a new model in just two lines of code. This is typical if you stay within the same library. From here we can test, improve, and compare.

# In[7]:


predictions_log = log_model.predict(X_test)
score = metrics.accuracy_score(y_test, predictions_log)
score


# TODO 
# 
# ### Support Vector Machine (SVM)
# 
# ### Decision Tree
# 
# ### Naive Bayes 
