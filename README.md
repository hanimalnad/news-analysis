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

When running in local, the system shall hit resort to `localhost:5000`
_It has two endpoints_

```
GET /scrape #To scarpe live-news sites
GET /summarize #To summarize the scrapped pages
```
