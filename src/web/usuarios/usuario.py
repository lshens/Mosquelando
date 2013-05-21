# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.api import users
from google.appengine.ext import ndb
from core.usuario.model import Usuario
from zen import router

def form(write_tmpl,handler):
    google_user=users.get_current_user()
    usuario = Usuario.current_user()
    if usuario:
        handler.redirect("/")
    else:
        values={"url_salvar":router.to_path(salvar),
                "email":google_user.email()}
        write_tmpl("/usuarios/templates/usuario_form.html",values)


def salvar(handler, user_name, email):
    google_user = users.get_current_user()
    Usuario(user_name=user_name,email=email,google_id=google_user.user_id()).put()
    handler.redirect("/")

def listar(write_tmpl):
    #REALIZA A CONSULTA PELOS ID MAIORES QUE 0 E ORDENA POR ID
    query = Usuario.query().order(Usuario.key)
    #TRAZ SOMENTE 10 LINHAS DA CONSULTA
    usuario =  query.fetch(10)
    #VALORES QUE SERÃO PASSADOS NA URL
    values = {"usuario":usuario,
              "apagar_url":router.to_path(apagar),
              "editar_url":router.to_path(editar)}
    #MONTA A PAGINA
    write_tmpl("/usuarios/templates/usuario_list.html",values)

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
    write_tmpl("/usuarios/templates/usuario_form.html")
