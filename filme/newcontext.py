from .models import Filme


def lista_filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by("-data_criacao")[0:12]
    if lista_filmes:
        filme_destaque = lista_filmes[0]
    else:
        filme_destaque = None
    return {"lista_filmes_recentes": lista_filmes, "filme_destaque": filme_destaque}


def lista_filmes_secao2(request):
    lista_filmes = Filme.objects.all().order_by("-data_criacao")[4:8]
    return {"lista_filmes_secao2": lista_filmes}


def lista_filmes_maisvistos(request):
    lista_filmes = Filme.objects.all().order_by("-visualizacoes")[0:12]
    return {"lista_filmes_maisvistos": lista_filmes}


def lista_filmes_mvsecao2(request):
    lista_filmes = Filme.objects.all().order_by("-visualizacoes")[4:8]
    return {"lista_filmes_mvsecao2": lista_filmes}
