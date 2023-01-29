#!/usr/bin/python3
""" Gather Data From Api """
import requests
import urllib
import sys


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("Usage: ./0-gather_data_from_an_API.py <employee ID>")
        exit(1)
    id = sys.argv[1]
    def get_user_info(id):
        """ Get User Info """
        url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
        r = requests.get(url)
        return r.json()

    def get_user_tasks(id):
        """ Get User Tasks """
        url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(id)
        r = requests.get(url)
        return r.json()
    
    user = get_user_info(id)
    tasks = get_user_tasks(id)
    completed_tasks = []
    [completed_tasks.append(task) for task in tasks if task.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed_tasks), len(tasks)))
    [print("\t {}".format(task.get("title"))) for task in completed_tasks]
   
       
    

    
