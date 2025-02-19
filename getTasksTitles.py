import sys

from API.Utils import get_tasks_from_lists, print_task_ids, PRODUCTION, print_tasks


def main():
    status, *list_ids = sys.argv[1:]

    tasks = get_tasks_from_lists(*list_ids, is_production=True, params={
        'statuses[]': [status],
    })

    return print_tasks(tasks)

if __name__ == '__main__':
    main()
