# Function to extract the event date from an Event object
def get_event_date(event):
    return event.date

# Function to determine which users are currently logged in on each machine
def current_users(events):
    # Sort the events chronologically by event date
    events.sort(key=get_event_date)

    # Dictionary to store the machines and their corresponding sets of logged-in users
    machines = {}

    # Process each event in the sorted list
    for event in events:
        # If the machine is not already in the dictionary, add it with an empty set
        if event.machine not in machines:
            machines[event.machine] = set()

        # If the event is a login, add the user to the machine's set
        if event.type == "login":
            machines[event.machine].add(event.user)
        # If the event is a logout, remove the user from the machine's set
        elif event.type == "logout":
            machines[event.machine].remove(event.user)

    # Return the dictionary containing machines and their logged-in users
    return machines

# Function to generate a report of currently logged-in users for each machine
def generate_report(machines):
    # Iterate over the dictionary of machines and their user sets
    for machine, users in machines.items():
        # Only generate a report for machines with logged-in users
        if len(users) > 0:
            # Create a comma-separated string of logged-in users
            user_list = ", ".join(users)
            # Print the machine name and the list of users
            print("{}: {}".format(machine, user_list))

# Class to define an Event object representing login/logout activities
class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date      # The timestamp of the event
        self.type = event_type      # The type of event: 'login' or 'logout'
        self.machine = machine_name # The machine where the event occurred
        self.user = user            # The user involved in the event

# List of Event objects representing login/logout actions
events = [
    Event('2020-01-21 12:45:46', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'login', 'mailserver.local', 'chris'),
]

# Call the function to determine the current users on each machine
users = current_users(events)

# Print the dictionary of current users
print(users)
