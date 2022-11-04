@echo off
title compile html, save to repo folder, update GitHub repo and website
jupyter-book build --all C:\Users\Jim\OneDrive\jupyter-books\C964
echo "Compiling local C:\Users\Jim\OneDrive\jupyter-books\C964 ..."
xcopy /s /e /h /i /y C:\Users\Jim\OneDrive\jupyter-books\C964 C:\Users\Jim\OneDrive\jupyter-books\github_book_repo\C964
echo "Copied local book to ..jupyter-books\github_book_repo\C964 ..."
cd C:\Users\Jim\OneDrive\jupyter-books\github_book_repo\C964 
git add ./*
SET /P Message=Enter git commit comment: 
git commit -m "%Message%"
echo "Commited..."
git push
echo "Pushed..."
ghp-import -n -p -f _build/html
echo "Imported to git page..."
start https://ashejim.github.io/C964/intro.html
echo "Gitpage may take a few minutes to update. END"
cd C:\Users\Jim\OneDrive\jupyter-books