# Stacc Code Challenge 2021 KYC

This is my solution to the code challenge PEP check task.  

My solution has the following features:  
- PEP check and api on individual
- PEP check and api on company
- Deployed on stacc-kyc-task.herokuapp.com (currently not working)  


## Requirements:
- Python 3.8.3 or higher


## How to use:
- `$ pip install -r requirements.txt`
- `$ flask run`

If pip not in path:
- `$ python -m pip install -r requirements.txt`


## API docs:  

Single PEP check example:  
`{{server}}/api/name?name=Jonas Gahr Støre`  

Company PEP check example:  
`{{server}}/api/company?orgNr=988971375`  

Default server:  
http://127.0.0.1:5000  


Thank you for reading this far! This is my first time implementing an API, had a lot of fun and learned a ton. There are a couple issues here to iron out but most of it should be working fine.