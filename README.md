# CSV Duplicate Identifier

## Dependencies

Please ensure you have ptyhon3 isntalled and accessible from your CLI

## For Local Setup & Configuration

1. Run . ./setupvirtualenv.sh to install virtual env for python3 and configure a virtual env instance
2. Run . ./envconfig.sh to activate virtual env instance and install dependencies

## Usage and Execution

In order to execute the code you need have the virtualenv instance active.

You can achieve this by either running: _**. ./envconfig.sh**_ or _**source csvvalidatorenv/bin/activate**_

The script accepts and requires two parameters in order to execute

1. First argument is the absolute file path 
  a. For example: /Users/{Your_Username}/Projects/emailIdValidator/sample.csv
3. Second argument is the column to be used for the evaluator 
  a. For Exmaple: 1
  
An example of the execution is: python3 csvDuplicateRowsFinder.py /Users/{Your_Username}/Projects/emailIdValidator/sample.csv 0

## Running sample test case

Run on CLI python3 csvDuplicateRowsFinder.py {YOURPATH}/sample.csv 0
