# ef-mini-project (backend)
eF Zoom Mini Project (BACKEND)

### Install requirement
- We use venv to create a sperate virtual environment.
- If on Mac, make sure you're using python 3.

```
> git clone git@github.com:azariz/ef-mini-project.git
> cd ef-mini-project
> python3 -m venv .venv
> source .venv/bin/activate
> pip install --upgrade pip
> pip install -r requirements.txt
```

### Run the backend
- A script is attached for quick local run (make sure it's ```chmod +x```).
- The app is running by default on Debug mode, can be disabled with ````FLASK_DEBUG=false````
- To run on a different host / port, change on ```run.sh```.
```
> ./run.sh
```

PS: If not using the script, be sure to activate the venv before running pip/flask.

```
> source .venv/bin/activate
```