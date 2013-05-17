# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext.webapp import blobstore_handlers
import webapp2
from core.usuario.model import Usuario


class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        files = self.get_uploads()
        if files:
            blob_key=files[0].key()
            usuario = Usuario.current_user()
            usuario.avatar = blob_key
            usuario.put()
            self.redirect("/")


app = webapp2.WSGIApplication([('/upfile', UploadHandler)], debug=False)
