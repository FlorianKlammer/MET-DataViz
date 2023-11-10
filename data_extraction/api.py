import json 
from requests_ratelimiter import LimiterSession
session = LimiterSession(per_second=80)


def getDepartments():
    url = "https://collectionapi.metmuseum.org/public/collection/v1/departments"
    response = session.get(url)
    return response.json()

def getObjectsfromDepartment(id):
    url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects?departmentIds={id}"
    response = session.get(url)
    return response.json()

def getObjectJSON(id):
    url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{id}"
    response = session.get(url)
    return response.json()


def getImgUrlfromJSON(data):
    return data['primaryImage']








    