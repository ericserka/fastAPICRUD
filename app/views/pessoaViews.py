from typing import List
from app import app
from app.ormarModels import Pessoa
from app.utils.removeDictKeysWithNoneValues import removeDictKeysWithNoneValues
from app.services.pessoa import getPessoaById


@app.get(
    "/pessoas",
    response_model=List[Pessoa],
    response_model_exclude={"created_at", "updated_at"},
)
async def get_pessoas():
    try:
        return await Pessoa.objects.fields(["id", "nome"]).order_by("-created_at").all()
    except:
        return {"message": "Erro ao listar pessoas!"}


@app.get("/pessoa/{id}")
async def get_pessoa(id):
    try:
        pessoa_db = await Pessoa.objects.fields(["id", "nome"]).get(pk=id)
        return removeDictKeysWithNoneValues(pessoa_db.dict())
    except:
        return {"message": "Pessoa não encontrada!"}


@app.post("/pessoas")
async def create_pessoa(pessoa: Pessoa):
    try:
        await pessoa.save()
        return {"message": "Pessoa criada com sucesso!"}
    except:
        return {"message": "Erro ao criar Pessoa!"}


@app.put("/pessoa/{id}")
async def update_pessoa(id, pessoa: Pessoa):
    try:
        pessoa_db = await getPessoaById(id)
        body = removeDictKeysWithNoneValues(pessoa.dict())
        if "nome" in body:
            pessoa_db.nome = body["nome"]
        await pessoa_db.update()
        return {"message": "Pessoa atualizada com sucesso!"}
    except:
        return {"message": "Erro ao atualizar Pessoa!"}


@app.delete("/pessoa/{id}")
async def delete_pessoa(id):
    try:
        pessoa_db = await getPessoaById(id)
        await pessoa_db.delete()
        return {"message": "Pessoa deletada com sucesso!"}
    except:
        return {"message": "Erro ao deletar Pessoa!"}
