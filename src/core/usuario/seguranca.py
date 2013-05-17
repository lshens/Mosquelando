# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.api import users
from core.usuario.model import Usuario
from core.web import decorator_util
from web.usuarios import usuario
from zen import router

red = usuario.form
def usuario_logado(fcn):
    def wrapper(_dependencias,handler,*args,**kwargs):
        usuario=Usuario.current_user()
        if usuario:
            novos_argumentos = decorator_util.find_dependencies(_dependencias,fcn)
            novos_argumentos.extend(args)
            return fcn(*novos_argumentos,**kwargs)
        google_user=users.get_current_user()
        if google_user:
            handler.redirect(router.to_path(red))
        else:
            url=router.to_path(fcn,*args)
            login_url=users.create_login_url(url)
            handler.redirect(login_url)
    return wrapper
