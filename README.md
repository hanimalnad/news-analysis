# THIS IS A WORK IN PROGRESS. THE README WILL BE UPDATED AS THE PROJECT IS UPDATED.

## Requirements for the project are:-

```
Python 3.9
```

## To run the above project

_Start a venv_

```
python -m venv myenv
./myenv/Scripts/activate
```

_Install all the requirements from the `requirements.txt`_

```
pip install -r requirements.txt
```

_Run the flask system_

```
python handlers.py
```

When running in local, the system shall connect port to `localhost:5000`
_It has two endpoints_

```
/scrape #To scarpe live-news sites
/summarize #To summarize the scrapped pages
```
