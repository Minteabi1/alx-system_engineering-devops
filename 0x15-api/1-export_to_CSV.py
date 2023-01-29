#!/usr/bin/python3
""" EXPORT TO CSV """

import csv
import requests
import sys

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("Usage: ./1-export_to_CSV.py <employee ID>")
        exit(1)
    id = sys.argv[1]

    def get_user_info(id):
        """ Get User Info """
        api_url = 'https://jsonplaceholder.typicode.com'
        user_uri = '{api}/users/{id}'.format(api=api_url, id=id)
        ruser_uri = requests.get(user_uri)
        return ruser_uri.json()

    def get_user_tasks(id):
        """ Get User Tasks """
        api_url = 'https://jsonplaceholder.typicode.com'
        user_uri = '{api}/users/{id}'.format(api=api_url, id=id)
        todo_uri = '{user_uri}/todos'.format(user_uri=user_uri)
        todo_url = requests.get(todo_uri)
        return todo_url.json()
    user = get_user_info(id)
    tasks = get_user_tasks(id)
    completed_tasks = []
    [completed_tasks.append(task) for task in tasks if task.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed_tasks), len(tasks)))
    [print("\t {}".format(task.get("title"))) for task in completed_tasks]

    with open('{}.csv'.format(id), 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([id, user.get('username'),
                             task.get('completed'), task.get('title')])
