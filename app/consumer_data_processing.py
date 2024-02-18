from pymongo import MongoClient
import time
import threading
import json
import datetime
import logging

############################################
#### Helper Functions for Data Handling ####
############################################

def insert_wikipedia_historic(data, topic):
    """
    Inserts data into the MongoDB Wikipedia Historic database into the correct collection.

    Args:
    data (str): The data from the Kafka consumer.
    """
    # Connect to MongoDB
    client = MongoClient("mongodb://root:example@mongo:27017/")
    # Access or create a database
    db = client["Wikipedia_Historic"]
    # Access or create a collection within the database
    collection = db[topic]
    # Insert documents into the collection
    result = collection.insert_many(data)
    # Print the result
    logging.info(f"Inserted document with ID to database Wikipedia_Historic: {result.inserted_ids} into collection: {topic}")
    # Close the connection
    client.close()

def insert_wikipedia_trend(data, topic):
    """
    Inserts data into the MongoDB Wikipedia Trend database into the correct collection.

    Args:
    data (str): The data from the Kafka consumer.
    """
    # Connect to MongoDB
    client = MongoClient("mongodb://root:example@mongo:27017/")
    # Access or create a database
    db = client["Wikipedia_Trend"]
    # Access or create a collection within the database
    collection = db[topic]

    # Count number of edits
    number_of_edits = len(data)
    german_edits = 0
    for edit in data:
        if edit["Type"] == "German":
            german_edits += 1
    results = {"Date": datetime.datetime.now(), 
               "Number_of_Global_Edits": number_of_edits, 
               "Number_of_German_Edits": german_edits}
    
    # Insert documents into the collection
    result = collection.insert_one(results)
    # Print the result
    logging.info(f"Inserted document with ID to database Wikipedia_Trend: {result.inserted_id} into collection: {topic}")
    # Close the connection
    client.close()

def process_data(data, topic):
    """
    This function processes the data from the Kafka consumer
    and inserts it into the MongoDB Databases:
    Wikipedia_Historic and Wikipedia_Trend.

    Args:
    data (str): The data from the Kafka consumer.
    """
    insert_wikipedia_historic(data, topic)
    insert_wikipedia_trend(data, topic)

####################################
#### Function used in Consumers ####
####################################
    
def handle_data(consumer, consumer_id, topic, processing_time=60):
    """
    This function handles the incoming data to the Kafka consumer.
    
    Args:
    consumer (KafkaConsumer): The Kafka consumer.
    """
    # Configure logging
    logging.basicConfig(filename='Kafka.log', level=logging.INFO)

    messages = []

    def process_data_periodically():
        while True:
            time.sleep(processing_time)
            if messages:
                logging.info(f"Consumer {consumer_id} processing data...")
                process_data(messages, topic)
                messages.clear()

    # Start the thread for periodic data processing
    processing_thread = threading.Thread(target=process_data_periodically)
    processing_thread.daemon = True  # Daemonize the thread so it automatically exits when the main program ends
    processing_thread.start()

    # Print the topic the consumer is handling
    logging.info(f"Consumer {consumer_id} now handles data on topic: {topic}")
    # Consume messages
    for message in consumer:
        # Append the message to the list
        if message.value:
            json_string = message.value.decode("utf-8")
            json_data = json.loads(json_string)
            messages.append(json_data)
            logging.info(f"Consumer {consumer_id} received message: {json_data}")