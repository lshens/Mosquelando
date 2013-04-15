__author__ = 'lucas.shen'
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb

class Historia(ndb.Model):
    img_meme=ndb.StringProperty;
    titulo=ndb.StringProperty;
    conteudo=ndb.StringProperty;
