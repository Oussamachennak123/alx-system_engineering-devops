#!/usr/bin/python3
"""
A sript that, uses a REST API, for a given employee ID returns
information about his/her TODO list progress
and exports data in the JSON format
"""

import json
import requests
from sys import argv


if __name__ == "__main__":

    sessionReq = requests.Session()

    idEmp = argv[1]
    idURL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(idEmp)
    nameURL = 'https://jsonplaceholder.typicode.com/users/{}'.format(idEmp)

    employee = sessionReq.get(idURL)
    employeeName = sessionReq.get(nameURL)

    json_req = employee.json()
    usr = employeeName.json()['username']

    totalTasks = []
    updateUser = {}

    for all__Emp in json_req:
        totalTasks.append(
            {
                "task": all__Emp.get('title'),
                "completed": all__Emp.get('completed'),
                "username": usr,
            })
    updateUser[idEmp] = totalTasks

    file__Json = idEmp + ".json"
    with open(file__Json, 'w') as f:
        json.dump(updateUser, f)
