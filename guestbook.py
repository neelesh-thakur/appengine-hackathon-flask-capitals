from datetime import datetime
from google.cloud import datastore


class Greeting:

    def __init__(self):
        self.ds = datastore.Client(project="bootcamp-nthakur4")
        self.kind = "PythonGreeting"

    def store_greeting(self, comment):
        key = self.ds.key(self.kind)
        entity = datastore.Entity(key)

        entity['comment'] = comment
        entity['timestamp'] = datetime.utcnow()

        return self.ds.put(entity)

    def fetch_greetings(self):
        query = self.ds.query(kind=self.kind)
        query.order = ['-timestamp']
        return self.get_query_results(query)

    def get_query_results(self, query):
        results = list()
        for entity in list(query.fetch()):
            results.append(dict(entity))
        return results

