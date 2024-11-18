from API.API import get_tasks_from_list

APPROVED = 'approved'
STAGE = 'stage'
BEFOREPROD = 'beforeprod'
PRODUCTION = 'production'


def get_tasks_from_lists(*list_ids, params=None) -> []:
    lists_tasks = []
    for list_id in list_ids:
        current_list_tasks = get_tasks_from_list(list_id, params)
        lists_tasks.extend(current_list_tasks)

    return [task['id'] for task in lists_tasks]
