import requests
from llm_api import LLMAPI

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.llm_api = LLMAPI()

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_id):
        self.tasks = [task for task in self.tasks if task['id'] != task_id]

    def update_task(self, task_id, updated_task):
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                self.tasks[i] = updated_task
                break

    def generate_optimal_schedule(self):
        optimal_schedule = self._generate_schedule_with_llm()
        return optimal_schedule

    def _generate_schedule_with_llm(self):
        data = {
            "tasks": self.tasks
        }
        response = self.llm_api.get_response("schedule", data)
        if "error" not in response:
            return response.get("optimal_schedule", "No schedule generated")
        else:
            return f"Error generating schedule: {response['message']}"
