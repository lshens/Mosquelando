# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from core.usuario.model import Usuario


class Tirinha(ndb.Model):
    titulo_tirinha = ndb.StringProperty(required=True)
    img_tirinha = ndb.BlobKeyProperty
    legenda = ndb.StringProperty(required=True)
    avaliacao = ndb.StringProperty(required=True)
    data = ndb.DateTimeProperty(auto_now_add=True)
    usuario = ndb.KeyProperty(Usuario,required=True)
