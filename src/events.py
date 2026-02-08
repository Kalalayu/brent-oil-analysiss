import pandas as pd

def load_events(path):
    events = pd.read_csv(path)
    events['Event_Date'] = pd.to_datetime(events['Event_Date'])
    return events
