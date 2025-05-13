# sistema_cognitivo_api
API de consulta de dados para o sistema cognitivo

## Dependencias
É necessário instalar algumas dependências na sua máquina para que tudo rode corretamente, sendo elas:

- Python: [Download Python](https://www.python.org/downloads/)
- Docker Compose: [Instruções de instalação](https://docs.docker.com/compose/install/)

## Configuração de ambiente e outras dependências
Após rodar a primeira vez, não é necessário rodar novamente o comando a seguir:
```bash
python -m venv .venv
```

Configure o ambiente virtual e instale as dependências do python com os comandos a seguir:
```bash
.venv\Scripts\activate  # Para Windows
source .venv/bin/activate  # Para Linux/MacOS
pip install -r requirements.txt
```

## Variáveis de ambiente
Crie um arquivo .env na raiz do projeto com as variáveis necessárias:
```bash
MONGO_USERNAME=admin
MONGO_PASSWORD=secret
MONGO_HOST=localhost
MONGO_PORT=27017
MONGO_DB=meu_banco
```

## Rodando o projeto
Para iniciar o docker que contém o banco, é necessário rodar o seguinte comando que já populará o banco com alguns dados de um dump presente no projeto:
```bash
docker compose up
```

Para inicializar a aplicação é necessário rodar o seguinte comando:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## Documentação com swagger
Após inicializada, é possível acessar uma documentação completa feita pelo swagger, que estará disponível no seguinte link:
http://localhost:8000/docs

