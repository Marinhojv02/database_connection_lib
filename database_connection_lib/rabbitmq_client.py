from pika import PlainCredentials, ConnectionParameters, BlockingConnection

class RabbitMQClient:
    def __init__(self, host: str, port: str):
        self.host = host
        self.port = port
        self.client = None
        self.connect()

    def connect(self):
        parameters = ConnectionParameters(host=self.host, port=self.port)
        self.client = BlockingConnection(parameters)
        print("Connected to RabbitMQ")
        
    def is_connected(self):
        return self.client is not None and self.client.is_open

    def close(self):
        if self.is_connected():
            self.client.close()
            self.client = None
            print("Closed RabbitMQ connection")
        else:
            print("No connection to close")
    
    def get_channel(self):
        if self.is_connected():
            return self.client.channel()
        return None