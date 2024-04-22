#!/usr/bin/python3
"""Returns  given employee ID."""
import requests
import sys

if __name__ == "__main__":
    uget = "https://jsonplaceholder.typicode.com/"
    user_get = requests.get(uget + "users/{}".format(sys.argv[1])).json()
    tget = requests.get(uget + "todos", params={"userId": sys.argv[1]}).json()

    com_data = [t.get("title") for t in tget if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user_get.get("name"), len(com_data), len(tget)))
    [print("\t {}".format(c)) for c in com_data]
