import requests


class Workast:
    def __init__(self, token):
        self._api = _API(token)
        self._lists = {space['name']: _Space(self._api, space) for space in self._api.lists()}
        self._users = {user['email']: user for user in self._api.users()}

    def space(self, name):
        return self._lists[name]

    def user(self, email):
        return self._users[email]


class _Space:
    def __init__(self, api, raw):
        self._api = api
        self._raw = raw

    def create_task(self, text, sublist_name=None, assigned_to=None, due_date=None):
        list_id = self._raw['id']
        sublist_id = self._sublist(sublist_name)['id'] if sublist_name is not None else None
        self._api.create_task(text=text,
                              list_id=list_id,
                              sublist_id=sublist_id,
                              assigned_to=assigned_to,
                              due_date=due_date)

    def _sublist(self, name):
        for sublist in self._raw['subLists']:
            if sublist['name'] == name:
                return sublist
        raise KeyError(f"Can't find {name} in f{self._raw['subLists']}")


class _API:
    _API_ENDPOINT = 'https://api.todobot.io/'

    def __init__(self, token):
        self._session = requests.Session()
        self._session.headers.update({'Authorization': f'Bearer {token}'})

    def _post(self, path, **kwargs):
        response = self._session.post(f'{self._API_ENDPOINT}{path}', **kwargs)
        response.raise_for_status()
        return response.json()

    def _get(self, path, **kwargs):
        response = self._session.get(f'{self._API_ENDPOINT}{path}', **kwargs)
        response.raise_for_status()
        return response.json()

    def lists(self):
        return self._get('list')

    def create_task(self, text, list_id, sublist_id=None, assigned_to=None, due_date=None):
        data = {'text': text}
        if sublist_id is not None:
            data['subListId'] = sublist_id
        if assigned_to is not None:
            data['assignedTo'] = [user['id'] for user in assigned_to]
        if due_date is not None:
            data['dueDate'] = due_date.isoformat()
        self._post(f'list/{list_id}/task', json=data)

    def users(self):
        return self._get('user')