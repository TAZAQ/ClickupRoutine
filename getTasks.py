import sys

from API.Utils import get_tasks_from_lists, print_task_ids

if __name__ == '__main__':
    status, *list_ids = sys.argv[1:]
    task_ids = get_tasks_from_lists(*list_ids, params={
        'statuses[]': [status],
    })

    print_task_ids(task_ids)
