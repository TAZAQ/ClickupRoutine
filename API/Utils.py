from API.API import get_tasks_from_list

APPROVED = 'approved'
STAGE = 'stage'
BEFOREPROD = 'beforeprod'
PRODUCTION = 'production'


def get_tasks_from_lists(*list_ids, params=None, is_production=False) -> []:
    lists_tasks = []
    for list_id in list_ids:
        current_list_tasks = get_tasks_from_list(list_id, params)
        lists_tasks.extend(current_list_tasks)

    if is_production:
        return lists_tasks

    return [task['id'] for task in lists_tasks]


def print_task_ids(task_ids):
    print('|'.join(task_ids) or 'Not found')


def print_tasks(tasks):
    print(*[f"{task['url']} - {task['name']}" for task in tasks], sep="\n")
