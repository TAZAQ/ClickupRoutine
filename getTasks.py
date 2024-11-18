import sys

from API.Utils import get_tasks_from_lists

if __name__ == '__main__':
    status, *list_ids = sys.argv[1:]

    task_ids = get_tasks_from_lists(*list_ids, params={
        'statuses[]': [status],
    })

    print('|'.join(task_ids) or 'Not found')
