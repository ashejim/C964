# Task 2 Part D

(task2_doc_d)=

Part D of the documentation explains the technical details of your project and should target the computer science subject matter experts. Hence, of the documentation, part D is most valued and scrutinized by the evaluators. Of part D, the [User Guide](task2d:userguide), [Machine Learning](task2d:ml), and [Validation](task2d:validation) sections are the most important. As such, we recommend completing these sections first. Follow the [Task 2 Template](https://westerngovernorsuniversity-my.sharepoint.com/:w:/g/personal/jim_ashe_wgu_edu/ERGxhsNfkbhEutlkXVFITMQBPOmWlkVx1p5H0UisvnBesg).

(task2_doc_d:user_guide)=

## User Guide

The evaluator might go here first. Following your instructions, they will verify your app functions as intended and simultaneously gain context of its purpose through demonstration. 

Include an enumerated (steps 1, 2, 3, etc.) guide on how to execute and use your application. The evaluator will play the "client" role and follow your instructions as provided. So you should include instructions for downloading and installing any necessary software or libraries (they'll have most of these installed anyway). Your application will be considered “user-friendly” if the evaluator successfully executes and uses your application on a Windows 10 machine following your instructions.

- **Provide examples.** Examples not only make the instructions easier to follow (hence easier to pass) but also demonstrate how the app solves the organizational need. When applicable provide sample input or input which can be copied and pasted.

- **Provide visual aides.** Screenshots or even a Panotpo video would all be great ways in aiding the evaluator's understanding of your project.

- **Test.** Create a new environment or borrow a friend's computer, follow your instructions verbatim, and verify that everything works as expected. It's easy to overlook small details.

:::{margin} No Windows machine?
*Nowhere is Windows specifically required* in the C964 rubric. However, WGU evaluators are issued Windows 10 machines, and they may have difficulty running a Linux or Mac app without special instructions. Therefore, we recommend that the [User Guide](task2_doc:userguide) provide explicit instructions for a Windows 10 user to run your code, such as using a [virtual machine](https://ubuntu.com/tutorials/how-to-run-ubuntu-desktop-on-a-virtual-machine-using-virtualbox#1-overview), remote machine, or using a [Linux subsystem](https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-10#1-overview). You should also provide a note when submitting to Assessments and alerting your course instructor. See the [Task 2 part C FAQ](task2c:faq:linux) for more details.

(task2_doc_d:user_guide:examples)=

:::

::::{card-carousel} 4
:::{card}

```{image} ../url_images/user_guide/user_guide1.png
:height: 100
:alt: Screenshot of a user guide from a sample task 2 dcoumentation.
```

:::
:::{card}

```{image} ../url_images/user_guide/user_guide2.png
:height: 100
:alt: Screenshot of a user guide from a sample task 2 dcoumentation.
```

:::
:::{card}

```{image} ../url_images/user_guide/user_guide3.png
:height: 100
:alt: Screenshot of a user guide from a sample task 2 dcoumentation.
```

:::
:::{card}

```{image} ../url_images/user_guide/user_guide4.png
:height: 100
:alt: Screenshot of a user guide from a sample task 2 dcoumentation.
```

:::
:::{card}

```{image} ../url_images/user_guide/user_guide5.png
:height: 100
:alt: Screenshot of a user guide from a sample task 2 dcoumentation.
```
:::

::::

(task2_doc_d:ml)=

## Machine Learning

This section should describe the development of your ML application justifying and explaining decisions made in the process. Explain the *what*, *how*, and *why* of the machine learning model and its application.

- *What?* Outline what your product does and then explain in detail what machine learning does in solving the proposed problem. Describe the algorithms, libraries, and other tools used to develop the machine learning model.

- *How?* Outline your application's implementation plan and then explain in detail how the machine learning portion was developed (or trained) and improved. 

- *Why?* Thoroughly justify development decisions. Address your algorithm(s) as a  good choice, why your training process was appropriate, etc.  

(task2_doc_d:validation)=

## Validation

In this section, discuss how you assessed the accuracy or success of the ML application(s). In most cases, this means providing an appropriate *metric* for assessing accuracy OR providing a development plan for obtaining such a metric in the future. Most libraries have builtins for this; see [sklearn metrics](https://scikit-learn.org/stable/modules/model_evaluation.html).

:::{Note}
There is **no** minimal accuracy requirement. At most, evaluators will assess the appropriateness of the metric (or planned metric).
:::

(task2d:accuracy:super)=

### For Supervised Classification Methods

The metric for measuring a supervised classification model's accuracy is straightforward. We use [the ratio of correct to total predictions](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score):

$$\text{Accuracy}=\frac{\text{correct predictions}}{\text{total predictions}}$$

Though no minimal accuracy is required, your model should perform better than randomly selecting categories, e.g., the model predicting 1 of 3 flower types should perform better than $\frac{1}{3} = 33.3\bar{3}\%$.

### For Supervised Regression Methods

As regression models estimate continuous values, they rarely exactly match actual values. Thus success of the model is measured by how closely the model fits the data. Common metrics include mean square error (MSE), mean absolute error (MAE), and mean absolute percentage error (MAPE). Statistical metrics such as the correlation coefficient or (more commonly) the coefficient of determination, $R^{2}$, can be used. See [sklearn's regression metric documentation](https://scikit-learn.org/stable/modules/model_evaluation.html#regression-metrics). As above there is no performance benchmark, but the model should at predict at least as well as thaking the mean.

### For Reinforced Learning Methods

Reinforced learning methods seek to optimize an outcome, e.g., the C950 delivery app seeks to minimize miles driven. The better this outcome, the better your algorithm.

## Solution Summary

Summarize the problem and solution. Describe how the application (Part C) supports a solution to the problem presented in parts A and B.

## Data Summary

Provide the source of the rwa data, how the data was collected, or how it was simulated. Include a description of how data was processed and managed throughtout the application development life cycle: design, development, maintenance, or others.

## Visualizations

Identify the location of at least three unique imgaes in part C. Part or all of those images can also be included in this section. Tehcnically, the visualizations are required to be part of the application. However, often this is not desirable, say when the app is intended to customer facing. So it is allowable to submit the code provindg the visualization separate from the main application code. Recall, images can be generated by the code or inserted as static images.
