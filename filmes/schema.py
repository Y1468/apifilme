
from ninja import ModelSchema,Schema,File
from .models import Clientes,Filmes
from typing import Optional
from datetime import date


class ClienteSchema(ModelSchema):
    class Meta:
        model=Clientes
        fields=['nome','email','cpf','senha','idade','sexo','qualidade','dt_nascimento','image']

class ProgressoFilmeSchema(Schema):
    nome:str
    email:str
    idade:int
    cpf:str
    qualidade:str
    total_filmes:int
    filmes_necessarios:int

class FilmeSquema(Schema):
    qtd:Optional[int]=1
    #email_cliente:str
    valor:float
    nome_filme:str
    episodios:str
    temporada:str
    qd_filme:str
    sobre:Optional[str]
    dt_lancamento:Optional[date]

    


    
    


    



