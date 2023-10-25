@echo off
SET /P Message=Enter git C964 commit comment: 
del /q "D:\OneDrive - Western Governors University\jupyter-books\C964\.history\*"
FOR /D %%p IN ("D:\OneDrive - Western Governors University\jupyter-books\C964\.history\*.*") DO rmdir "%%p" /s /q
del /q "D:\OneDrive - Western Governors University\jupyter-books\C964\_build\html\.history\*"
FOR /D %%p IN ("D:\OneDrive - Western Governors University\jupyter-books\C964\_build\html\.history\*.*") DO rmdir "%%p" /s /q
title compile html, save to repo folder, update GitHub repo and website
jupyter-book build --all "D:\OneDrive - Western Governors University\jupyter-books\C964"
echo "Compiling local D:\OneDrive - Western Governors University\jupyter-books\C964 ..."
xcopy /s /e /h /i /y "D:\OneDrive - Western Governors University\jupyter-books\C964" "D:\OneDrive - Western Governors University\jupyter-books\github_book_repo\C964"
echo "Copied local book to D:\... \jupyter-books\github_book_repo\C964 ..."
cd "D:\OneDrive - Western Governors University\jupyter-books\github_book_repo\C964" 
git add ./*
git commit -m "%Message%"
echo "Commited..."
git push
echo "Pushed..."
ghp-import -n -p -f _build/html
echo "Imported to git page..."
start https://ashejim.github.io/C964/intro.html
echo "Gitpage may take a few minutes to update. END"
cd D:\OneDrive - Western Governors University\jupyter-books\C964