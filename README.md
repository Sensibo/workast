# workast

```
import json
import datetime
import workast

token = open('token').read()

client = workast.Workast(token)
client.space('Personal tasks').create_task('hello',
                                       sublist_name='some sublist',
                                       assigned_to=[client.user("email@email.com")],
                                       due_date=datetime.datetime.now())
```
