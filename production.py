import sys

from API.API import update_task_status, add_comment_to_task
from API.Utils import get_tasks_from_lists, BEFOREPROD, PRODUCTION, print_tasks

if __name__ == '__main__':
    comment, *list_ids = sys.argv[1:]
    tasks = get_tasks_from_lists(*list_ids, is_production=True, params={
        'statuses[]': [BEFOREPROD],
    })

    for task in tasks:
        update_task_status(task['id'], PRODUCTION)
        add_comment_to_task(task['id'], comment)

    print_tasks(tasks)
