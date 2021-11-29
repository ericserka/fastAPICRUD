from typing import List
from app import app
from app.ormarModels import Noticia
from app.utils.removeDictKeysWithNoneValues import removeDictKeysWithNoneValues
from app.services.noticia import getNoticiaById


@app.get(
    "/noticias",
    response_model=List[Noticia],
    response_model_exclude={"created_at", "updated_at"},
)
async def get_noticias():
    try:
        return (
            await Noticia.objects.fields(["id", "link"]).order_by("-created_at").all()
        )
    except:
        return {"message": "Erro ao listar notícias!"}


@app.get("/noticia/{id}")
async def get_noticia(id):
    try:
        noticia_db = await Noticia.objects.fields(["id", "link"]).get(pk=id)
        return removeDictKeysWithNoneValues(noticia_db.dict())
    except:
        return {"message": "Notícia não encontrada!"}


@app.post("/noticias")
async def create_noticia(noticia: Noticia):
    try:
        await noticia.save()
        return {"message": "Notícia criada com sucesso!"}
    except:
        return {"message": "Erro ao criar notícia!"}


@app.put("/noticia/{id}")
async def update_noticia(id, noticia: Noticia):
    try:
        noticia_db = await getNoticiaById(id)
        body = removeDictKeysWithNoneValues(noticia.dict())
        if "link" in body:
            noticia_db.link = body["link"]
        await noticia_db.update()
        return {"message": "Notícia atualizada com sucesso!"}
    except:
        return {"message": "Erro ao atualizar notícia!"}


@app.delete("/noticia/{id}")
async def delete_noticia(id):
    try:
        noticia_db = await getNoticiaById(id)
        await noticia_db.delete()
        return {"message": "Notícia deletada com sucesso!"}
    except:
        return {"message": "Erro ao deletar notícia!"}
