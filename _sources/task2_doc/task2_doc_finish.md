
# Task 2 final touches

(task2_doc_finish:how_to_submit)=

## Submitting Task 2, the document (parts A, B, and D)

1. Use the [Task 2 Template](https://westerngovernorsuniversity-my.sharepoint.com/:w:/g/personal/jim_ashe_wgu_edu/ERGxhsNfkbhEutlkXVFITMQBPOmWlkVx1p5H0UisvnBesg).
2. Check Grammar!!
3. Check adherence to APA formatting, particularly citations. Preserve the formatting of the template and use the MS reference tool, and this shouldn't be a problem.
4. Export parts A, B, and D as a *single* .pdf file.
5. *Always upload the document* separately from the code. It should be easily, identified.

:::{tip}
Preserve the template's section titles, and order, and submit all four parts as a single document (preferably a `.pdf`). With a long, complicated document, aligning content to competencies presents a challenge. Don't make things difficult for the evaluator by spreading the content over several documents in an unfamiliar format.
:::

(task2_doc_finish:how_to_submit_code)=

## Submitting Task 2, the code (part C)

Three things are required:

1. Evaluators can access everything needed to recreate your application. This includes access to data, source files, and all software requirements.
2. For any materials modifiable after submission, e.g., webpage links, hosted notebooks, etc., you must upload the sources files.
3. Uploaded files cannot exceed 200 MB in total.

The second requirement is to ensure there is a static record for the Evaluation team and Assessment's records. But you can still expect evaluators to view links representing the polished finished application. When submitting, consider making it as easy as possible to review your application -webpages and hosted notebooks are a great way to do this and always appreciated by evaluators, and are encouraged -just submit the source files as directed below.

:::{note}
You may receive a warning when submitting .ipynb (Jupyter), Python, or other source files. Submitting these files is permitted, and the warning can be ignored.
:::

### What if all or part of the application is online?

If some or all of your application is online, then you should submit the necessary link(s) AND the minimal source files needed to recreate the project locally. For example,

- If the application is a Jupyter Notebook hosted on Google Colab, submit the Colab link AND the .ipynb and any necessary data files.
- If the application is a webpage, submit the web link AND the necessary .html files.
- If the trained model is stored in a cloud drive, provide the link AND the source code needed to train the model.

It is acceptable to have code import data or submit links provide the source can't be modified, such as links from Kaggle.com. Never use Google Drive, as WGU policy forbids WGU employees from using it. Use of Google Colab is acceptable, but upload the source code as directed above.

### What if the project files exceed 200 MB?

Projects over 200 MB typically result from large datasets or saved models.

#### For large data sets

- If the data source doesn't belong to you, your code can import the data directly (preferred) or instruct the evaluator to download the data.
- You can upload a smaller subset of the data. Your documentation and presentation of the application can still be based on the full dataset.

#### For large saved models

- Check to see if the serialization can be compressed. For example, [`joblib`](https://joblib.readthedocs.io/en/latest/) has a `compress` argument. However, most serialization methods use a relatively compact method by default.
- Upload all the source code and provide instructions for the evaluator to train the model locally. If training are very time or resource consuming, provide a link to download the model for the evaluator's convenience.  

If none of the above work, please contact your course instructor so they can help work out a solution.

## Grammar and Sources

(task2_doc_finish:grammar)=

### Grammar

:::{warning}
Grammar and sources are the *most common* reason for returned submissions! Even minor grammatical errors can prevent a submission from passing.
:::

After focusing on the content, check your grammar using [Grammarly.com](https://www.grammarly.com/) ![grmmarly](https://github.com/ashejim/C769/blob/main/url_images/icon-grammarly.png?raw=true#icon) (it's what the evaluators use). Style is not assessed (blue and green), but even a few grammar mistakes will prevent competency in *Professional Communication*. The free side has been sufficient, but if using the online app, you sometimes need to wait before mistakes are caught. 


:::{warning}
Students have reported missed mistakes when using the Google doc Grammarly extension. Therefore, we advise that you copy and paste it into the online app or purchase the premium version for MS Word. 
:::

(task2_doc_finish:sources)=

### Sources

For sources, you should follow [APA guidelines](https://apastyle.apa.org/style-grammar-guidelines). Avoid errors by using the [MS Word Reference Tool](https://support.microsoft.com/en-us/office/create-a-bibliography-citations-and-references-17686589-4824-4940-9c69-342c289fa2a5) to create and manage references.

- No references are required.
- All sources on the reference page must have a matching in-text citation, e.g., (Author, year)
- To cite sources used for code, you should include the referfences as code comments within the source code.
