import os

import requests
from dotenv import load_dotenv

load_dotenv('.env')
CU_TOKEN = os.getenv('CU_TOKEN')
WORKSPACE_ID = os.getenv('WORKSPACE_ID')


def get_tasks_from_list(list_id, params=None):
    url = f'https://api.clickup.com/api/v2/list/{list_id}/task'
    headers = {
        'Authorization': CU_TOKEN,
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()['tasks']


def update_task_status(task_id, status):
    url = f'https://api.clickup.com/api/v2/task/{task_id}'
    headers = {
        'Authorization': CU_TOKEN,
        'Content-Type': 'application/json',
    }
    data = {
        'status': status
    }
    response = requests.put(url, headers=headers, json=data)
    return response.json()


def add_comment_to_task(task_id, comment):
    url = f'https://api.clickup.com/api/v2/task/{task_id}/comment'
    headers = {
        'Authorization': CU_TOKEN,
        'Content-Type': 'application/json',
    }
    data = {
        'comment_text': comment
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()
