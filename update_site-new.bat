@echo off
cd D:\OneDrive - Western Governors University\jupyter-books\C964
FOR /d /r . %%d IN (.history) DO @IF EXIST "%%d" rd /s /q "%%d"
@REM DEL /S /Q "D:\OneDrive - Western Governors University\jupyter-books\C964\output_plot*.png"
DEL /S /Q "output_plot*.png"
SET /P Message=Enter git C964 commit comment: 
title compile html, save to repo folder, update GitHub repo and website
jupyter-book build --all "..\C964"
echo "Compiling local ..\C964 ..."
xcopy /s /e /h /i /y "..\C964" "..\github_book_repo\C964"
echo "Copied local book to ..\github_book_repo\C964 ..."
cd "..\github_book_repo\C964" 
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
