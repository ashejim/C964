# Creating Your Own GitHub Webpage!

## What you need to get started...

1. Python 3 ($\geq 3.9$ recommended)
2. The [Jupyter-Book](https://pypi.org/project/jupyter-book/) & [ghp-import](https://pypi.org/project/ghp-import/) packages.
4. A [Markdown](https://www.markdownguide.org/) editor. 
5. A GitHub account and repository.

## Step 1. Getting Python. 

Choose your flavor.
- [python.org](https://www.python.org/downloads/)
- [Anaconda](https://www.anaconda.com/products/distribution)

For a demonstration on this page, I'll use Anaconda because environments can be managed through a GUI; see [Python Environments Management in Anaconda Navigator](https://medium.com/cluj-school-of-ai/python-environments-management-in-anaconda-navigator-ad2f0741eba7). Creating a specialized Python environment is not required, but it is good practice. But if you're going to use Python for nothing else, you can probably skip this step.  

```{margin} What is a virtual environment? 
It's a tool that keeps dependencies required for different projects separate by creating isolated python virtual environments for them. This is one of the most important tools Python developers use. (TODO add GeekforGeek reference) See [Python Virtual Environment](https://www.geeksforgeeks.org/python-virtual-environment/) for more detals. 
```

## Step 2. Install the Required Packages
Open a windows terminal (or a terminal by launching CMD.exe from Anaconda Navigator. 

**Install Jupyter-book** which converts markdown and jupyter-notebook files into html. 

`````{tab-set}
````{tab-item} pip
```{code-block} shell
pip install jupyter-book
```
````
````{tab-item} conda
```{code-block} shell
conda install -c conda-forge jupyter-book
```
````
`````

````{margin} Pip in Conda
Want to use pip and Anaconda?
```shell
conda install -c anaconda pip
```
Now you can 'pip' in conda. 
````

**Install git** (it should already be installed) so you can connect your local files to a GitHub repository. 
`````{tab-set}
````{tab-item} pip
```{code-block} shell
pip install python-git
```
````
````{tab-item} conda
```{code-block} shell
conda install -c anaconda git
```
````
`````

**Install ghp-import** which will post your HTML files from your GitHub repository to the web. 
`````{tab-set}
````{tab-item} pip
```{code-block} shell
pip install ghp-import
```
````
````{tab-item} conda
```{code-block} shell
conda install -c conda-forge ghp-import
```
````
`````

```{margin} Adding cool stuff
Check out all the cool UI stuff you can do: [JupyterBook UI elements](https://jupyterbook.org/en/stable/content/components.html#components-tabs).
```

## Step 3. Create a Jupyter-Book

Create a sample book by going to the directory and running the following command:
```shell
jupyter-book create mynewbook/
```
Where 'mynewbook/' is the name of the folder you want your jupyter-book and all its source files to live (it will create the folder). 

## Step 4. Add some content!

Your two main choices for adding content are  Markdown (.md) and Juptyer Notebook (.ipynb) files. The former is easier and great for most stuff. The latter is less easy but very flexible. 

```{note} 
The sample book created in step 3 includes both Markdown and Jupyter files. 
```
Some Markdown editor options:
- [online editor](https://stackedit.io/app#)
- [Visual Studio Code](https://code.visualstudio.com/Docs/languages/markdown)
- [typora](https://typora.io/)

I use Visual Studio. 

## Step 5. Turn your Markdown/Jupyter files into HTML.

This is why we need juptyer-book. Go to folder where your jupyter-book folder lives and type: 

```shell
jupyter-book build mynewbook
```
And that's it. You now have the web files. After building, you'll be provided with a local link. Copy and paste the link into your browser of choice to check it out. 

## Step 6. Move Your Web files to the Web!

You can put your web files wherever you like. I'll use GitHub.

1. Go to your GitHub account. 
2. Create a repository. 
3. Clone the repository to a local directory -this will be the directory linked to github (use a different one than above unless you want to copy over it).  
4. Copy your book into the local repo clone.

```{margin} Jupyter Docs
See the [jupyter-book documentation](https://jupyterbook.org/en/stable/start/publish.html) for more details. 
```

```shell
cd directorywhereyouwantittobe
git clone https://github.com/<my-org>/<my-repository-name>
```
For example, 
```shell
cd github_book_repo
git clone https://github.com/ashejim/examplebook/
```

Now copy your built Jupyter book files into this new folder.  

```{warning}
What! You don't have a GitHub account? Well getting one is free and easy. As long as its public, your repos and webpages will also be free.  
```
A GitHub repository is a great place to put all kinds of stuff. 

## Step 7. Sync your local repo to the GitHub repoistory. 

```shell
cd directorywhereyouwantittobe/mynewbook
git add ./*
git commit -m "a message is optional, but helpful."
git push
```

## Step 8. Sync your book to a GitPage. 
In the same folder:

```shell
ghp-import -n -p -f _build/html
```

Wait a few minutes and go to:

```shell
https://<user>.github.io/<myonlinebook>/
``` 
(you can copy and paste the new site name from the terminal output.)

```{margin} GitHub Pages Docs
See the [Github Pages Doc](https://docs.github.com/en/pages/getting-started-with-github-pages/unpublishing-a-github-pages-site) for more (and better) details.
```

Congratulations! You have a website!