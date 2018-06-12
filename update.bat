SET /P umes=Commit Message:
git add .
git commit -m %umes
git push -u origin master