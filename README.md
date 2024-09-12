
# Sample Python Selenium  Framework
# for web store  https://www.saucedemo.com/
## There are 3 Test cases class when we test functional working of website in terms of login, user, make a choice of product and complete buying product  

### test_login_user

* Testing using name of user and password
* Check if the access was successful

### test_choose_product

* Make a choice of product
* Check if product been chosen and get in cart 

### test_of_buying

* Complete all steps to buy product 
* Check if we get proper indication on site 


The tech stack used in this project are:

    Python as the programming language for writing test code
    Selenium as the framework
    PIP3 as the build tool
    VSCode as the preferred IDE for writing python code.

Design pattern of Selenium 
  ```
Page object model POM
  ```
### Structure of project:

- Directory tests - contents scripts of all tests 
-  Directory pages - contents scripts of pages 

- requirements.txt -is a file that contains a list of packages or libraries needed to work on a project that can all be installed with the file.
- setup.py - content fixture for pretesting setup (login and choose product)
- README.md - information for installing and using this framework 



## What to need to do run all tests


### Install all packages and prepare your environment 

install Chromedriver or another driver for browser working:

[Install Chromedriver
](https://developer.chrome.com/docs/chromedriver/downloads?hl=ru)

### Create virtual environment 
  ```
python -m venv venv 
  ```
### Activate virtual environment pip
  ```
.\venv\scripts\activate  
  ```
### Install all packages in your IDE,  type in  Terminal command:
  ```
pip install -r requirements.txt
  ```

### Run test 
In order to run all tests type this in Terminal IDE  

  ```
  pytest -v   
  ```
