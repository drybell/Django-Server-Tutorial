import requests as r 
import json 

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

body = { 
	'text': 'Delete this task created by a python script'
}

# res = r.get('http://localhost:8000/backend/todo', headers=headers)
res = r.post('http://localhost:8000/backend/todo/', headers=headers, data=json.dumps(body))

return_dict = json.loads(res.content.decode('utf-8'))

print(json.dumps(return_dict, indent=4))