
# Django, React, Docker & TDD



## Stack utilizada
**Back-end:** Django, Django Rest Framework, Django-Cors, Django Simple JWT, PostGresQL


## Rodando a aplicação

Faça uma copia do arquivo .env.example com o nome de .env

```bash
  cp .env.example .env
```

Carregue as variaveis no ambiente do sistema operacional
```bash
source .env
```

Crie um super usuario no django para ter acesso aos carros, pessoas e oportunidades de venda.
```bash
docker-compose exec django python manage.py createsuperuser
```

Rode o banco de dados, servidor e web com o docker-compose
```bash
docker-compose up -d
```
