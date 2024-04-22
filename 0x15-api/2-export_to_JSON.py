#!/usr/bin/python3
"""Exports to-do list inf"""
import json
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    ba = "https://jsonplaceholder.typicode.com/"
    user = requests.get(ba + "users/{}".format(employee_id)).json()
    username = user.get("username")
    todos = requests.get(ba + "todos", params={"userId": employee_id}).json()

    with open("{}.json".format(employee_id), "w") as jsonfile:
        json.dump({employee_id: [{
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": username
            } for todo in todos]}, jsonfile)
