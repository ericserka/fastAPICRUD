from sqlalchemy import Column, DateTime, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Noticia(Base):
    __tablename__ = "noticia"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('noticia_id_seq'::regclass)"),
    )
    link = Column(String(255), nullable=False)
    updated_at = Column(
        DateTime(True), nullable=False, server_default=text("CURRENT_TIMESTAMP")
    )
    created_at = Column(
        DateTime(True), nullable=False, server_default=text("CURRENT_TIMESTAMP")
    )


class Pessoa(Base):
    __tablename__ = "pessoa"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('pessoa_id_seq'::regclass)"),
    )
    nome = Column(String(255), nullable=False)
    created_at = Column(
        DateTime(True), nullable=False, server_default=text("CURRENT_TIMESTAMP")
    )
    updated_at = Column(
        DateTime(True), nullable=False, server_default=text("CURRENT_TIMESTAMP")
    )
