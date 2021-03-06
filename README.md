### PROJECT NAME
Awads
### PROJECT AUTHOR
Suad M.Shire
### DESCRIPTION
This is a website that allows for  it's users to sign up, login, and post projects as well as rate the poted projects.
### PREREQUISITES
1. python3.6
2. Django=1.11
3. Postgres
4. virtual 
### CLONING & RUNNING
Run the following command on the terminal:

       git clone https://github.com/suad7/awads
### CREATE VENV    
- To Create a virtual environment run the following command:  

        python3.6 -m venv <the name of your virtual>     
- Then activate the virtual with this command:

        . virtual/bin/activate
### INSTALL DEPENDANCIES     
nstall the dependancies that will create an environment for the app to run with this command:

     pip3 install -r requirements.txt
### CREATE DATABASE
Run:  

     psql
     CREATE DATABASE <the name of your database>; 
### .ENV FILE      
Create .env file and paste paste the following filling where appropriate:  
```
SECRET_KEY = '<Secret_key>'
DBNAME = 'awads'
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True
```
### RUN MIGRATIONS
```
python3.6 manage.py makemigrations <the name of your App>
python3.6 manage.py migrate
```
## TECHNOLOGIES USED
* Django
* Python3.6
* Bootstrap 4
### DEPLOYING (LIVE LINK)

### BEHAVIOR DRIVEN DEVELOPMENT (SPECIFICATIONS)
| Input        | Output           | Behavior  |
| ------------- |:-------------:| -----:|
| Visit Awards site| Various projects are displayed  | User can review projects |
| Click on image| Image details displayed | Image details displayed |
| Visit profile | Projects posted by user are displayed | App gets projects for user |
### CONTACT 
sm.ha21@hotmail.com
### LICENSE 
ermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files, to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Copyright (c) 2020 Suad7