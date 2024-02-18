# Kafa Challenge 

## Setup

1. Install [Docker](https://www.docker.com/get-started)
2. Install [Docker Compose](https://docs.docker.com/compose/install/)
3. Clone this repository

## Running the project

1. Open a terminal and navigate to the root of the project
2. Run `docker-compose up`

This will setup the Kafka Container, the MongoDB Container and the Python Application Container.
By spinning up the Python Application, it initially spawns three Consumers for different Kafka Topics. 

## Accessing the services

Going to http://localhost:8888/ brings you to a Jupyterlab, where you can spawn a Producer to send data to a certain Topic via: <big>producer.ipynb</big> 

The data you send via the Producer is being processed by the Consumers and later saved to the MongoDB database.
You can go to http://localhost:8081 to manage the MongoDB Database in Mongo-Express.

You can also check in the logs of the Python Application Container to see the data being processed and saved to the Database.