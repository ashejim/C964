(task2c)=
<!-- hack to open links in new tab -->
<head>
    <base target="_blank">
</head>

# Task 2: Part C -the application

Your software application (the "app") is the entirety of part C of task 2. However, the Computer Science capstone is *not* a software project. Other than requiring an application of machine learning to data, they will assess *what* your application does -not how. 

```{margin} **What is an *application*?**
An application (app) is simply software that performs specific tasks. 
```
(task2c:appreqs)
## What does the application need to do?

Your app must help the user solve the organizational problem from [task 1](task1) by doing the following:  

1. Use data to develop a machine learning model.

2. Apply the ML model to user-provided data.   

3. Provide visualizations (pictures).

4. Provide an interactive front-end (interface) so the user can use the application to help solve their organizational problem.  

`````{tab-set}
````{tab-item} Example 1
>**The App:** A standalone Python project which can predict Iris types.
> 
>**Data &rarr; ML model:** Labeled [Iris petal dimensions](https://www.kaggle.com/datasets/uciml/iris) train an SVN classification model.
>
> **New data &rarr; ML model &rarr; prediction:** Using new flower dimensions, the model can predict the Iris type. 
>
> **Visualizations:** Histograms showing distributions of different flower features and a confusion matrix illustrating the accuracy of the classification model.
>  
> **User interface:** Following detailed instructions, via console the user can input flower dimensions and the app returns a prediciton.
````
````{tab-item} Example 2
> **The App:** A standalone [Jupyter Notebook](https://jupyter.org) file (.ipynb) predicting house prices.
>
> **Data &rarr; ML model:** Labeled housing data trains a multi-linear regression model to predict house prices.
>
> **New data &rarr; ML model &rarr; prediction:** Using unseen house data, the model predicts the house's price. 
>
> **Visualizations:** Histograms showing distributions of data features and scatterplots demonstrating data correlations.  
>
> **User interface:** Following detailed instructions, via the Jupyter notebook file, the user can adjust widget sliders to get a price prediciton.
````
````{tab-item} Example 3
> **The App:** A web app providing movie recommendations.
>
> **Data &rarr; ML model:** Cosine similarity provides a similarity score between any two movies. 
>
> **User data &rarr; ML model &rarr; recommendation:** Using a user provided movie, the five most similiar movies are returned. 
>
> **Visualizations:** Histograms showing distributions of movie features and samples of Cosine Similarity matrices.  
>
> **User interface:** A web app (developed with [Juptyer, voila, and deployed on Heroku](https://pythonforundergradengineers.com/deploy-jupyter-notebook-voila-heroku.html) returns five recommendations for a user typed movie.
````
````{tab-item} Example 4
> **The App:** A hosted Jupyter notebook identifies images as a cat or dog.  
>
> **Data &rarr; ML model:** Labeled images are used to [train a neural network model to classify images](https://www.tensorflow.org/tutorials/images/classification) of dogs and cats.
>
> **New data &rarr; ML model &rarr; prediction:** Loading an image from a hosted folder, the model classifies it as a dog or cat. 
>
> **Visualizations:** Graphs of training and validation accuracy and loss, a confusion matrix showing model accuracy, and image examples.
>
> **User interface:** Follwoing detailed instructions, the user can upload an image to Jupyter notebook deployed on [Datalore](https://datalore.jetbrains.com), and the app classifies the image as cat or dog.
````
`````

(task2c:faq)=
## FAQ
**What are the most common reasons for the task 2 code being returned?**

1. Evaluators cannot get the code to run as intended. This usually happens because of an incomplete or incorrect [user guide](task2doc:d) or because evaluators don't have access to shared cloud links. 

2. Evaluators are not certain how the code is meant to be used by the "user." Again, an incomplete or incorrect [part D user guide](task2doc:d) is usually the culprit. Adding an explicit example (and including example user files when appropriate) also helps avoid this issue.

**I've completed the coding for task 2. Should I send it to my course instructor for review?** 

If you have specific questions or concerns -yes. However, if the code runs and meets the [minimum app requirements](task2c:appreqs) it's usually best to move on to the [documentation](task2doc). As you can continue to tweak and improve the app, but can be comfortable knowing that what you have can pass. 

**I need help with part C. Who do I contact?**

