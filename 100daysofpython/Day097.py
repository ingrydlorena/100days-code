import weakref
import gc
from datetime import datetime, timedelta
from itertools import cycle, count
from functools import lru_cache


class Event:
    __slots__ = ['name', 'date', 'next_event', '__weakref__']  # Allow weak references

    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.next_event = None  # Placeholder for next event reference

    def __repr__(self):
        return f"{self.name} on {self.date.strftime('%Y-%m-%d')}"


@lru_cache(maxsize=10)
def get_event_date(start_date, weeks_ahead):
    return start_date + timedelta(weeks=weeks_ahead)


event_names = cycle(["Hackathon", "Workshop", "Conference", "Meetup"])
event_counter = count(1)  


events = []


start_date = datetime.now()
previous_event = None

print("\nUpcoming Events Schedule:\n")

for _ in range(6):
    event_number = next(event_counter)
    event_date = get_event_date(start_date, event_number)
    event_name = next(event_names)

    event = Event(event_name, event_date)  

    
    if previous_event:
        previous_event.next_event = weakref.ref(event)

    previous_event = event 
    events.append(event)  

    print(event)  


gc.collect()


print("\nEvents still in memory:")
for ev in events:
    print(ev)  
