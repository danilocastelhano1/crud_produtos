# CRUD de Produtos em Django Rest Framework


## Passos:
- Criar uma venv e ativar ela:
```
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
```
- Rodar pip from requeriments.txt: ```pip install -r /path/to/requirements.txt```
- Rodar make migrate: ``` python manage.py migrate```
- Criar um SuperUser: ```python manage.py createsuperuser --email admin@admin.com --username admin```


### Endpoints:
- Crud está em ```{BASE_URL}/api/produtos/```


### oAuth:
- Criar a Aplicação: ```{BASE_URL}/api/auth/applications/


- Gerar o Token:  ```{BASE_URL}/api/auth/token/```
```
curl --location --request POST '{BASE_URL}/api/auth/token/' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'grant_type=password' \
--data-urlencode 'client_id={CLIENTE_ID}' \
--data-urlencode 'client_secret={CLIENTE_SECRET}' \
--data-urlencode 'username={DJANGO USERNAME}' \
--data-urlencode 'password={DJANGO PASSWORD}'
```

## Documentação (swagger):

- Schemas: ```127.0.0.1:8000``` on browser

