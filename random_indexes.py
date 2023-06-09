import datetime
import random
from elasticsearch import Elasticsearch

es = Elasticsearch(hosts=['http://localhost:9200'])

def generate_random_data():
    data = {
        'timestamp': datetime.datetime.now(),
        'value': random.randint(1, 100)
    }
    return data

def create_indices_and_fill_data():
    for month in range(1, 13):
        index_name = f"index-data-{datetime.date.today().year}-{month:02d}"
        
    
        es.indices.create(index=index_name)
        print(f"Created index: {index_name}")
        
    
        for _ in range(1000):
            data = generate_random_data()
            es.index(index=index_name, body=data)
        
        print(f"Indexed data for index: {index_name}")

create_indices_and_fill_data()
