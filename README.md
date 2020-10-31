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
- Finalmente, executar o comando abaixo para realizar as migrações do banco de dados
    - `python manage.py migrate`