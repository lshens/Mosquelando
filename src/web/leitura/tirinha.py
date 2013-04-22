# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json
from datetime import date
from google.appengine.ext import ndb
from core.tirinha.model import Tirinha
from zen import router


def form(write_tmpl):
    values={"save_url":router.to_path(salvar)}
    write_tmpl("/leitura/templates/tirinha_form.html",values)

def salvar(handler, img_tirinha, titulo_tirinha, legenda, avaliacao, data, id=None):
    #SE O ID NÃO EXISTIR ELE CRIA UM NOVO ID E REGISTRO
    if id:
       # data=str(date.today())
        tirinha = Tirinha(id=long(id), img_tirinha=img_tirinha, titulo_tirinha=titulo_tirinha, legenda=legenda,
                          avaliacao=avaliacao, data=data)
    #SE ELE POSSUIR UM ID, ELE REALIZA UM UPDATE DO RESGISTRO
    else:
        tirinha = Tirinha(img_tirinha=img_tirinha, titulo_tirinha=titulo_tirinha, legenda=legenda,
                          avaliacao=avaliacao, data=data)
    #SALVA AS ALTERAÇÕES
    tirinha.put()
    #REDIRECIONA PARA O LISTAR
    handler.redirect(router.to_path(listar))

def listar(write_tmpl):
    #REALIZA A CONSULTA PELOS ID MAIORES QUE 0 E ORDENA POR ID
    #query = Tirinha.query(Tirinha.get_by_id>0).order(Tirinha.get_by_id)
    #VALORES QUE SERÃO PASSADOS NA URL
    values = {"list_url":router.to_path(listar_ajax)}
              #"apagar_url":router.to_path(apagar),
             # "editar_url":router.to_path(editar)}
    #MONTA A PAGINA
    write_tmpl("/leitura/templates/tirinha_list.html",values)

def listar_ajax(resp, offset="0"):
    PAGE_SIZE=2
    #REALIZA A CONSULTA PELOS ID MAIORES QUE 0 E ORDENA POR ID
    query = Tirinha.query().order(Tirinha.key)
    #DEFINE O QUANTD DE RESULTADOS E O OFFSET
    offset=long(offset)
    tirinha =  query.fetch(PAGE_SIZE,offset=offset)
    #REALIZA O FOR PARA A LISTAGEM NO HTML MUSTACHE
    tirinha=[{"id":t.key.id(),"titulo":t.titulo_tirinha,"avaliacao":t.avaliacao} for t in tirinha]
    #ADD MAIS PAGE_SIZE A PAGINA
    offset+=PAGE_SIZE
    next_page_url=router.to_path(listar_ajax,offset)
    #VALORES QUE SERÃO PASSADOS NA URL
    dct = {"tirinha":tirinha,
           "nextPageUrl":next_page_url}
    js=json.dumps(dct)
    resp.write(js)

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
              "leitura":tirinha}
    write_tmpl()
