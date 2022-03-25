#!/bin/bash

rm -rf .git
git init
git add -A
git status
git commit -m "Initial commit"
heroku create gpwg-test
heroku open
git push heroku master
