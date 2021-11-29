from typing import List
from app import app
from app.ormarModels import Pessoa
from app.utils.removeDictKeysWithNoneValues import removeDictKeysWithNoneValues
from app.services.pessoa import putPessoa, deletePessoa


@app.get(
    "/pessoas",
    response_model=List[Pessoa],
    response_model_exclude={"created_at", "updated_at"},
)
async def get_pessoas():
    try:
        return await Pessoa.objects.fields(["id", "nome"]).order_by("-created_at").all()
    except Exception as e:
        return {"message": "Erro ao listar pessoas!", "exception": str(e)}


@app.get("/pessoa/{id}")
async def get_pessoa(id):
    try:
        pessoa_db = await Pessoa.objects.fields(["id", "nome"]).get(pk=id)
        return removeDictKeysWithNoneValues(pessoa_db.dict())
    except Exception as e:
        return {"message": "Pessoa não encontrada!", "exception": str(e)}


@app.post("/pessoas")
async def create_pessoa(pessoa: Pessoa):
    try:
        await pessoa.save()
        return {"message": "Pessoa criada com sucesso!"}
    except Exception as e:
        return {"message": "Erro ao criar Pessoa!", "exception": str(e)}


@app.put("/pessoa/{id}")
async def update_pessoa(id, pessoa: Pessoa):
    return await putPessoa(id, removeDictKeysWithNoneValues(pessoa.dict()))


@app.delete("/pessoa/{id}")
async def delete_pessoa(id):
    return await deletePessoa(id)
