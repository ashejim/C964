# Task 2: Part C -the application

(task2_part_c)=

Your software application (the "app") is the entirety of part C of task 2. However, the Computer Science capstone is *not* a software project. Other than requiring you to apply machine learning (ML) to data, they will only assess *what* your application does -not its presentation.

```{margin} **What is an *application*?**
An application (app) is simply software that performs specific tasks. 
```

:::{warning}
*The rubric is currently under development.* Written holistically, many find the rubric difficult to understand. We recommend first referring to the guidelines on this webpage and the [Task 2 template](https://westerngovernorsuniversity-my.sharepoint.com/:w:/g/personal/jim_ashe_wgu_edu/ERGxhsNfkbhEutlkXVFITMQBPOmWlkVx1p5H0UisvnBesg?rtime=3q_Efs-u2kg).
:::

(task2_part_c:what_does_the_application_need_to_do)=

## What does the application need to do?

<!-- example of link with help of Marksman ext. edited to add rel path (..) and html (.md links dont get translated by JB apparently): 
This is [choosing a topic test](../task1.html#choosing-a-topic) 
However, link mapping seems inconsistent for ipynb. It looks to map below, not at, the md cell. 
-->

(task2_part_c:what_does_the_application_need_to_do)=

Your app must help the user solve the organizational problem from [task 1](task1) by doing the following:  

1. **Data → ML model:** Use data to develop a machine learning model.

2. **Accuracy Metric:** Provide an appropriate metric or plan for measuring the app's accuracy.

3. **Visualizations:** Present 3 different pictures; can be presented in the app or document.

4. **User Application:** Provide a way for the "user" to use the ML model towards solving the problem.

<!--tab-item examples -->
`````{tab-set}
````{tab-item} Example 1
**The App:** A standalone [Jupyter Notebook](https://jupyter.org) file (.ipynb) which can predict Iris types (see the [example](./example_sup_class/sup_class_ex.html#example-supervised-classification-app)).
>**Data → ML model:** Labeled [Iris petal dimensions](https://www.kaggle.com/datasets/uciml/iris) train an [SVM classification model](sup_class_ex:develop).
>
> **Accuracy Metric:** Percent of correct predictions on [testing data](sup_class_ex:accuracy).   
>
> **Visualizations:** [Histograms](sup_class_ex:descriptive_methods_and_visualizations) showing distributions of different flower features and a [confusion matrix](sup_class_ex:accuracy:confusion_matrix) illustrating the accuracy of the classification model.
>  
> **User interface:** (New data → ML model → prediction) Following detailed instructions, the user can [input flower dimensions](sup_class_ex:ui:code), run code in the Jupyter notebook, and the app returns a prediction helping customers identify their flowers.
````

````{tab-item} Example 2
**The App:** A standalone Pycharm (Python) project predicting house prices.
>
> **Data → ML model:** Labeled housing data trains a multi-linear regression model to predict house prices.
> 
> **Accuracy Metric:** [Mean squared error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#examples-using-sklearn-metrics-mean-squared-error) of the model on testing data.
>
> **Visualizations:** Histograms showing distributions of data features and scatterplots demonstrating data correlations. 
>
> **User interface:** (New data → ML model → prediction) Via console the user can input unseen house data, and the model predicts a house's price helping a realty firm make investment decisions.
````

````{tab-item} Example 3
**The App:** A web app (developed with [Juptyer, voila, and deployed on Heroku](https://pythonforundergradengineers.com/deploy-jupyter-notebook-voila-heroku.html) recommending movies.
> **Data → ML model:** Using movie data, data is [vectorized](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html) so that [Cosine similarity](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html) can provide similarity scores between any two movies. 
>
> **Accuracy Metric:** [Cosine simliarity score](https://scikit-learn.org/stable/modules/metrics.html#cosine-similarity) on test data, or a plan to measure the app's acccuracy based on future user feedback,
>
> **Visualizations:** Histograms showing distributions of movie features and samples of Cosine Similarity matrices.  
> 
> **User interface:** (New data → ML model → prediction) Using a user-provided movie, the web app returns five recommendations for a user typed movie helping customers find movies to watch. See this [movie recommendation example](https://github.com/Prajwal10031999/Movie-Recommendation-System-Using-Cosine-Similarity)
````

````{tab-item} Example 4
**The App:** A hosted Jupyter notebook identifies images as a cat or dog.  
> **Data → ML model:** Labeled images are used to [train a neural network model to classify images](https://www.tensorflow.org/tutorials/images/classification) of dogs and cats.
>
> **Accuracy Metric:** Percent of correct predictions on testing data.  
>
> **Visualizations:** Graphs of training and validation accuracy and loss, a confusion matrix showing model accuracy, and image examples.
>
> **User interface:** (New data → ML model → prediction) Following detailed instructions, the users upload an image to Jupyter notebook folder deployed on [Datalore](https://datalore.jetbrains.com), and run the app classifying the image as cat or dog.
````
`````

(task2c:data_requirements)=

### Data requirements

- Your data must be sufficiently complex and processed for your ML algorithm to function as needed.
- Evaluators must be able to access your data.

There are no specific requirements regarding the complexity or nature of your data. However, your application must work and fulfill the organizational need you'll outline in the [task 2 documentation](task2_doc). Therefore, when choosing your raw data, consider carefully any additional time and effort necessary to prepare that data for use. As these extra steps are only needed in so far as the chosen problem and algorithm need them, you may wish to adjust your project or choose a different data set accordingly.

You do not need special permission to use any open-source dataset (see our [list](resources:task1:data)). Furthermore, data sets used in previous C964 projects are available for reuse (no list of previously used datasets exists).

(task2_part_c:mlreqs)=

### Machine Learning requirements

- You must apply machine learning to data.

You are encouraged to use ML libraries. Provided the source code is available to evaluators, any language or library of your choosing is allowed. However, we do recommend and can give better support for Python. The [scikit-learn](https://scikit-learn.org/stable/) library is an excellent choice; it is diverse, robust, and has many supplementary resources to help you get started.

(task2c:visualreqs)=

### Visualization requirements

- You must have three different images helping describe your project.

The images are typically presented in the application but can also be given in the documentation. The purpose is to help the reader understand your project, but little is required other than the three images being unique and related to your project. The visualizations can describe the data or ML algorithm. They can be the same type describing different data subsets or of different types describing the same data. Examples include pie charts, histograms, scatterplots, confusion matrices, etc.

<!-- card carousel of example visualizations -->
::::{card-carousel} 4
:::{card}
:class-body: text-center
Scatterplot

```{image} ../url_images/visual_demos/visual12.png
:height: 100
:alt: Example image of a scatterplot. 
```

:::
:::{card}
:class-body: text-center
Regression Line

```{image} ../url_images/visual_demos/visual0.png
:height: 100
:alt: Example image of a regression line.
```

:::
:::{card}
:class-body: text-center
Confusion Matrix

```{image} ../url_images/visual_demos/visual1.jpg
:height: 100
:alt: Example image of a confusion matrix. 
```

:::
:::{card}
:class-body: text-center
Histogram

```{image} ../url_images/visual_demos/visual11.png
:height: 100
:alt: Example image of a histogram
```

:::
:::{card}
:class-body: text-center
Histograms

```{image} ../url_images/visual_demos/visual5.png
:height: 100
:alt: Example image of a grid of four histgrams.
```

:::
:::{card}
:class-body: text-center
Pie-chart

```{image} ../url_images/visual_demos/visual6.png
:height: 100
:alt: Example image of a pie-chart.
```

:::
:::{card}
:class-body: text-center
Scatterplot Matrix

```{image} ../url_images/visual_demos/visual7.png
:height: 100
:alt: Example image of a scatterplot matrix.
```

:::
:::{card}
:class-body: text-center
Correlation Matrix

```{image} ../url_images/visual_demos/visual13.png
:height: 100
:alt: Example image of a correlation matrix.
```

:::
:::{card}
:class-body: text-center
Barplot

```{image} ../url_images/visual_demos/visual9.png
:height: 100
:alt: Example image of a horizontal barplot. 
```

:::
:::{card}
:class-body: text-center
Barplot

```{image} ../url_images/visual_demos/visual8.png
:height: 100
:alt: Example image of a vertical barplot. 
```

:::
:::{card}
:class-body: text-center
Line plots

```{image} ../url_images/visual_demos/visual10.png
:height: 100
:alt: Example image of line plots.
```

:::
:::{card}
:class-body: text-center
Model Explanation

```{image} ../url_images/visual_demos/visual4.png
:height: 100
:alt: Example image of decision tree model explanation. 
```

:::
:::{card}
:class-body: text-center
Regression

```{image} ../url_images/visual_demos/visual2.png
:height: 100
:alt: Example image of a 2-D non-linear regression model with margin of error.
```

:::
:::{card}
:class-body: text-center
Clustering

```{image} ../url_images/visual_demos/visual3.png
:height: 100
:alt: Example image of 3-D clustering.
```

:::
::::

(task2c:user_interface_requirements)=

### User interface requirements

- You must provide a user-friendly interface by which the proposed client can use your application to help solve the problem.

Playing the role of the client, the evaluator will follow your [user guide](task2_doc_d:user_guide) in part D of the documentation. To meet this requirement they should be able to do the following:

1. **Run your application (user-friendly).** Your application will be considered “user-friendly” if the evaluator successfully executes and uses your application on a Windows 10 machine following your instructions. They can be instructed to download and install necessary dependencies or software.

2. **Use your application to solve the proposed problem as intended (interface).** Most often the interface requirement is met by having some way for the user to provide input and receive output. For example, a user provides weather conditions, and the app returns a prediction of popsicle sales. How the interface is implemented, whether it be widgets, uploaded data, or simple console input; is up to you.

At a minimum, the interface must provide means for the user to provide input and receive feedback. Any method by which you can provide instructions is acceptable. For example:

> ***...***
> ***Step 10:*** *Next, the user should type the following command into line 57:*
>
>```python
>mymodel.predict([[temperature, humidity]])
>```
>
>*in place of 'temperature' and 'humidity', the user should type the temperature in Fahrenheit and humidity as a percentage for which they'd like a prediction, e.g.,*
>
>```python
>mymodel.predict([[75, 24.5]])
>```
>
>*for a temperature of 75 degrees and humidity of 24.5%.*
>
> ***Step 11*** *Run the code by pressing the 'Run' button in the Jupyter Notebook menu or pressing 'Crtl+Enter' to the left of block 57.*
> ***...***

See the individual [example user guides](task2_doc_d:user_guide:examples) and guides provided in the completed [task 2 document examples](task2_doc:examples).

<!-- continue revisions here -->

(task2_part_c:coding)=

## Coding

Time to get to work.

<!-- &nbsp; fixes odd spacing issue -->
````{margin} Good Code &nbsp;

```{image} ../url_images/good_code.png
:width: 200
:alt: XKCD comic. Flowchart on how to write good code.
```
{cite}`xkcdCodeFlowChart`

````

````{warning}
Following tutorials/examples is a great way to learn. But when it comes to writing your own code, *don't [copy, paste, and **pray**](https://www.youtube.com/watch?v=-wtzy1aqS9Q)*. Instead, understand what it's doing for each line of code and check that it runs as intended. Investing in the extra time will make you a better computer scientist and could save many frustrating hours. 

```{figure} ../url_images/code_quality.png
:height: 150
:align: center
:alt: XKCD comic about writing code with poor style and structure.

**Code Quality** {cite}`xkcdCodeQuality` 

```

````

Start *slow*. You must learn and incorporate many small but probably new skills into a large working app -data processing, data analysis, new libraries, and user interface. Learn one new skill, implement it, and check your code before onto to the next step. Things will start slowly and expect to make mistakes, but things can progress quickly after the initial investment.

### Start small and build up

:::{sidebar} Simple coding example
<iframe 
    src="https://wgu.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=ae4e4987-3196-4b67-9752-ae010137b64c&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=true&interactivity=all"
    title="Simple ML supervised classification example "
    alt= "Simple ML supervised classification coding python example by Dr. Jim Ashe."
    style="border: 1px solid #464646;"
    class="center"
    allowfullscreen allow="autoplay"
>
</iframe>
:::

A suggested path:

1. Import data and convert it to a data frame (using [Pandas](https://pandas.pydata.org/pandas-docs/stable)).
2. Explore the data and create some images.
3. Determine which ML algorithm to start with and choose a supporting library.
4. Read the library's documentation and understand the expected data format and usage.
5. Apply the algorithm to the data, e.g., train it, and create a model. 
6. Apply the model to new data, e.g., a single input.
7. Create a procedure for the user to apply the model, e.g., provide input.

Add [three images](sup_class_ex:descriptive_methods_and_visualizations), and you have a passing part C after step 7. Then, as time allows, you can go back to step 2, improving the performance and presentation of your application until you are satisfied.

Jupyter Notebook is a great choice for the application's development **and** front end. Passing applications often include only the Notebook (.ipynb) and data files. Jupyter Notebooks are a great way to present code and information together. Moreover, they can also be progressively developed into a more polished product. For example, a development path might look like the following:

- Python IDE → Jupyter Notebook → notebook with widgets → hosted notebook with widgets → web app.

Provided the [minimal app criteria](task2_part_c:what_does_the_application_need_to_do) are met, submitting any point along this path will pass part C. You can use whatever language or libraries you like. However, we recommend Python. For ML libraries,  the [scikit-learn](https://scikit-learn.org/stable/) (aka sklearn) is a great choice. In addition to having an extensive collection of ML-specific tools and tutorials, WGU has better faculty support available for it.

(task2_part_c:application_performance)=

## Application Performance

For supervised methods, you should use a metric to measure accuracy and help improve the model. Knowing which algorithm will perform best requires an understanding of the data and algorithms. However, using a metric, you can quickly compare and experiment with different approaches -usually by changing a few lines of code. Such experimentation can then lead to understanding. Depending on the method, metrics might similarly be used for unsupervised models, such as Silhouette[ coefficients](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_silhouette_analysis.html) for KMeans clustering. Alternatively (and typically), a future development plan for measuring the accuracy of your unsupervised method can be used.

:::{margin} What is good accuracy?
A good question. The answer subjectively depends on the data and project needs. A 5% accuracy in predicting stoplights is not so good. However, it is *very* good if predicting lottery numbers.
:::

:::{Note}
There is **no** minimal accuracy requirement. At most, evaluators will assess the appropriateness of the metric (or planned metric).
:::

Measuring accuracy (or a plan to do so) will be discussed in detail in the [Accuracy Analysis](task2_doc_d:accuracy_analysis) section of part D of your documentation.

(task2c:faq)=

## FAQ

### What are the most common reasons for task 2 part C (the app/code) being returned?

1. Evaluators cannot get the code to run as intended. This usually happens because of an incomplete or incorrect [User Guide](task2_doc_d:user_guide) or because evaluators can't access shared links (check the permissions!).

2. Evaluators are not sure how the code is meant to be used by the "user." Again, an incomplete or incorrect [User Guide](task2_doc_d:user_guide) is usually the culprit. Adding an explicit example (including example user files when appropriate) helps avoid this issue.

### I've completed the coding for task 2. Should I send it to my course instructor for review?

If you have specific questions or concerns -yes. However, if the code runs and meets the [minimum app requirements](task2_part_c:what_does_the_application_need_to_do) it's usually best to move on to the [documentation](task2_doc). You can continue to tweak and improve the app but can be comfortable knowing that what you have can pass. Recall, you have **unlimited** submissions. So for both the code and documentation, it's usually best to submit it as soon as it's ready and restrict revisions according to the evaluator's feedback.  

For getting help with task 2 part C, see the advice [below](task2_part_c:faq:i_need_help_with_part_C_who_do_i_contact).

(task2_part_c:faq:i_need_help_with_part_C_who_do_i_contact)=

### I need help with part C. Who do I contact?

That depends on what you need help with. For questions about the capstone, how to meet the requirements, evaluator comments, or how to best approach the project to meet your individual goals, contact your [assigned course instructor](ci_c964) or the [capstone team inbox](mailto:ugcapstoneit@wgu.edu?cc=your%20assigned%20CI&subject=C964%20capstone%20question) (this inbox supports all IT capstones). However, the capstone team supports all of the IT college capstone projects. As such, your assigned course instructor may not have the technical expertise to answer questions related to computer science or coding. Particularly with debugging code, given the wide range of approaches, languages, and libraries available for use.  

For technical questions related to code or math, see the [BSCS, Software, and other Course Faculty](ci_other) page, and follow these [guidelines](ci_other:better_questions_get_better_answers). Keep in mind, that while these faculty may be subject matter experts in their field, they do *not* necessarily support the capstone and so may not know the capstone requirements. Hence it is often best to contact your capstone instructor first, so you can appropriately limit the scope of your question(s). When contacting faculty on the [BSCS, Software, and other Course Faculty](ci_other) page, follow these [guidelines](ci_other:better_questions_get_better_answers). Keep in mind, that non-capstone faculty love to help **but do so as a generosity.** Their  priority is the students struggling in their supporting courses.

Remember, our job (as educators) is to help *you* fix your problem -not fix it for you.

(task2_part_C:faq:what_if_i_start_working_on_task_2 and_want to change things)=

### What if I start working on task 2 and want to change things? Do I need to resubmit task 1?

No, not unless it's an entirely different topic. Minor changes from task 1 to task 2 are expected and allowed *without updating the approval form*. Evaluators will not rigorously compare tasks 1 and 2 (if at all). Task 2 is where the work is, and even with complete topic changes, at most, you'll only be asked to revise the approval form (if at all). So never let task 1 dictate what you do in task 2.  

### How many attempts are allowed for each task?

You have *unlimited* attempts for both tasks 1 and 2. However, incomplete submissions or submissions significantly falling short of the minimum requirements may be *locked* from further submissions without instructor approval. Furthermore, such submissions do not receive meaningful evaluator comments.

### What is a descriptive method?

Anything that describes the data. Histograms, scatterplots, pie charts -all the familiar descriptive statistics techniques are included. ML methods such as k-means clustering can also be descriptive. Whether a method is descriptive or non-descriptive is determined by its use. For example, using a regression line to describe the relationship between variables is descriptive, but using the line to predict a variable or claim a correlation between the variables exist is inferential (non-descriptive).

For task 2, you do not need to explicitly identify descriptive and non-descriptive methods. In almost all cases, the visualizations will satisfy the former and the user interface the latter.

### What is a non-descriptive method?

Anything that infers from the data, e.g., making predictions, recommendations, identifying correlations, inferring from correlations, etc. Also, see the comments above.

(task1:faq:what_is_machine_learning?)=

### What is machine learning?

That depends on who you ask! But for this project, it is an algorithm applied to data.

For computer science, Machine learning is a subfield of artificial intelligence (a subfield of mathematics), broadly defined as the development of machines capable of self-adjusting behavior based on data. However, from the data science perspective, machine learning is generally defined as using algorithms to identify patterns, make predictions, etc., from data. That is, machine learning is a goal, not a technique. So, for example, a data scientist (and the evaluators) consider linear regression machine learning -when it's used as a prediction model. However, a mathematician would politely (or not so politely) disagree with a 19<sup>th</sup>-century equation being classified as ML.

### Can I use libraries outside the standard (Python, Java, etc.) installation?

Yes! Unlike C950 (Data Structures & Algorithms II), you are allowed and encouraged to use outside libraries. All the major languages, but particularly Python, have a wide array of highly developed ML tools. The C964 capstone is about applying these tools -not their development.

### What language, libraries, and platforms should I use?

You can use whatever you like. However, we strongly recommend Python and the [scikit-learn](https://scikit-learn.org/stable/) (aka sklearn) library. In addition to having an extensive collection of ML-specific tools and tutorials, WGU has better faculty support for these. Jupyter Notebook (a browser-based IDE designed for this type of project) is a great place to start for the app's development and front end. Passing applications are often submitted as the Notebook (.ipynb) and data files. Jupyter Notebooks are a great way to present code and information together, but they can also progressively be developed into a more polished product. Students are often tempted to use Jave because of their JavaFX experience in software II, but a GUI is not required, and Python is better suited.

A development path might look like the following:

- Python IDE → Jupyter Notebook → notebook with widgets → hosted notebook with widgets → web app.

Provided the [minimal app criteria](task2_part_c:what_does_the_application_need_to_do) are met, submitting at any point along this path will pass part C.

### What sort of user interface do I need? Do I need a GUI?

No, a GUI is *not* required. Your app must be usable by the "client" to solve the proposed problem. If the evaluators can run your app as intended, playing the role of the "client," following your [user guide](task2_doc_d:user_guide), then your app will be considered to have a user-friendly interface. This can be done through a GUI and widgets, but using the command line or reading user data from a local directory will also suffice.

<!-- TODO add to task D or polish up? -->
(task2_part_c:faq:my_project_exceeds_the_200_mb_limit)=

### My project exceeds the 200 MB limit. How can I submit it?

As you might guess, this is a common issue. But evaluators only need *access* to everything necessary to develop and run your project. Access to large files can be provided with a cloud link (say your Google Drive) -don't forget to set the share settings so they can access it!

<!-- %%also in doc FAQ -->
(task2_part_c:faq:i_only_have_a_linux_or_mac_machine)=

### I only have a Linux (or Mac) machine. Will evaluators be able to run my code?

Technically (and unfortunately), we are a "Windows" university, and all submitted projects should be able to run in Windows. However, being Windows-compatible is *nowhere specifically required* in the C964 rubric, and doing so would be a little silly for a computer science program. That said, WGU evaluators are only issued Windows 10 machines, and they may have difficulty running a Linux or Mac app without special instructions. Therefore, we recommend that your [user guide](task2_doc_d:user_guide) provide explicit instructions for a Windows 10 user to run your code, such as using a [virtual machine](https://ubuntu.com/tutorials/how-to-run-ubuntu-desktop-on-a-virtual-machine-using-virtualbox#1-overview), a remote machine, or using a [Linux subsystem](https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-10#1-overview). Provide a note when submitting to Assessments and alert your course instructor.

### How complex does my data, algorithm, or model need to be?

It must be complex enough to meet the needs of your project. There is no explicit minimal complexity for any of these items. However, the model must meet the needs of the "organizational need" and the data must be appropriate for developing the model which could indirectly impose a minimal complexity. For example, a supervised model requires two variables.

### Are there any restrictions on which datasets I can choose?

Only that data must be legally available to use and share with evaluators. For example, using data belonging to a current employer would require submitting a [waiver form](task1:waiverform).

- You *can* use any dataset found on [kaggle.com](https://www.kaggle.com/datasets).
- You *can* use simulated data.
- You *can* use data used for previous projects (submitted by you or others).
- You only need to apply for [IRB review](https://cm.wgu.edu/t5/Frequently-Asked-Questions/WGU-IRB-and-Human-Subject-Protections-FAQ/ta-p/2002) if you are *collecting* data involving human participants (this is very rare). Otherwise, your project is in IRB compliance.  

### Can I use my C950 project for C964?

Yes. You can use any of your own academic or professional work for C964 including the C950 project (Data Structures & Algorithms II). Though the document (Task 2 parts A, B, and D) will need some adjustment, the coding portion of C950 almost meets all the requirements of the C964 application (Task 2 part C). Referring to the [Task 2 part C page](https://ashejim.github.io/C964/task2_c/task2_part_c.html#what-does-the-application-need-to-do), the C964 application needs the following:

1. **Data → ML model:** C950 applies a reinforced learning algorithm to the distance and package data.

2. **Accuracy Metric:** The total miles. The maximum allowed miles for C950 is 120, which WGU Assessment Department has already determined to be "efficient."

3. **Visualizations:** This will need to be added, but any three pictures will meet the requirements.

4. **User Application:** The require console user interface required for C950 allows the user to provide input and apply the algorithm toward solving the problem.

So only the three images will need to be added. Furthermore, you are free to adjust the distance and package data as desired. For example, dropping some of the delivery restrictions requiring different trucks or certain packages to be delivered together, and will be easier to apply a more sophisticated algorithm. Say a [Monte Carlo method](https://en.wikipedia.org/wiki/Monte_Carlo_method) such as [Simulated Annealing](https://en.wikipedia.org/wiki/Simulated_annealing).

<img src="./_images/simulated_annealing.gif" height="150px" alt = "A short animated image demonstraiting simulated annealing applied to a two dimensional travleing salesperson problem. Points on a plane are connected via lines creating a circular path. The movie shows the algorithm interatively finds shorter paths. Each iteration improves less, until the algorihtm stops at a final path." />

{cite}`WikiTSPimage`

### Can I use my C951 task 1 or 2 for C964?

Yes. You can use any of your own academic or professional work for C964 including the C950 project (Data Structures & Algorithms II). However, C951 Tasks 1 (chatbot) and 2 (rescue robot) can be passed without applying a mathematically based algorithm which is necessary to pass C964 (no C951 task requires AI). While chatbots are often trained and improved with ML/AI methods, it's difficult to acquire sufficient user data within students' typical timeframe. An algorithm is easier to employ in C951 Task 2, but the application would be limited to the [CoppeliaSim](https://www.coppeliarobotics.com/coppeliaSim) simulation software which may make meeting the user application requirements of C964 difficult. Furthermore, [CoppeliaSim](https://www.coppeliarobotics.com/coppeliaSim)'s dependency on Lua makes the application of ML libraries problematic. For these reasons and others, we do not recommend using either of these projects for C964 -unless the C951 projects far exceed their requirements and meet the C964 requirements as is.

### Can I use my C951 task 3? Should I use it?

You can reuse anything you've of your own academic or professional work, including copying verbatim from C951 task 3. If it's convenient, feel free to do it. But at best, the time saved is little. At worst, you might get bogged down trying to work on two projects simultaneously and going with an unnecessarily complex C964 topic. If you have time, consider completing C964 first, as parts A and B of task 2 can always be used verbatim for task 3 of C951.

Here are some points to consider:

- C951.3 is just a written project, typically around five pages (I'm guessing; ask your C951 instructor), and can be completed in a single afternoon. Comparatively, C964 requires a working machine learning application and accompanying documentation, typically around 20 pages.
- C951.3 only relates to parts A and B of C964.2. These parts are just a framework for providing a general audience and purpose for the ML application. If present, these parts almost always pass. Furthermore, they'll have to be at least partially rewritten anyways. Parts C and D of C964 are what evaluators care about, but C951.3 has no corresponding parts C and D.
- Rewriting C951.3 content for a different C964 topic takes little additional work.
- As it's just a written project, students often pick a complex topic for C951.3. But then they feel pressured to use the same complex topic for C964 and struggle with creating the app.
- Trying to comprehend two projects at once is just more difficult. 

Whatever you do for C964 can meet the requirements of C951 task 3. If you have plenty of time, completing C964 first might be the best option.

### Help, the rubric is confusing! The directions seem to require items outside the scope of the project, e.g., "implementation of interactive queries." The directions have parts A, B, C, and D, but the rubric has "Outcomes" 1-6. How do these align?

*We do not advise directly following the official rubric for C964* (it is under development). Follow the guidelines found on this webpage and the [Task 2 template](https://westerngovernorsuniversity-my.sharepoint.com/:w:/g/personal/jim_ashe_wgu_edu/ESLuMNRuDjpCrKvqWaC6cywB4I97WEPdk5MRZRq4LfmFhQ). Because of the ambiguity of the official rubric (how do directions A-D align with Outcomes 1-6?), following this template is helpful (almost necessary) in aligning your documentation with the rubric outcomes. So while following the template format is not technically required, it is highly recommended.

Preserve the template's section titles, and order, and submit all four parts as a single document (preferably a pdf). With a long, complicated document, aligning content to competencies presents a challenge. Don't make things difficult for the evaluator by spreading the content over several documents in an unfamiliar format.

## Questions, comments, or suggestions?

<script
   type="text/javascript"
   src="https://utteranc.es/client.js"
   async="async"
   repo="ashejim/C964"
   issue-term="pathname"
   theme="github-light"
   label="💬 comment"
   crossorigin="anonymous"
/>