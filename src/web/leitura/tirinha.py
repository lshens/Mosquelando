# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json
from google.appengine.ext import ndb
from core.tirinha.model import Tirinha
from core.usuario import seguranca
from core.usuario.model import Usuario
from zen import router

@seguranca.usuario_logado
def form(write_tmpl):
    values={"save_url":router.to_path(salvar)}
    write_tmpl("/leitura/templates/tirinha_form.html",values)

def salvar(handler, img_tirinha, titulo_tirinha, legenda, avaliacao, data, usuario_id=None, id=None):
    #SE FOR UM ID NO RETORNO ENTÃO ELE SALVA
    if usuario_id is None:
        usuario_id = Usuario.current_user().key.id()
    usuario_id = long(usuario_id)
    usuario_key = ndb.Key(Usuario,usuario_id)
    if id:
       # data=str(date.today())
        tirinha = Tirinha(id=long(id), img_tirinha=img_tirinha, titulo_tirinha=titulo_tirinha, legenda=legenda,
                          avaliacao=avaliacao, data=data, usuario=usuario_key)
    #SE O  RETORNO NÃO FOR UM ID, POR EXEMPLO A URLSAFE ENTÃO FAZ O UPDATE
    else:
        tirinha = Tirinha(img_tirinha=img_tirinha, titulo_tirinha=titulo_tirinha, legenda=legenda,
                          avaliacao=avaliacao, data=data, usuario=usuario_key)
    #SALVA AS ALTERAÇÕES
    tirinha.put()
    #REDIRECIONA PARA O LISTAR
    handler.redirect(router.to_path(listar))


def listar(write_tmpl,usuario_id=None):
    if usuario_id is None:
        usuario_id = Usuario.current_user().key.id()
    usuario_id = long(usuario_id)
    usuario = Usuario.get_by_id(usuario_id)
    #VALORES QUE SERÃO PASSADOS NA URL
    values = {"list_url":router.to_path(listar_ajax,usuario)}
    #MONTA A PAGINA
    write_tmpl("/leitura/templates/tirinha_list.html",values)

def listar_ajax(resp,usuario_id, offset="0"):
    PAGE_SIZE=2
    usuario_id = long(usuario_id)
    usuario_key=ndb.Key(Usuario,usuario_id)
    #REALIZA A CONSULTA ORDENA POR ID
    query = Tirinha.query(Tirinha.usuario == usuario_key).order(Tirinha.key)
    #DEFINE O QUANTD DE RESULTADOS E O OFFSET
    offset=long(offset)
    tirinha =  query.fetch(PAGE_SIZE,offset=offset)
    #REALIZA O FOR PARA A LISTAGEM NO HTML MUSTACHE
    tirinha=[{"id":t.key.id(),"titulo":t.titulo_tirinha,"avaliacao":t.avaliacao,"urlsafe":t.key.urlsafe()} for t in tirinha]
    #ADD MAIS PAGE_SIZE A PAGINA
    offset+=PAGE_SIZE
    next_page_url=router.to_path(listar_ajax,offset)
    #VALORES QUE SERÃO PASSADOS NA URL
    dct = {"tirinha":tirinha,
           "nextPageUrl":next_page_url,
           "editar_url":router.to_path(editar),
           "apagar_url":router.to_path(apagar)}
    js=json.dumps(dct)
    resp.write(js)

def apagar(handler, id):
    #RECEBE O OBJETO MAIS O ID DELE
    key = ndb.Key(Tirinha,long(id))
    #DELETA O REGISTRO
    key.delete()
    #REDIRECIONA PARA A PAGINA LISTAR
    #handler.redirect(router.to_path(listar))

def editar(write_tmpl,urlsafe):
    #
    key =  ndb.Key(urlsafe=urlsafe)
    #PEGA A CHAVE PRIMARIA E ARMAZENA NA HISTORIA
    tirinha = key.get()
    #CARREGA O VALORES DA PK E MANDA PARA O SALVAR
    values = {"save_url":router.to_path(salvar),
              "tirinha":tirinha}
    write_tmpl("/leitura/templates/tirinha_form.html",values)
