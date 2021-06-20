from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer

from django.shortcuts import get_object_or_404
from app.forms import FilmesForm
from app.models import Filmes


class FilmesResource(DjangoResource):
    preparer = FieldsPreparer(fields={
        'id': 'id',
        'nome': 'nome',
        'diretor': 'diretor',
        'genero' : 'genero',
        'ano' : 'ano',
    })

    def list(self):
        return Filmes.objects.all()

    def create(self):
        return Filmes.objects.create(
            nome=self.data['nome'],
            diretor=self.data['diretor'],
            genero=self.data['genero'],
            ano=self.data['ano'],
        )

    def detail(self, pk):
        return get_object_or_404(Filmes, pk=pk)

    def update(self, pk):
        Filmes = self.detail(pk)

        Filmes.nome = self.data['nome']
        Filmes.diretor = self.data['diretor']
        Filmes.genero = self.data['genero']
        Filmes.ano = self.data['ano']
        Filmes.save()

        return Filmes

    def delete(self, pk):
        Filmes = self.detail(pk)
        Filmes.delete()


    def is_authenticated(self):
        return True
