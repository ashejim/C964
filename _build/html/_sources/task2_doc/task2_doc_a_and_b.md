
(task2ab)=

# Task 2 parts A and B

The purpose of parts A and B is to demonstrate competency in communicating your technical solution to different less technical audiences. Follow the [Task 2 Template](../resources/C964_task_2_template.docx).

- Part A - Convince senior leadership to approve your project.
- Part B - Implementation plan for IT leadership (but not CS experts) or middle management.

Part D, explains the CS-related aspects of your project. With the exception of the [User Guide](task2d:userguide), all sections should target the computer science subject-matter experts. This is *not* a business project, and neither does the rubric have any qualitative business criteria for parts A and B. As such, parts A and B aspects such as budgets, methodology, and planning parts are not assessed rigorously from a business perspective.


(task2:parta)=

## Part A: Letter of Transmittal

Write a letter convincing senior leadership to approve your project -a brief cover letter (suggested length 1-2 pages) describing the problem, how the application (part C) applies to the problem, the practical benefits to the organization, and a brief implementation plan. Include all artifacts typical of a professional (business) letter, e.g., subject line, date, greeting, signature, etc. **Write everything in the future tense.**

The letter should be concise and target a non-technical audience. Include the following:

- A summary of the problem.
- A proposed solution centering around your application.
- How the proposed solution benefits the organization.
- A summary of the costs, timeline, data, and any ethical concerns (if relevant).
- Your relevant expertise.

## Part B: Project Proposal

The project proposal should target your client’s IT leadership or middle management. This audience may be IT professionals but have limited computer science expertise. Use appropriate industry jargon and sufficient technical details to describe the proposed project and its application. Remember, you’re establishing the technical context for your project and how it will be implemented for the client. **Write everything in the future tense.**

### Project Summary

Include the following:

- A description of the problem.
- A summary of the client and their needs as related to the problem.
- Descriptions of all deliverables. For example, the finished application and a user guide.
- A summary justifying how the application will benefit the client.  

### Data Summary

Include the following:

- The source of the raw data, how the data will be collected, or how it will be simulated.  
- A description of how data will be processed and managed throughout the application development life cycle: design, development, maintenance, or others.
- A justification of why the data meets the needs of the project. If relevant, describe how data anomalies, e.g., outliers, incomplete data, etc., will be handled.
- A list of any ethical or legal concerns regarding the data and how these concerns will be addressed. If there are no concerns, explain why.  

### Implementation

Include the following:

- A description of an industry-standard methodology to be used.
- An outline of the project’s implementation plan. The outline can focus on the project’s development as a whole; or it may focus on only the implementation of the machine learning solution.

### Timeline

Provide a projected timeline. Include each milestone and deliverable, its (project) dependencies, resources, start and end dates, and duration. (a table is not required but encouraged).

| Milestone or Deliverable  | Resources | Dependencies |  Projected Start & End Dates | Duration  |
| --- | --- | --- | --- | --- |
| Item 1 | Resources A, B | None | 4/28/2025 – 4/28/2025 | 1 day |
| Item 2 | Resource C | Item 1 | 4/29/2025 – 4/29/2025 | 1 day |
| Item 3 | Resources A, C | Items 1, 2 | 4/30/2025 – 5/01/2025 | 2 days |
|$\vdots$ |$\vdots$ |$\vdots$ |$\vdots$ |$\vdots$ |

```{note}
*All* dates must be in the future. Part B is a proposal.
```

### Evaluation Plan

Include the following:

- A description of the verification method(s) to be used at each stage of development.
- A description of the validation method to be used upon completion.

#### Verification

*Verification* is testing that your product meets its specifications and requirements. This can include tests, inspections, or methods applying to the code or model. For the latter approaches to avoid overfitting could be included. Verification checks that the product is built correctly.

#### Validation

*Validation* is testing how well the machine learning model performs. The appropiate validation method depends on your ML application and your project's purpose.

- For *supervised learning* describe an appropriate metric(s) for testing the model’s performance, e.g., accuracy or mean sqaured error.

- For *unsupervised learning* describe an appropriate method(s) for testing the model’s performance. The method should provide an appropriate example of the model’s output and how the output is relevant, or a metric measuring the model’s performance, e.g., the Rand index, collaborative filtering accuracy, or Silhouette Coefficient

- For *Reinforcement learning* describe what will be optimized and how it will be measured.

### Resources and Costs

Include an itemized list of all resources and costs. Where possible, provide specific on the items, e.g., ‘PyCharm Professional Ed.  2024.3.5.’

- Itemize hardware costs.
- Itemize software costs and include relevant version or licensing information.
- Itemize estimated labor time and costs.
- Itemize all estimated application costs including the specific environment, e.g., deployment, hosting, maintenance, etc.
