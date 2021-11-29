from app.ormarModels import Pessoa


async def getPessoaById(id):
    return await Pessoa.objects.get(pk=id)
