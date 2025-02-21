import sys

from API.API import add_comment_to_task

if __name__ == '__main__':
    comment, *task_ids = sys.argv[1:]

    if len(task_ids) == 1:
        task_ids = task_ids[0].split('|')

    for task_id in task_ids:
        add_comment_to_task(task_id, comment)
