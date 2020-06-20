from confluent_kafka import Producer
from confluent_kafka.admin import AdminClient, NewTopic


BROKER_URL = 'localhost:9092'


### The produce will create a NewTopic - Using JSON shcema

class KafkaProducer(self):

    def __init__(self,num_partitions=1,num_replicas=1,topic_name,cleanup_policy='delete'):
        
        # Topic configuration that you wanna modify
        self.num_partitions = num_partitions
        self.num_replicas= num_replicas
        self.topic_name = topic_name
        self.cleanup_policy = cleanup_policy

        # If you chose compact, pleas use lz4, for more details - view README.md
        if(self.cleanup_policy == 'compact'):
            ## Configure Topic for compact
            self.topic_configuration  = {
                "cleanup.policy": 'compact',
                "compression.type": "lz4",
                "delete.retention.ms": 100,
                "file.delete.delay.ms": 10
            }
        else:
            ## Configure Topic for compact
            self.topic_configuration  = {
                "cleanup.policy": 'delete'
            }            

        # create a dict with Producer configuration
        self.producer_configuration = {
            "bootstrap.servers": BROKER_URL,
            "client.id": f{topic_name.splt(".")[-1]+"_group"}
        }

        # create a producer
        self.producer = Producer(
            self.producer_configuration
        )
        


    def create_topic(self):
        client = AdminClient({"bootstrap.servers":BROKER_URL})
        
        topic_metadata = client.list_topics(timeout = 5)

        if (topics_metadata.topics.get(self.topic_name) is not None):
            print("Topic already exist")
            pass
        else:
            print(f" Creating New Topic {self.topic_name}")

            future = client.create_topic([
                NewTopic(
                    topic = self.topic_name,
                    num_partitions = self.num_partitions,
                    replication_factor = self.num_replicas,
                    config = self.topic_configuration  
                )
            ])
            for topic, future in futures.items():
                try:
                    future.result()
                    print(f"Topic {self.topic_name} Create Sucessuful!!!")
                except Exception as e:
                    print(f"Failed to create topic {topic_name}: {e}")
                    raise


    def close():
        # Close the Producer, firts flush second close
        self.produce.flush()
        self.produce.close()
        print("Produce Close Succesulf!!")