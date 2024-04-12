from locust import HttpUser, task, between

class UserBehavior(HttpUser):
    wait_time = between(0.5, 2.5)

    @task
    def download_memorise_model(self):
        self.client.get('/assets/bernburg_spaces_english.glb')