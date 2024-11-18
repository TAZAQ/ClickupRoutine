# Автоматизатор релизов

## Задачи в CU-списках

```bash
python getTasks.py status_name list_id1, list_id2, list_id3, ...
```

## Переводы в статусы

### approved - stage

```bash
python stage.py list_id1, list_id2, list_id3, ...
```

Перенесёт все таски из списков из статуса "approved" в статус "stage".

### stage - beforeprod

```bash
python beforeprod.py list_id1, list_id2, list_id3, ...
```

Перенесёт все таски из списков из статуса "stage" в статус "beforeprod".

### beforeprod - production

```bash
python production.py comment_text list_id1, list_id2, list_id3, ...
```

Перенесёт все таски из списков из статуса "beforeprod" в статус "production".

Во все таски из списка добавит сообщение comment_text.

### Возвращаемое значение

все скрипты выведут в консоль список задач, разделённый символом "|". Пример:

```text
8696negr8|8696ctgwp|8696ctgu8|8696c2b3n|8695kjeyf|8695kfcpv
```
