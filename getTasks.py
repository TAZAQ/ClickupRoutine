import sys

from API.Utils import get_tasks_from_lists, print_task_ids, PRODUCTION, print_tasks


def main():
    status, *list_ids = sys.argv[1:]
    is_production = status == PRODUCTION

    tasks = get_tasks_from_lists(*list_ids, is_production=is_production, params={
        'statuses[]': [status],
    })

    if is_production:
        return print_tasks(tasks)

    print_task_ids(tasks)


if __name__ == '__main__':
    main()
