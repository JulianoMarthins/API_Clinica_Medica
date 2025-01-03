from django.db import models

# Create your models here.

class Pacientes(models.Model):

    id_paciente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nascimento = models.DateField(blank=True, null=True)
    endereco = models.CharField(max_length=80, blank=True, null=True)
    num_endereco = models.IntegerField(blank=True, null=True)
    bairro = models.CharField(max_length=60, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)
    data_cadastro = models.DateField(auto_now=True)
    rg = models.CharField(max_length=100, blank=True, null=True)


    class Meta:
        managed = True # Significa que a table poderá ser trabalhada pelo programador
        db_table = 'pacientes' # O nome da tabela será pacientes.




    """
        Observações para fins didáticos.
    
        O 'id_paciente' utilizada um método de models para auto incrementar valores para a 
    id do paciente, em seu argumento, tornamos esta id como chave primária para o banco de
    dados
    
    
        Durante a criação dos atributos da classe, utilizamos nos argumentos o valor TRUE para 
    os parâmetros blank e null, estes significam que o atributo pode ser deixado em branco ou 
    nulo durante o preenchimento do cadastro do cliente. 
    
        A data de cadastro utilizada a função DateField, onde seu parâmetro auto_now faz com 
    que a data do dia em que o cliente seja cadastrado, seja armazenado no banco de dados.
        
        
        Dentro do arquivo models, passamos os atributos da classe, neste caso, da classe cliente, 
    passamos todos os dados que queremos receber e armazenar no banco de dados, para poder
    cadastrar um cliente em nosso sistema.
        Campos como id, nome, endereço, rg, cpf, aniversário, são exemplo de atributos que a 
    classe cliente pode receber e que serão uteis a nosso sistema, logo, podemos classificar o 
    arquivo models como os atributos do objeto que serão salvos no banco de dados do nosso 
    sistema. 
        
    
    """
