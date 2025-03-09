'''
Dive into Python's standard library modules (e.g., datetime, itertools, functools).
'''

from datetime import datetime, timedelta
from itertools import cycle, count
from functools import lru_cache

# 1. Function to generate event dates
@lru_cache(maxsize=10)  # Cache results for optimization
def get_event_date(start_date, weeks_ahead):
    """Calculate future event date by adding weeks."""
    return start_date + timedelta(weeks=weeks_ahead)

# 2. Cycle through a list of event names
event_names = cycle(["Gym", "Work", "Conference", "Lunch"])

# 3. Generate recurring events (next 6 occurrences)
start_date = datetime.now()
event_counter = count(1)  # Start counting from 1

print("\nUpcoming Events Schedule:\n")
for _ in range(6):  # Get the next 6 events
    event_number = next(event_counter)  # Increment event count
    event_date = get_event_date(start_date, event_number)  # Compute event date
    event_name = next(event_names)  # Get the next event type
    print(f"Event {event_number}: {event_name} on {event_date.strftime('%Y-%m-%d')}")

