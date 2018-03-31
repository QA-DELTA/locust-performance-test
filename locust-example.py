from locust import HttpLocust, TaskSet, task
import uuid
from datetime import datetime
import json
 
headers={'authorization' : "Bearer 38f2721da1a909af591ed329d596767a60818fbd539a8010403eba067ff13a6f"}
 
class Tasks(TaskSet):
    @task()
    def redeemption(self):
        self.client.get("/_exclusive/homepage-panels?limit=3&offset=4", headers=headers)
 
class Tasks(HttpLocust):
    task_set = Tasks
    min_wait = 5000
    max_wait = 9000
