# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext.webapp import blobstore_handlers
import webapp2
from core.usuario.model import Usuario


class UploadHandler(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self):
        usuario=Usuario.current_user()
        self.send_blob(usuario.avatar)


app = webapp2.WSGIApplication([("/down", UploadHandler)], debug=False)
