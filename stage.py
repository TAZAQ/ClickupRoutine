import sys

from API.API import update_task_status
from API.Utils import get_tasks_from_lists, APPROVED, STAGE

if __name__ == '__main__':
    task_ids = get_tasks_from_lists(*sys.argv[1:], params={
        'statuses[]': [APPROVED],
    })

    for task_id in task_ids:
        update_task_status(task_id, STAGE)

    print('|'.join(task_ids))
