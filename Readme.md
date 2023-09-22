#Flask app setup

- create and activate the virtual environment:
    ```bash 
        use python3 or python 

        --- creates a virtual environment
        python3 -m venv venv (linux/mac)
        python3 -m virtualenv venv (windows)

        --- activate the virtual environment
        . venv/bin/activate (linux/mac)
        /venv/Scripts/activate.bat (windows)
    ```

- next, install the flask  and flask-sqlalchemy after activating the virtual environment

```
    pip install flask flask-sqlalchemy

    or 

    pip install -r requirements.txt
```


- set up your entry point file, which is typically the app.py or index.py file.


- if you are using html files with flask, you should put them in a folder/directory named "templates" because flask will look in this folder for them automatically

- if you have assets like images, css files, and javascript files, you should put them in a folder/directory named "static" because flask looks into this folder for them automatically.


- to run your app, run:
  ```
    python app.py

    or 

    python3 app.py          // your entry point
  ```

<br>

### this project has been rearranged with a simple flask app structure.

# Submitting forms

- The form is linked to a route in the app.py file, e.g the form on the index.html has a POST method and an action of '/submit'.
  - this is is pointing to a route with the same action and method in app.py where the data is collected and stored in the database, after which the user is redirected to the same index.html
  

# Accessing saved data from database
- The form data in the database can be accessed by querying/fetching from the database, then passing the fetched data to the index.html template.
- The data cannot be shown in plain html, so we use "jinja2" syntax to display the data in a html table. jinja2 allows us to write python-like code in html.



# Additional information
- .gitignore file. 
  - this file ignores some files that I don't want on github

