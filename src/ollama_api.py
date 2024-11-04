import requests

class OllamaAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.ollama.com/v1"

    def send_request(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        response = requests.post(url, headers=headers, json=data)
        return response

    def get_response(self, endpoint, data):
        response = self.send_request(endpoint, data)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.status_code, "message": response.text}
