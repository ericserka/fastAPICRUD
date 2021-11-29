from typing import List
from app import app
from app.ormarModels import Noticia
from app.utils.removeDictKeysWithNoneValues import removeDictKeysWithNoneValues
from app.services.noticia import deleteNoticia, putNoticia


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
    except Exception as e:
        return {"message": "Erro ao listar notícias!", "exception": str(e)}


@app.get("/noticia/{id}")
async def get_noticia(id):
    try:
        noticia_db = await Noticia.objects.fields(["id", "link"]).get(pk=id)
        return removeDictKeysWithNoneValues(noticia_db.dict())
    except Exception as e:
        return {"message": "Notícia não encontrada!", "exception": str(e)}


@app.post("/noticias")
async def create_noticia(noticia: Noticia):
    try:
        await noticia.save()
        return {"message": "Notícia criada com sucesso!"}
    except Exception as e:
        return {"message": "Erro ao criar notícia!", "exception": str(e)}


@app.put("/noticia/{id}")
async def update_noticia(id, noticia: Noticia):
    return await putNoticia(id, removeDictKeysWithNoneValues(noticia.dict()))


@app.delete("/noticia/{id}")
async def delete_noticia(id):
    return await deleteNoticia(id)
