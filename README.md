# starwarsAPI

Este projeto é uma API sobre os planetas de Star Wars.
Feito em django rest framework, com banco de dados PostgreSQL e usando docker.

A proposta da API é a seguinte:
``` 
Para cada planeta, os seguintes dados devem ser obtidos do banco de dados da aplicação, 
sendo inserido manualmente:

· Nome
· Clima
· Terreno

E deve ter as seguintes funcionalidades:

- Adicionar um planeta (com nome, clima e terreno)
- Listar planetas
- Buscar por nome
- Buscar por ID
- Remover planeta 

- Para cada planeta também devemos ter a quantidade de aparições em filmes, 
que podem ser obtidas pela API pública do Star Wars: https://swapi.dev/
```

### Como executar?
Para executar este projeto, é necessário que tenha o docker instalado e seguir os seguintes passos:

- Executar o comando abaixo no terminal, posicionado na pasta do projeto
    - `docker-compose up`
- Em outra janela do terminal, executar o comando abaixo para pegar o id do container:
    - `docker ps`
- Na mesma janela, com o id do container, executar o comando abaixo alterando o <CONTAINER_ID>  pelo id do container:
    - `docker exec -t -i <CONTAINER_ID> bash`
- Ainda na mesma janela do terminal, executar o comando abaixo para realizar as migrações do banco de dados
    - `python manage.py migrate`
- Finalmente, fazer a requisição para o endereço abaixo:
    - `http://localhost:8000/planetas/`

### Exemplos de requisições

- Adicionar um novo planeta

```
POST http://localhost:8000/planetas/

BODY
{
    "nome": "Dagobah",
    "clima": "CO",
    "terreno": "Deserto"
}
```
Possível resposta:
```
HTTP/1.1 201 CREATED
{
    "id": 4,
    "filmes": 2,
    "nome": "Alderaan",
    "clima": "CO",
    "terreno": "DE"
}
```
Em caso de tentar adicionar um planeta com nome já existente, é exibida a resposta abaixo:
```
HTTP/1.1 400 BAD REQUEST
{
    "nome": [
        "planeta with this nome already exists."
    ]
}
```
Em caso de tentar escolher um clima ou terreno fora da lista pré-definida (abaixo), será exibida a resposta abaixo:
```
HTTP/1.1 400 BAD REQUEST
{
    "clima": [
        "\"clima_teste\" is not a valid choice."
    ],
    "terreno": [
        "\"terreno_teste\" is not a valid choice."
    ]
}
```
Lista de terrenos e climas:
```
Clima:
CO = Congelado 
TR = Tropical
TE = Temperado
AR = Árido

Terreno:
DE = Deserto
OC = Oceano
FL = lorestas
MO = Montanhoso
TU = Tundra
PA = Pantano
```

- Listar todos os planetas
```
GET http://localhost:8000/planetas/
```

Possível resposta:
```
HTTP/1.1 200 OK
[
    {
        "id": 1,
        "filmes": 3,
        "nome": "Dagobah",
        "clima": "CO",
        "terreno": "Deserto"
    },
    {
        "id": 2,
        "filmes": 5,
        "nome": "Tatooine",
        "clima": "CO",
        "terreno": "DE"
    }
]
```

- Buscar um planeta por ID
```
GET http://localhost:8000/planetas/1

HTTP/1.1 200 OK
{
    "id": 1,
    "filmes": 3,
    "nome": "Dagobah",
    "clima": "CO",
    "terreno": "Deserto"
}
```


- Buscar um planeta por nome
```
GET http://localhost:8000/planeta/Dagobah

HTTP/1.1 200 OK
{
    "id": 1,
    "filmes": 3,
    "nome": "Dagobah",
    "clima": "CO",
    "terreno": "Deserto"
}
```

- Excluir um planeta
```
DELETE /planetas/3/

HTTP/1.1 204 NO CONTENT
```