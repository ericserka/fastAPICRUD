from app import database, metadata
import ormar
from sqlalchemy import text
from datetime import datetime


# nullable = True torna o field not required; eh util na hora do PUT para nao ser obrigado a sempre passar todos os fields


class Noticia(ormar.Model):
    class Meta(ormar.ModelMeta):
        metadata = metadata
        database = database
        tablename = "noticia"

    id = ormar.Integer(primary_key=True)
    link = ormar.String(max_length=255, nullable=True)
    updated_at = ormar.DateTime(server_default=text("CURRENT_TIMESTAMP"))
    created_at = ormar.DateTime(server_default=text("CURRENT_TIMESTAMP"))


class Pessoa(ormar.Model):
    class Meta(ormar.ModelMeta):
        metadata = metadata
        database = database
        tablename = "pessoa"

    id = ormar.Integer(primary_key=True)
    nome = ormar.String(max_length=255, nullable=True)
    created_at = ormar.DateTime(server_default=text("CURRENT_TIMESTAMP"))
    updated_at = ormar.DateTime(server_default=text("CURRENT_TIMESTAMP"))


@ormar.pre_update([Noticia, Pessoa])
async def before_update(instance, **kwargs):
    instance.updated_at = datetime.now()
