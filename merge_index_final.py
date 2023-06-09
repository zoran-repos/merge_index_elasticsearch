import datetime
import signal
from elasticsearch import Elasticsearch

cancel_flag = False
es = Elasticsearch(hosts=['http://localhost:9200'])


def get_indexes_to_merge():
   
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month

    indexes_to_merge = []
    for year in range(2020, current_year + 1):
        end_month = 12 if year < current_year else current_month - 1
        for month in range(1, end_month + 1):
            index_name = f"index-data-{datetime.date.today().year}-{month:02d}"
            indexes_to_merge.append(index_name)

    return indexes_to_merge

 
def run_force_merge():
    indexes_to_merge = get_indexes_to_merge()

    for index_name in indexes_to_merge:
        print(f'Starting force merge for index: {index_name}')
 
        if not es.indices.exists(index=index_name):
            print(f'Index {index_name} does not exist. Skipping force merge.')
            continue
 
        response = es.indices.forcemerge(index=index_name, max_num_segments=1)
 
        if response.get('failed'):
            print(f'Failed to perform force merge for index: {index_name}')
        else:
            print(f'Force merge completed for index: {index_name}')
 
        if should_cancel():
            print('Force merge process cancellation requested. Stopping further merges.')
            break

def should_cancel():
    return cancel_flag


def handle_keyboard_interrupt(signal, frame):
    global cancel_flag
    cancel_flag = True
    print('Force merge process cancellation requested. Stopping further merges.')


signal.signal(signal.SIGINT, handle_keyboard_interrupt)


run_force_merge()

