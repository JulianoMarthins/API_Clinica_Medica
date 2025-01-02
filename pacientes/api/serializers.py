from rest_framework import serializers
from pacientes.models import Pacientes

class PacientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pacientes # utilizada o arquivo model do Paciente como padrão
        fields = '__all__'


    """
            
            A classe Meta está recebendo em seu atributo model, Pacientes, isso significa que
        que estamos tornando padrão o arquivo models do pacote paciente.
        
            O atributo fields será setado como "__all__" ordenando assim que utilizemos todos
        os atributos contidos em models, caso desejamos pegar atributos específicos, devemos
        passar uma lista ou tupo de strings com os nomes dos atributos desejados. 
    
    
    """