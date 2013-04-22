# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from core.usuario.model import Usuario
from zen import router

def form(write_tmpl):
    values={"save_url":router.to_path(salvar)}
    write_tmpl("/usuario/templates/")

def salvar(handler, user_name, email, senha, avatar, id=None):
    #SE O ID NÃO EXISTIR ELE CRIA UM NOVO ID E REGISTRO
    if id:
        usuario = Usuario(id=long(id),user_name=user_name, email=email, senha=senha,avatar=avatar)
    #SE ELE POSSUIR UM ID, ELE REALIZA UM UPDATE DO RESGISTRO
    else:
        usuario = Usuario(user_name=user_name, email=email, senha=senha,avatar=avatar)
        #SALVA AS ALTERAÇÕES
    usuario.put()
    #REDIRECIONA PARA O LISTAR
    handler.redirect(router.to_path(listar))

def listar(write_tmpl):
    #REALIZA A CONSULTA PELOS ID MAIORES QUE 0 E ORDENA POR ID
    query = Usuario.query(Usuario.get_by_id>0).order(Usuario.get_by_id)
    #TRAZ SOMENTE 10 LINHAS DA CONSULTA
    usuario =  query.fetch(10)
    #VALORES QUE SERÃO PASSADOS NA URL
    values = {"usuario":usuario,
              "apagar_url":router.to_path(apagar),
              "editar_url":router.to_path(editar)}
    #MONTA A PAGINA
    write_tmpl()

def apagar(handler, id):
    #RECEBE O OBJETO MAIS O ID DELE
    key = ndb.Key(Usuario,long(id))
    #DELETA O REGISTRO
    key.delete()
    #REDIRECIONA PARA A PAGINA LISTAR
    handler.redirect(router.to_path(listar))

def editar(write_tmpl,urlsafe):
    #
    key =  ndb.Key(urlsafe=urlsafe)
    #PEGA A CHAVE PRIMARIA E ARMAZENA NA HISTORIA
    usuario = key.get()
    #CARREGA O VALORES DA PK E MANDA PARA O SALVAR
    values = {"save_url":router.to_path(salvar),
              "usuario":usuario}
    write_tmpl()
