# Автоматизатор релизов

## Где взять list_id?
Замечено 2 вида ссылок:
* https://app.clickup.com/1234567/v/l/6-901204650614-1 - list_id = 901204650614
* https://app.clickup.com/1234567/v/l/901204650614 - list_id = 901204650614

## Задачи в CU-списках

```bash
python getTasks.py status_name list_id1, list_id2, list_id3, ...
```

### Статусы

* approved
* stage
* beforeprod
* production

### Возвращаемое значение (не production)

```text
8696negr8|8696ctgwp|8696ctgu8|8696c2b3n|8695kjeyf|8695kfcpv
```

### Возвращаемое значение (production)

```text
https://app.clickup.com/t/8696kq7ag - Настройки/Сообщения - в общих настройках SMS и WhatsApp пропало второе поле для отображения разрешенного периода отправки сообщения
https://app.clickup.com/t/8696hmen9 - Пациенты/Инфокарта - 500 ошибка при открытии вкладки "Счета" в инфокарте конкретного пациента
https://app.clickup.com/t/8696h6b8n - ЕГИСЗ/Отчество подписывающего врача - иностранцы без отчества не могут подписывать док. ЕГИСЗ без ошибок
...
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
