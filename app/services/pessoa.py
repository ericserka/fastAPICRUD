from app.ormarModels import Pessoa


async def putPessoa(id, body):
    try:
        pessoa_db = await Pessoa.objects.get(pk=id)
        if "nome" in body:
            pessoa_db.nome = body["nome"]
        await pessoa_db.update()
        return {"message": "Pessoa atualizada com sucesso!"}
    except Exception as e:
        return {"message": "Erro ao atualizar pessoa!", "exception": str(e)}


async def deletePessoa(id):
    try:
        pessoa_db = await Pessoa.objects.get(pk=id)
        await pessoa_db.delete()
        return {"message": "Pessoa deletada com sucesso!"}
    except Exception as e:
        return {"message": "Erro ao deletar pessoa!", "exception": str(e)}