That depends on what you need help with. For questions about the capstone, how to meet the requirements, and how to best approach the project to meet your individual goals, contact your [assigned course instructor](cipage:capcis) or [capstone team inbox](mailto:ugcapstoneit@wgu.edu?cc=your%20assigned%20CI&subject=C964%20capstone%20question). However, the capstone team supports all of the IT college capstone projects. As such, your assigned course instructor may not have the expertise to answer technical questions related to computer science or coding. Particularly debugging code, given the wide range of approaches, languages, and libraries available for use.  

For technical questions related to code or math, see the [CS and software subject matter expert list](cspage). Keep in mind, that while these faculty may be subject matter experts in their field, they do *not* necessarily support the capstone, and so may not know your capstone requirements. Hence it is often best to contact your capstone instructor first, so you can appropriately limit the scope of your question(s). When contacting faculty on the [CS and software subject matter expert list](cspage), always follow the [guidelines](cspage:guideline).

Remember, our job (as educators) is to help *you* fix your problem -not just fix it for you. 

ALSO IN TASK1
**What if I start working on task 2 and want to change things? Do I need to resubmit task 1?** 

No, not unless it's an entirely different topic. Minor changes from task 1 to task 2 are expected and allowed *without updating the approval form*. Evaluators will not rigorously compare tasks 1 and 2. Task 2 is where the work is, and even with complete topic changes at most, you'll be asked to revise the approval form (if at all). So never let task 1 dictate what you do in task 2.  


**How many attempts are allowed for each task?**

You have unlimited submissions (as with all WGU performance assessments). Furthermore, a project requiring multiple submissions is not precluded from being given an excellence award. However, do attempt to fully meet *each* requirement as submissions falling significantly short of the minimum requirements may be *locked* from further submissions without instructor approval. Moreover, such submissions do not receive meaningful evaluator comments.   

**What is a descriptive method?**
Anything that describes the data. Histograms, scatterplots, pie charts -all the familiar descriptive statistics techniques are included. ML methods such as k-means clustering can also be descriptive. Whether a method is descriptive or non-descriptive is determined by its use. For example, using a regression line to describe the relationship between variables is descriptive, but using the line to predict a variable or claim a correlation between the variables exist is inferential (non-descriptive)   

**What is a non-descriptive method?**

Anything that infers from the data, e.g., making predictions, recommendations, identifying correlations, inferring from correlations, etc. Also, see the comments above. 

**What is machine learning?**

That depends on who you ask! But for this project, it is an algorithm applied to data. 

For computer science, Machine learning is a subfield of artificial intelligence (which is a subfield of mathematics), broadly defined as the development of machines capable of self-adjusting behavior based on data. However, from the data science perspective, machine learning is generally defined as the practice of using algorithms to identify patterns, make predictions, etc. from data. That is, machine learning is a goal, not a technique. So for example, a data scientist (and the evaluators) consider linear regression machine learning -when it's used as a prediction model, but a mathematician would politely (or not so politely) disagree.       

**Can I use libraries outside the standard (Python, Java, etc.) installation?**

Yes. Unlike C950 (Data Structures & Algorithms II), you are allowed and encouraged to use outside libraries. All the major languages, but particularly Python, have a wide array of highly developed ML tools. The C964 capstone is about the application of these tools -not their development.   

TODO ADD PICTURES

**What sort of user interface do I need? Do I need a GUI?**

No, a GUI is *not* required. Your app must be usable by the "client" towards solving the proposed problem. If the evaluators can get run your app as intended playing the role of the "client" following your [user guide](task2_doc:userguide), then your app will be considered to have a user-friendly interface. This can be done through a GUI and widgets but using the command line or reading user data from a local directory will also suffice.       


TODO DOC FAQ
**Are there length requirements for the documentation?**

No. What you see in the examples (ADD LINKS) are just guidelines. The individual evaluator determines what qualifies as "sufficient detail" which further varies depending on the project and writing style. If you feel you've met the requirements, simply move on to the next section. Upon submission, it will pass, or they will request more details.

**I've completed the task 2 documentation. Should I send it to my course instructor for review?** 

If you have specific questions or concerns -yes. However, in most cases, it's best just to submit. What suffices as “sufficient detail” is highly subjective. We can always tell you to add more, but if you've done your best to fulfill the requirements, submit it and let them tell you which (if any) parts need to be rewritten. At best, it passes; at worst, we address the issues cited by the evaluator -and then it passes. Responding to the more narrow focus of the evaluator's comments is generally easier than overworking the entire project.

You have *unlimited* submissions but limited time. And, typically this is the best and most efficient approach. 