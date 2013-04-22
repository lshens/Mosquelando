# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb

class Memes(ndb.Model):
    img_meme = ndb.StringProperty;
    titulo = ndb.StringProperty;
    conteudo = ndb.StringProperty;
