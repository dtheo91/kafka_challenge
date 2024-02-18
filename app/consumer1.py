
from kafka import KafkaConsumer
from consumer_data_processing import handle_data

if __name__ == "__main__":
    bootstrap_servers = 'kafka:9092'
    topic = 'Artificial_Intelligence'
    consumer_id = 1

    consumer = KafkaConsumer(topic,
                         auto_offset_reset='earliest',
                         bootstrap_servers=bootstrap_servers)
    
    # Consume messages
    handle_data(consumer, consumer_id, topic, processing_time=5)