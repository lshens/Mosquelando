# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext.blobstore import blobstore
from core.usuario import seguranca


@seguranca.usuario_logado
def index(write_tmpl):
    url = blobstore.create_upload_url("/upfile")
    values = {"url": url}
    write_tmpl("/upload/templates/upload.html",values)
