# THIS IS A WORK IN PROGRESS. THE README WILL BE UPDATED AS THE PROJECT IS UPDATED.

## Requirements for the project are:-

```
Docker
```

## To run the above project

- Start your docker engine 
- Run the following command in the specific directory
```
docker-compose up --build
```
To shut down the local dev 
```
docker-compose down 
```

When running in local, the system shall connect port to `localhost:5000` \
_It has two endpoints_

```
GET /scrapeand_categorize_ #To scarpe live-news and categorize
GET /senti #To obtain the sentiment analysis of the scrapped pages
```
