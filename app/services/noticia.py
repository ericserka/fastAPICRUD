from app.ormarModels import Noticia


async def getNoticiaById(id):
    return await Noticia.objects.get(pk=id)
