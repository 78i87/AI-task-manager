import datetime
import calendar

class CalendarIntegration:
    def __init__(self):
        self.calendar = {}

    def update_schedule(self, task, start_time, end_time):
        date = start_time.date()
        if date not in self.calendar:
            self.calendar[date] = []
        self.calendar[date].append({
            "task": task,
            "start_time": start_time,
            "end_time": end_time
        })

    def get_schedule_for_date(self, date):
        return self.calendar.get(date, [])

    def sync_with_external_calendar(self, external_calendar):
        for date, events in external_calendar.items():
            if date not in self.calendar:
                self.calendar[date] = []
            self.calendar[date].extend(events)
