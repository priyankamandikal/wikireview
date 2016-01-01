# Wikireview

The goal of this project is to build an accuracy review bot for Wikipedia that marks outdated/unclear passages and sends it to the reviewers for review.

It is advisable to run the application in a virtual environment. Ubuntu users can install it using this command:
```
$ sudo apt-get install virtualenv
```

To run the application on your system, clone this GitHub repository into your local PC using the following command in the terminal:<br>
```
$ git clone https://github.com/priyankamandikal/wikireview.git
```
Now setup a virtual environment called venv (you could give it any name) in the project folder using:
```
$ virtualenc venv
```
Activate the virtualenv:
```
$ source venv/bin/activate
```
You'll now have to install all the dependencies before being able to run the application. All the dependies have been specified in the requirements.txt file. They can be installed using the command:
```
$ pip install -r requirements.txt
```
The database also has to be set up. Just run the following command.
```
python manage.py db upgrade
```
You should now see data-dev.sqlite in your project home folder.<br><br>
The set up is now complete! Run the app using the command:
```
python manage.py runserver
```
Open up your browser and go to http://127.0.0.1:5000/<br>
You now have a working version of the application!
