import sys
from task_manager import TaskManager
from personal_assistant import PersonalAssistant
from calendar_integration import CalendarIntegration

def main():
    task_manager = TaskManager()
    personal_assistant = PersonalAssistant(task_manager)
    calendar_integration = CalendarIntegration()

    while True:
        user_input = input("How can I assist you today? (type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        response = personal_assistant.handle_user_input(user_input)
        print(response)

if __name__ == "__main__":
    main()
