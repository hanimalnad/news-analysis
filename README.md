# THIS IS A WORK IN PROGRESS. THE README WILL BE UPDATED AS THE PROJECT IS UPDATED.

## Requirements for the project are:-
```
Python 3.9
```
## To run the above project
Start a venv
```
python -m venv myenv
./myenv/Scripts/activate
```

Install all the requirements from the `requirements.txt`
```
pip install -r requirements.txt
```
Run the web scrapper first to get the live news data and then run the summarizer to get summary of individual news articles
```
python webscrapper.py
python summarizer.py
```
