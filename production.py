import sys

from API.API import update_task_status, add_comment_to_task
from API.Utils import get_tasks_from_lists, BEFOREPROD, PRODUCTION, print_task_ids

if __name__ == '__main__':
    comment, *list_ids = sys.argv[1:]
    task_ids = get_tasks_from_lists(*list_ids, params={
        'statuses[]': [BEFOREPROD],
    })

    for task_id in task_ids:
        update_task_status(task_id, PRODUCTION)
        add_comment_to_task(task_id, comment)

    print_task_ids(task_ids)
