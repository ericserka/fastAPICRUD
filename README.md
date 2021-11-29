# FastAPI CRUD (PostgreSQL)

- Instalando os pacotes pip: ```pip install -r requirements.txt```
- Formatando o código: ```black .```
- Configurar o banco de dados usando o ```.env``` a partir do ```.env.example```
- Criando models SQLAlchemy a partir de um banco de dados existente: ```sqlacodegen --schema sihab postgresql://<database_user>:<database_password>@<database_host>/<database_name>```. Esse comando vai printar as classes no terminal, criei um arquivo chamado ```sqlAlchemyModels.py``` e colei o código nele. Depois disso criei o arquivo ```sqlAlchemyToOrmar.py``` e rodei ele executando ```python3.9 sqlAlchemyToOrmar.py```. O código vai printar os models correspondentes do ```ormar```. Salvei esse código no arquivo ```ormarModels.py``` (com modificações porque o código gerado não está perfeitamente correto).
- Startando o servidor: ```uvicorn run:app --reload```