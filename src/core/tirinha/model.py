# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.api import images
from google.appengine.ext import ndb
from google.appengine.ext.blobstore.blobstore import BlobInfo
from core.usuario.model import Usuario


class Tirinha(ndb.Model):
    titulo_tirinha = ndb.StringProperty(required=True)
    imgtirinha = ndb.BlobKeyProperty()
    legenda = ndb.StringProperty(required=True)
    avaliacao = ndb.StringProperty()
    data = ndb.DateTimeProperty(auto_now_add=True)
    usuario = ndb.KeyProperty(Usuario)

    def img(self, size=470):
        if self.imgtirinha:
            return images.get_serving_url(self.imgtirinha, size=size)
