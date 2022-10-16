
## Documentação da API

#### POST /auth/token
Autentica o usuario, devolvendo um access_token

#### POST /auth/token/refresh
Atualiza o token do usuario

#### POST /persons/
Adiciona uma nova pessoa 
Retorna Status Code 201
```JSON
{
    "name": "any name"
}
```

#### GET /persons
Retorna todas as pessoas
Status Code 200


#### GET /persons/sales-opportunity
Retornas as pessoas que tem uma possível oportunidade de compra.
Status Code 200


#### POST /cars/
Cria um novo carro
Status Code 201

```JSON
{
    "color": 1,
    "type": 1,
    "person": 1 
}
```

#### GET /cars/
Retorna todos os carros Status Code 200


## Comandos curtos
make venv

make init-dev

make init-prd 

make test

make migrations

make migrate

make dev 

make clean
