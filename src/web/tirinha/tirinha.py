__author__ = 'Shen'

from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from core.historia.model import Historia
from zen import router

def form(write_tmpl):
    values={"save_url":router.to_path(salvar)}
    write_tmpl("/historia/templates/")

def salvar(handler, img_meme,titulo, conteudo, id=None):
    #SE O ID NÃO EXISTIR ELE CRIA UM NOVO ID E REGISTRO
    if id:
        historia = Historia(id=long(id), img_meme=img_meme, titulo=titulo, conteudo=conteudo)
    #SE ELE POSSUIR UM ID, ELE REALIZA UM UPDATE DO RESGISTRO
    else:
        historia = Historia(img_meme=img_meme, titulo=titulo, conteudo=conteudo)
        #SALVA AS ALTERAÇÕES
    historia.put();
    #REDIRECIONA PARA O LISTAR
    handler.redirect(router.to_path(listar))

def listar(write_tmpl):
    #REALIZA A CONSULTA PELOS ID MAIORES QUE 0 E ORDENA POR ID
    query = Historia.query(Historia.get_by_id>0).order(Historia.get_by_id)
    #TRAZ SOMENTE 10 LINHAS DA CONSULTA
    historia =  query.fetch(10)
    #VALORES QUE SERÃO PASSADOS NA URL
    values = {"historia":historia,
              "apagar_url":router.to_path(apagar),
              "editar_url":router.to_path(editar)}
    #MONTA A PAGINA
    write_tmpl()

def apagar(handler, id):
    #RECEBE O OBJETO MAIS O ID DELE
    key = ndb.Key(Historia,long(id))
    #DELETA O REGISTRO
    key.delete()
    #REDIRECIONA PARA A PAGINA LISTAR
    handler.redirect(router.to_path(listar))

def editar(write_tmpl,urlsafe):
    #
    key =  ndb.Key(urlsafe=urlsafe)
    #PEGA A CHAVE PRIMARIA E ARMAZENA NA HISTORIA
    historia = key.get()
    #CARREGA O VALORES DA PK E MANDA PARA O SALVAR
    values = {"save_url":router.to_path(salvar),
              "historia":historia}
    write_tmpl()
