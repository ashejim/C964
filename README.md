#Hi

To compile this locally, you'll need jupyter-books
'pip install jupyter-books <2'
This is version 1.0. The latest version uses myst.  

You will also need to install most of the packages included in 'requirements.txt'
run:
'pip install -r requirments.txt'

Run
'jb build ./repo_directory'

If you get an error about missing kernels, it's because VS code creates unique kernel names in the ipynb's metadata. This is really dumb and prevents it from running on other machines. To fix this, you can relabel the kernel names (VS code doesn't nativel;y allow this) using the included py script:
'python .\update_kernels.py' 