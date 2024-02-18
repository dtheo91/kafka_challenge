# Kafa Challenge 

## Setup

1. Install [Docker](https://www.docker.com/get-started)
2. Install [Docker Compose](https://docs.docker.com/compose/install/)
3. Clone this repository

## Running the project

1. Open a terminal and navigate to the root of the project
2. Run `docker-compose up`

This will setup the Kafka container, the MongoDB container and the Python Application container.
By spinning up the Python Application, we spawn three consumers for different Kafka topics. 

Going to http://localhost:8888/ brings you to a Jupyterlab, where you can spawn a Producer to send data to a certain topic in producer.ipynb. The data you send is being processed by the consumers and later saved to the MongoDB database.

You can go to http://localhost:8081 to manage the MongoDB database in Mongo-Express.