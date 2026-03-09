from django.db import models

qualidade_choices=(
    ('B','Bom'),
    ('R','Ruin'),
    ('O','Otimo')
)

class Clientes(models.Model):
    nome=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    cpf=models.CharField(max_length=20)
    senha=models.CharField(max_length=10)
    idade=models.IntegerField(default=10)
    sexo=models.CharField(max_length=255)
    qualidade=models.CharField(max_length=1,choices=qualidade_choices,default='B')
    dt_nascimento=models.DateField(null=True,blank=True)
    image=models.ImageField(upload_to='foto_perfil',null=True,blank=True)

    def __str__(self):
        return self.nome
    
class Filmes(models.Model):
    cliente=models.ForeignKey(Clientes,on_delete=models.CASCADE)
    nome_filme=models.CharField(max_length=255)
    episodios=models.CharField(max_length=255)
    qd_filme=models.CharField(max_length=1,choices=qualidade_choices,default='O')
    valor=models.DecimalField(max_digits=10,decimal_places=2)
    temporada=models.CharField(max_length=255)
    sobre=models.TextField(blank=True,null=True)
    dt_lancamento=models.DateField(null=True,blank=True)

    def __str__(self):
        return self.cliente.nome
    

    
