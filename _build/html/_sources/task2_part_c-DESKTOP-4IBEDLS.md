<!-- hack to open links in new tab -->
<head>
    <base target="_blank">
</head>

(task2c)=
# Task 2: Part C -the application

Your software application (the "app") is the entirety of part C of task 2. However, the Computer Science capstone is *not* a software project. Other than requiring an application of machine learning to data, they will assess *what* your application does -not its presentation. 

```{margin} **What is an *application*?**
An application (app) is simply software that performs specific tasks. 
```

:::{warning}
*Do not follow the official C964 rubric.* Instead, follow the guidelines on this webpage and the [Task 2 template](https://westerngovernorsuniversity-my.sharepoint.com/:w:/g/personal/jim_ashe_wgu_edu/ERGxhsNfkbhEutlkXVFITMQBPOmWlkVx1p5H0UisvnBesg?rtime=3q_Efs-u2kg). This template has seemingly become the defacto rubric and is what evaluators expect. 
:::

(task2c:appreqs)=
## What does the application need to do?

Your app must help the user solve the organizational problem from [task 1](task1) by doing the following:  

1. Use data to develop a machine learning model.

2. Apply the ML model to user-provided data.   

3. Provide visualizations (pictures; they can be presented in the app or document).

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
> **User interface:** Following detailed instructions via the console, the user can input flower dimensions, and the app returns a prediction.
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
> **User interface:** Following detailed instructions via the Jupyter notebook file, the user can adjust widget sliders to get a price prediction.
````
````{tab-item} Example 3
> **The App:** A web app providing movie recommendations.
>
> **Data &rarr; ML model:** Cosine similarity provides a similarity score between any two movies. 
>
> **User data &rarr; ML model &rarr; recommendation:** Using a user-provided movie, the five most similar movies are returned. 
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
> **User interface:** Following detailed instructions, the user can upload an image to Jupyter notebook deployed on [Datalore](https://datalore.jetbrains.com), and the app classifies the image as cat or dog.
````
`````

(task2c:datareqs)=
### Data requirements 

- Your data must be sufficiently complex and processed for your ML algorithm to function as needed.
- Evaluators must be able to access your data. 

There are no specific requirements regarding the complexity or nature of your data. However, your application must work and fulfill the organizational need you'll outline in the [task 2 documentation](task2doc). Therefore, when choosing your raw data, consider carefully any additional time and effort necessary to prepare that data for use. As these extra steps are only needed in so far as the chosen problem and algorithm need them, you may wish to adjust your project or choose a different data set accordingly.    

You do not need special permission to use any open-source dataset. See our [list](resources:task1:data). Furthermore, data sets used in previous C964 projects are available for reuse (no list of previously used datasets exists). Select data in a format supported by your chosen data analysis library, e.g., the Python library Pandas supports importing CSV. 

(task2c:mlreqs)=
### Machine Learning requirements

- You must apply machine learning to data.

You are encouraged to use ML libraries. Provided the source code is available to evaluators, any language or library of your choosing is allowed. However, we do recommend and can give better support for Python. The [scikit-learn](https://scikit-learn.org/stable/) library is an excellent choice; it is diverse, robust, and has many supplementary resources to help you get started. 

(task2c:visualreqs)=
### Visualization requirements

- You must have three different images helping describe your project. 

The images are typically presented in the application but can also be given in the documentation. The purpose is to help the reader understand your project, but little is required other than the three images being unique and related to your project. The visualizations can describe the data or ML algorithm. They can be the same type describing different data subsets or of different types describing the same data subset. Examples include pie charts, histograms, scatterplots, confusion matrices, etc. 

::::{card-carousel} 4
:::{card}
:class-body: text-center
Scatterplot
```{image} ./url_images/visual_demos/visual12.png
:height: 100
```
:::
:::{card}
:class-body: text-center
Regression Line
```{image} ./url_images/visual_demos/visual0.png
:height: 100
```
:::
:::{card}
:class-body: text-center
Confusion Matrix
```{image} ./url_images/visual_demos/visual1.jpg
:height: 100
```
:::
:::{card}
:class-body: text-center
Histogram
```{image} ./url_images/visual_demos/visual11.png
:height: 100
```
:::
:::{card}
:class-body: text-center
Histograms
```{image} ./url_images/visual_demos/visual5.png
:height: 100
```
:::
:::{card}
:class-body: text-center
Pie-chart
```{image} ./url_images/visual_demos/visual6.png
:height: 100
```
:::
:::{card}
:class-body: text-center
Scatterplot Matrix
```{image} ./url_images/visual_demos/visual7.png
:height: 100
```
:::
:::{card}
:class-body: text-center
Correlation Matrix
```{image} ./url_images/visual_demos/visual13.png
:height: 100
```
:::
:::{card}
:class-body: text-center
Barplot
```{image} ./url_images/visual_demos/visual9.png
:height: 100
```
:::
:::{card}
:class-body: text-center
Barplot
```{image} ./url_images/visual_demos/visual8.png
:height: 100
```
:::
:::{card}
:class-body: text-center
Line plots
```{image} ./url_images/visual_demos/visual10.png
:height: 100
```
:::
:::{card}
:class-body: text-center
Model Explanation
```{image} ./url_images/visual_demos/visual4.png
:height: 100
```
:::
:::{card}
:class-body: text-center
Regression
```{image} ./url_images/visual_demos/visual2.png
:height: 100
```
:::
:::{card}
:class-body: text-center
Clustering
```{image} ./url_images/visual_demos/visual3.png
:height: 100
```
:::
::::

(task2c:uireqs)=
### User interface requirements

- You must provide a user-friendly interface by which the proposed client can use your application to help solve the problem.

Playing the role of the client, the evaluator will follow your [user guide](task2doc:userguide) in the documentation. To meet this requirement they should be able to do the following:

1. **Successfully run your application (user-friendly).** Your application will be considered “user-friendly” if the evaluator successfully executes and uses your application on a Windows 10 machine following your instructions. They can be instructed to download and install necessary dependencies or software.
   
2. **Use your application to solve the proposed problem as intended (interface).** Most often the interface requirement is met by having some way for the user to provide input. For example, a user provides weather conditions, and the app returns a prediction of popsicle sales. How the interface is implemented, whether it be widgets, uploaded data, or simple console input; is up to you.

At a minimum, the user interface must provide a means to apply user-input. Any method by which you can provide instructions is acceptable. For example, 

:::{example}
example hi
:::

> ***...***
> ***Step 10:*** *Next, the user should type the following command into line 57:*
>```python
>mymodel.predict([[temperature, humidity]])
>```
>*in place of 'temperature' and 'humidity', the user should type the temperature in Fahrenheit and humidity as a percentage for which they'd like a prediction, e.g., *
>```python
>mymodel.predict([[75, 24.5]])
>```
>*for a temperature of 75 degrees and humidity of 24.5%. *
>
> ***Step 11*** *Run the code by pressing the 'Run' button in the Jupyter Notebook menu or pressing 'Crtl+Enter' to the left of line 57.*
> ***...***

%%%TODO ADD EXAMPLES

## Coding

Time to get to work. 

````{margin} ...but the requirments won't change.
```{image} ./url_images/good_code.png
:width: 200
```
````

````{warning} 
Following tutorials/examples is a great way to learn. But when it comes to writing your own code, *don't [copy, paste, and **pray**](https://www.youtube.com/watch?v=-wtzy1aqS9Q)*. Instead, understand what it's doing for each line of code and check that it runs as intended. Investing in the extra time will make you a better computer scientist and could save many frustrating hours. 
```{image} ./url_images/code_quality.png
:height: 150
:align: center
```
````

Start *slow*. You must learn and incorporate many small but probably new skills into a large working app -data processing, data analysis, new libraries, and user interface. Learn one new skill, implement it, and check your code before onto to the next step. Things will start slowly and expect to make mistakes, but things can progress quickly after the initial investment. 

**Start small and build up**
A suggested path:

1. Import data and convert it to a (pandas) data frame.
2. Explore the data and create some images. 
3. Determine which ML algorithm to start with and choose a supporting library.
4. Read the library's documentation and understand the expected data format and usage.
5. Apply the algorithm to the data, e.g., train it, and create a model. 
6. Apply the model to new data, e.g., a single input.
7. Create a procedure for the user to apply the model, e.g., provide input.

Add [three images](task2c:visualreqs), and you have a passing part C after step 7. Then, as time allows, you can go back to step 2, improving the performance and presentation of your application until you are satisfied. 

Jupyter notebook is a great place to start for the application's front end. Passing applications often include only the notebook (.ipynb) and data files. Jupyter notebooks are a great way to present code and information together, but you can also progressively develop them into a more polished product. For example, a development path might look like the following:

- Python IDE &rarr; Jupyter notebook (.ipynb) &rarr; notebook with widgets &rarr; hosted notebook with widgets &rarr; web app. 

Provided the [minimal app criteria](task2c:appreqs) are met, submitting at any point along this path will pass part C. You can use whatever language or libraries you like. However, we recommend Python. For ML libraries,  the [scikit-learn](https://scikit-learn.org/stable/) (aka sklearn) is a great choice. In addition to having an extensive collection of ML-specific tools and tutorials, WGU has better faculty support for these. 

(task2c:app-performance)=
## Application Performance

For supervised methods, you should use a metric to measure accuracy and help improve the model. Knowing which algorithm will perform best requires a deep understanding of the data and algorithms. However, using a metric, you can quickly compare and experiment with different approaches -usually by changing a few lines of code. Such experimentation can then lead to understanding. Depending on the method, metrics might similarly be used for unsupervised models. Alternatively (and typically), a development plan for measuring accuracy in the future can be used.

:::{Note}
There is **no** minimal accuracy requirement. Evaluators only assess the appropriateness of the metric (or planned metric).
:::

:::{margin} What is good accuracy?
A good question. The answer is subjective depending on data and project needs. A 5% accuracy in predicting stoplights is not so good. However, it is *very* good if prediction lottery numbers.
:::

Measuring accuracy (or a plan to do so) will be discussed in detail in the [Accuracy Analysis](task2d:accuracy) section of part D of the documentation. 

(task2c:faq)=
## FAQ
**What are the most common reasons for the task 2 code being returned?**

1. Evaluators cannot get the code to run as intended. This usually happens because of an incomplete or incorrect [user guide](task2doc:d) or because evaluators can't access shared links (check the permissions!). 

2. Evaluators are not sure how the code is meant to be used by the "user." Again, an incomplete or incorrect [part D user guide](task2doc:d) is usually the culprit. Adding an explicit example (including example user files when appropriate) helps avoid this issue.

**I've completed the coding for task 2. Should I send it to my course instructor for review?** 

Suppose you have specific questions or concerns -yes. However, if the code runs and meets the [minimum app requirements](task2c:appreqs) it's usually best to move on to the [documentation](task2doc). You can continue to tweak and improve the app but can be comfortable knowing that what you have can pass. 

For questions about whether your application satisfies the requirements, contact a [C964 faculty](ci_c964). 

For technical coding questions, see the [BSCS, Software, and other Course Faculty](ci_other) page, and follow these [guidelines](ci_other:guidelines) (more info below). 

**I need help with part C. Who do I contact?**

That depends on what you need help with. For questions about the capstone, how to meet the requirements, and how to best approach the project to meet your individual goals, contact your [assigned course instructor](ci_c964:cis) or the [capstone team inbox](mailto:ugcapstoneit@wgu.edu?cc=your%20assigned%20CI&subject=C964%20capstone%20question). However, the capstone team supports all of the IT college capstone projects. As such, your assigned course instructor may not have the expertise to answer technical questions related to computer science or coding. Particularly with debugging code, given the wide range of approaches, languages, and libraries available for use.  

For technical questions related to code or math, see the [BSCS, Software, and other Course Faculty](ci_other) page, and follow these [guidelines](ci_other:guidelines). Keep in mind, that while these faculty may be subject matter experts in their field, they do *not* necessarily support the capstone and so may not know the capstone requirements. Hence it is often best to contact your capstone instructor first, so you can appropriately limit the scope of your question(s). When contacting faculty on the[BSCS, Software, and other Course Faculty](ci_other) page, follow these [guidelines](ci_other:guidelines).

Remember, our job (as educators) is to help *you* fix your problem -not just fix it for you. 

%%ALSO IN TASK1
**What if I start working on task 2 and want to change things? Do I need to resubmit task 1?** 

No, not unless it's an entirely different topic. Minor changes from task 1 to task 2 are expected and allowed *without updating the approval form*. Evaluators will not rigorously compare tasks 1 and 2. Task 2 is where the work is, and even with complete topic changes at most, you'll be asked to revise the approval form (if at all). So never let task 1 dictate what you do in task 2.  

**How many attempts are allowed for each task?**

You have *unlimited* attempts for both tasks 1 and 2. However, incomplete submissions or submissions significantly falling short of the minimum requirements may be *locked* from further submissions without instructor approval. Furthermore, such submissions do not receive meaningful evaluator comments. 

**What is a descriptive method?**

Anything that describes the data. Histograms, scatterplots, pie charts -all the familiar descriptive statistics techniques are included. ML methods such as k-means clustering can also be descriptive. Whether a method is descriptive or non-descriptive is determined by its use. For example, using a regression line to describe the relationship between variables is descriptive, but using the line to predict a variable or claim a correlation between the variables exist is inferential (non-descriptive)   

**What is a non-descriptive method?**

Anything that infers from the data, e.g., making predictions, recommendations, identifying correlations, inferring from correlations, etc. Also, see the comments above. 

(task1:faq:whatisml)=
**What is machine learning?**

That depends on who you ask! But for this project, it is an algorithm applied to data. 

For computer science, Machine learning is a subfield of artificial intelligence (a subfield of mathematics), broadly defined as the development of machines capable of self-adjusting behavior based on data. However, from the data science perspective, machine learning is generally defined as using algorithms to identify patterns, make predictions, etc., from data. That is, machine learning is a goal, not a technique. So, for example, a data scientist (and the evaluators) consider linear regression machine learning -when it's used as a prediction model. However, a mathematician would politely (or not so politely) disagree with a 19<sup>th</sup>-century equation being classified as ML.

**Can I use libraries outside the standard (Python, Java, etc.) installation?**

Yes. Unlike C950 (Data Structures & Algorithms II), you are allowed and encouraged to use outside libraries. All the major languages, but particularly Python, have a wide array of highly developed ML tools. The C964 capstone is about applying these tools -not their development.   


**What language, libraries, and platforms should I use?**

You can use whatever you like. However, we recommend using Python and the [scikit-learn](https://scikit-learn.org/stable/) (aka sklearn) library. In addition to having an extensive collection of ML-specific tools and tutorials, WGU has better faculty support for these. Jupyter notebook is a great place to start for the app front end. Passing applications are often submitted as the notebook (.ipynb) and data files. Jupyter notebooks are a great way to present code and information together, but they can also progressively be developed into a more polished product. Students are often tempted to use Jave because of their JavaFX experience in software II, but a GUI is not required, and Python is better suited.

A development path might look like the following:

- Python IDE &rarr; Jupyter notebook &rarr; notebook with widgets &rarr; hosted notebook with widgets &rarr; web app. 

Provided the [minimal app criteria](task2c:appreqs) are met, submitting at any point along this path will pass part C. 

**What sort of user interface do I need? Do I need a GUI?**

No, a GUI is *not* required. Your app must be usable by the "client" to solve the proposed problem. If the evaluators can run your app as intended, playing the role of the "client," following your [user guide](task2_doc:userguide), then your app will be considered to have a user-friendly interface. This can be done through a GUI and widgets, but using the command line or reading user data from a local directory will also suffice.   


%%also in doc FAQ
(task2c:faq:linux)=
**I only have a Linux (or Mac) machine. Will evaluators be able to run my code?"**

Technically (and unfortunately), we are a "Windows" university, and all submitted projects should be able to run in Windows. However, being Windows-compatible is *nowhere specifically required* in the C964 rubric, and doing so would be a little silly for a computer science program. That said, WGU evaluators are only issued Windows 10 machines, and they may have difficulty running a Linux or Mac app without special instructions. Therefore, we recommend that the [user guide](task2_doc:userguide) provide explicit instructions for a Windows 10 user to run your code, such as using a [virtual machine](https://ubuntu.com/tutorials/how-to-run-ubuntu-desktop-on-a-virtual-machine-using-virtualbox#1-overview), remote machine, or using a [Linux subsytem](https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-10#1-overview). You should also provide a note when submitting to Assessments and alerting your course instructor. 