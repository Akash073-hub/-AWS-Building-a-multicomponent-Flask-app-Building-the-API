import shelve
from flask import g


# This function creates a database if none has yet been created,
# or opens it if it's already there.
def pull_db():
    db_ = getattr(g, '_database', None)
    if db_ is None:
        db_ = g._database = shelve.open("storage")
    return db_


# This function returns the entire dataset of devices as a dictionary
def get():
    with pull_db() as shelf:
        devices_ = {}
        keys = list(shelf.keys())
        for key in keys:
            devices_[key] = shelf[key]
    return devices_


# This function adds a new element to the datastore of devices
def post(args):
    # TODO: create the database shelf object
        # TODO: Check if the id already exists in the shelf, and if so--returnin an error message

        # If the ID does not exist, add the new device
        # TODO: add the data about the new item from args to the shelf


# A Dict of Dicts to define initial devices
devices = {"001": {
    "id": "001",
    "name": "Light bulb",
    "location": "hall",
    "status": "off"
},
    "002": {
        "id": "002",
        "name": "Humidity_sensor",
        "location": "bedroom",
        "status": "on"
    },
    "003": {
        "id": "003",
        "name": "Humidifier",
        "location": "bedroom",
        "status": "off"
    }
}

# Initialize db with some data already in it
with shelve.open('storage') as db:
    for key, value, in devices.items():
        db[key] = value


