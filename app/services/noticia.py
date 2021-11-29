from app.ormarModels import Noticia


async def putNoticia(id, body):
    try:
        noticia_db = await Noticia.objects.get(pk=id)
        if "link" in body:
            noticia_db.link = body["link"]
        await noticia_db.update()
        return {"message": "Notícia atualizada com sucesso!"}
    except Exception as e:
        return {"message": "Erro ao atualizar notícia!", "exception": str(e)}


async def deleteNoticia(id):
    try:
        noticia_db = await Noticia.objects.get(pk=id)
        await noticia_db.delete()
        return {"message": "Notícia deletada com sucesso!"}
    except Exception as e:
        return {"message": "Erro ao deletar notícia!", "exception": str(e)}
