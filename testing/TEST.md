# Test and validations

## Introduction
During the development process, unit testing has been done to check if functionality is as expected. Same test has been executed again later on when new features has been added.

## Test
Functionality has been tested by the same test cases as the front-end project and are documented in that repository. 

### Automatic tests

At first an atempt to work testdriven (TDD) was made and some test was written early and used during the development. However as the work progressed the automatic test cases were not prioritized enough. If more test had been written some common bugs could have been prevented when changes in back-end affected format of response. ¨

The automatic test cases were never seen as something that should validate or verify end functionality but be helpful during the development. 

## Solved bugs during development
- [#58](https://github.com/MartinaB91/project5-task-app-front/issues/58) Family member images won't show

## Validation 
### Python 

To validate the python code the extension "pycodestyle" has been used. 

GitPod PROBLEMS reports following errors when 'objects' is used "Class 'MODEL' has no 'objects' member" and "Class 'MODEL' has no 'DoesNotExist' member", this is an error that is safe to ignore according to Google and student channel. 

The validation of the settings.py has been only checked for errors and severe warnings. All other error/warnings/information has been left as is because changes in the settings file could affect the whole project. 
