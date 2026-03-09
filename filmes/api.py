from ninja import Router,File,Form
from .schema import ClienteSchema,ProgressoFilmeSchema,FilmeSquema
from .models import Clientes,Filmes
from ninja.errors import HttpError
from typing import List
from .filme import*
from datetime import date
from ninja.files import UploadedFile


filme_router=Router()

@filme_router.post('',response={200:ClienteSchema})
def add_cliente(request,
                cliente:ClienteSchema=Form(),
                cv:UploadedFile=File()
                ):
    
    nome=cliente.dict()['nome']
    email=cliente.dict()['email']
    senha=cliente.dict()['senha']
    idade=cliente.dict()['idade']
    cpf=cliente.dict()['cpf']
    sexo=cliente.dict()['sexo']
    qualidade=cliente.dict()['qualidade']
    dt_nascimento=cliente.dict()['dt_nascimento']
    image=cliente.dict()['image']
    

    if Clientes.objects.filter(email=email).exists():
        raise HttpError(400,'E-mail ja cadastrado')
    
    if Clientes.objects.filter(cpf=cpf).exists():
        raise HttpError(400,'cpf ja cadastrado')
    
    if len(senha)<8 or not senha:
        raise HttpError(400,'a senha deve ter no minimo 8 caracteres')
    
    
    with open(f"media/foto_perfil/{cv.size}-{cv.name}","wb+") as f:
        for chuk in cv.chunks():
            f.write(chuk)

 
    pessoa=Clientes(
        nome=nome,
        email=email,
        senha=senha,
        idade=idade,
        cpf=cpf,
        sexo=sexo,
        qualidade=qualidade,
        dt_nascimento=dt_nascimento,
        image=image

    )

    pessoa.save()
    return pessoa

    

@filme_router.get('/cliente/',response=List[ClienteSchema])
def list_user(request):

    cliente=Clientes.objects.all()

    return cliente


@filme_router.get('/progresso',response={200:ProgressoFilmeSchema})
def progresso_filme(request,cliente_email:str):

    cliente=Clientes.objects.get(email=cliente_email)
    filme_atual=cliente.get_qualidade_display()
    numero=order.get(filme_atual,0)
    total_filmes=calculate(numero)
    filme_concluido=Filmes.objects.filter(cliente=cliente,qd_filme=cliente.qualidade).count()
    filmes_faltantes=total_filmes-filme_concluido

    return{
        "email":cliente.email,
        "nome":cliente.nome,
        "idade":cliente.idade,
        "cpf":cliente.cpf, 
        "qualidade":cliente.qualidade,
        "total_filmes":filme_concluido,
        "filmes_necessarios":filmes_faltantes
    }

@filme_router.put('/update_user/{cliente_id}',response=ClienteSchema)
def update_user(request,cliente_id:int,cliente_data:ClienteSchema):

    cliente=Clientes.objects.get(id=cliente_id)
    idade=date.today() - cliente.dt_nascimento

    
    if int(idade.days/365) < 18 and cliente_data.dict()['qualidade'] in ('B','O','R'):
        raise HttpError(400,'Menores de 18 não pode assistir esse filme')
    
    
    for attr,value in cliente_data.dict().items():
        if value:
            setattr(cliente,attr,value)

    
    cliente.save()
    return cliente

@filme_router.delete('/delite_user/{user_id}',response={200:dict})
def delet_user(request,user_id:int):
    
    cliente=Clientes.objects.filter(id=user_id).first()

    if cliente:

        cliente.delete()
        return 200,{"message":"cliente removido com sucesso"}
    
    else:
        raise HttpError(404,"cliente não emcontrado")
    
'''
@filme_router.post('/asistido',response={200:str})
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
    
'''


    



    

    


    


    
