from django.forms import ModelForm
from app.models import Filmes

# Create the form class.
class FilmesForm(ModelForm):
    class Meta:
        model = Filmes
        fields = ['nome', 'diretor', 'genero' , 'ano']
