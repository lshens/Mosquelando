# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from google.appengine.ext.webapp import blobstore_handlers
import webapp2
from core.tirinha.model import Tirinha
from core.usuario.model import Usuario


class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        files = self.get_uploads()
        titulo_tirinha = self.request.get("titulo_tirinha")
        legenda = self.request.get("legenda")
        id = self.request.get("id")
        usuario_id = None

        if files:
            blob_key=files[0].key()
            if usuario_id is None:
                usuario_id = Usuario.current_user().key.id()
            usuario_id = long(usuario_id)
            usuario_key = ndb.Key(Usuario,usuario_id)
            if id:
                tirinha = Tirinha(id=long(id), img_tirinha=blob_key, titulo_tirinha=titulo_tirinha, legenda=legenda,
                                  usuario=usuario_key)
            else:
                tirinha = Tirinha(img_tirinha=blob_key, titulo_tirinha=titulo_tirinha, legenda=legenda,
                                  usuario=usuario_key)
            tirinha.put()
            self.redirect("/leitura/tirinha/listar_all")



app = webapp2.WSGIApplication([('/uptirinha', UploadHandler)], debug=False)
