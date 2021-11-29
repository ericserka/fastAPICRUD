from sqlalchemy_to_ormar import ormar_model_str_repr, sqlalchemy_to_ormar
from sqlAlchemyModels import Noticia, Pessoa
from app import database, metadata

OrmarNoticia = sqlalchemy_to_ormar(Noticia, database=database, metadata=metadata)
OrmarPessoa = sqlalchemy_to_ormar(Pessoa, database=database, metadata=metadata)
print(ormar_model_str_repr(OrmarNoticia))
print(ormar_model_str_repr(OrmarPessoa))
