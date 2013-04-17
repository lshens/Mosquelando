from xmlrpclib import DateTime

__author__ = 'Shen'

from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from core.tirinha.model import Tirinha
from datetime import datetime
from zen import router

def form(write_tmpl):
    values={"save_url":router.to_path(salvar)}
    write_tmpl("/historia/templates/")

def salvar(handler, img_tirinha, titulo_tirinha, legenda, avaliacao, data, id=None):
    #SE O ID NÃO EXISTIR ELE CRIA UM NOVO ID E REGISTRO
    data=datetime.today()
    if id:
        avaliacao=long(avaliacao)
        avaliacao=0
        tirinha = Tirinha(id=long(id), img_tirinha=img_tirinha, titulo_tirinha=titulo_tirinha, legenda=legenda,
                          avaliacao=avaliacao, data=data)
    #SE ELE POSSUIR UM ID, ELE REALIZA UM UPDATE DO RESGISTRO
    else:
        tirinha = Tirinha(img_tirinha=img_tirinha, titulo_tirinha=titulo_tirinha, legenda=legenda,
                          avaliacao=long(avaliacao), data=data)
        #SALVA AS ALTERAÇÕES
    tirinha.put();
    #REDIRECIONA PARA O LISTAR
    handler.redirect(router.to_path(listar))

def listar(write_tmpl):
    #REALIZA A CONSULTA PELOS ID MAIORES QUE 0 E ORDENA POR ID
    query = Tirinha.query(Tirinha.get_by_id>0).order(Tirinha.get_by_id)
    #TRAZ SOMENTE 10 LINHAS DA CONSULTA
    tirinha =  query.fetch(5)
    #VALORES QUE SERÃO PASSADOS NA URL
    values = {"tirinha":tirinha,
              "apagar_url":router.to_path(apagar),
              "editar_url":router.to_path(editar)}
    #MONTA A PAGINA
    write_tmpl()

def apagar(handler, id):
    #RECEBE O OBJETO MAIS O ID DELE
    key = ndb.Key(Tirinha,long(id))
    #DELETA O REGISTRO
    key.delete()
    #REDIRECIONA PARA A PAGINA LISTAR
    handler.redirect(router.to_path(listar))

def editar(write_tmpl,urlsafe):
    #
    key =  ndb.Key(urlsafe=urlsafe)
    #PEGA A CHAVE PRIMARIA E ARMAZENA NA HISTORIA
    tirinha = key.get()
    #CARREGA O VALORES DA PK E MANDA PARA O SALVAR
    values = {"save_url":router.to_path(salvar),
              "tirinha":tirinha}
    write_tmpl()
