from ninja import Router
from .schema import FilmeSquema
from ninja.errors import HttpError
from .models import Clientes,Filmes
from typing import List

api_filme=Router()


@api_filme.post('/asistido',response={200:str})
def filme_asistido(request,assistido:FilmeSquema):


    qtd=assistido.dict()['qtd']
    email_cliente=assistido.dict()['email_cliente']
    valor=assistido.dict()['valor']
    n_filme=assistido.dict()['nome_filme']
    ep_sodio=assistido.dict()['episodios']
    temporada=assistido.dict()['temporada']
    sobre=assistido.dict()['sobre']
    dt_lancamento=assistido.dict()['dt_lancamento']

    if qtd<=0:
        raise HttpError(400,'Quantidade de filme deve ser maior qui zero')
    
    
    try:

        cliente=Clientes.objects.get(email=email_cliente)

    except Clientes.DoesNotExist:
        raise HttpError(404,"Cliente com esse email não emcontrado")
    

    for _ in range(0,qtd):
        ass=Filmes(
            cliente=cliente,
            qd_filme=cliente.qualidade,
            valor=valor,
            nome_filme=n_filme,
            episodios=ep_sodio,
            temporada=temporada,
            sobre=sobre,
            dt_lancamento=dt_lancamento
        )

        ass.save()
        return 200,f"filme marcado como assistido para {cliente.nome}"
    
@api_filme.get('/list',response=List[FilmeSquema])   
def list_tdfilme(request):

    filme=Filmes.objects.all()
    return filme



@api_filme.get('/unicfilme',response={200:FilmeSquema})
def list_unicfilme(request,filme_id:int):

    try:
        filme=Filmes.objects.get(id=filme_id)

        return{
            'nome_filme':filme.nome_filme,
            'episodios':filme.episodios,
            'qd_filme':filme.qd_filme,
            'valor':filme.valor,
            'temporada':filme.temporada,
            'sobre':filme.sobre,
            'dt_lancamento':filme.dt_lancamento
    }
    except Filmes.DoesNotExist:
        raise HttpError(404,'Filme não emcontrado')


   


@api_filme.put('/unicfilme{filme_id}',response=FilmeSquema)
def update_filme(request,filme_id:int,filme_data:FilmeSquema):

    filme=Filmes.objects.get(id=filme_id)

    for attr,value in filme_data.dict().items():
        if value:
            setattr(filme,attr,value)

    filme.save()
    return filme


@api_filme.delete('/delitfilme{id_filme}',response={200:dict})
def delit_filme(request,id_filme:int):

    filme=Filmes.objects.filter(id=id_filme).first()

    if filme:
        filme.delete()
        return 200,{"message":"filme removido com sucesso"}
    else:
        raise HttpError(404,'Filme não emcontrado')








    
