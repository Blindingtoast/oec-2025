import pytest
from backend.database.models import UsersSchema, ReportsSchema
import random
import datetime

def generate_report(lat, lon, deviation, types):
    """Create a report to be sent by a client, with a random name

    Args:
        lat (float): a latitude coordinate
        lon (float): a longitude coordinate
        radius (float): the distance (in kilometers) from the coordinates that a report can be generated
        type (list[ReportType]): the types of reports that can be generated
    """
    rand_lat = random.gauss(lat, deviation)
    rand_lon = random.gauss(lon, deviation)
    rand_time = datetime.now()

    report = ReportSchema
    return 
    
    
def create_user():
    pass

def 

def test_add_single_user(client):
    create_user()
    # A dict with the different fields in the request body we need
    data
    client.post()

def test_single_report(client):
    generate_report(0, 0, 10)
