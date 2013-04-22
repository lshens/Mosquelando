# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb

class Tirinha(ndb.Model):
    titulo_tirinha = ndb.StringProperty(required=True);
    img_tirinha = ndb.StringProperty(required=True);
    legenda = ndb.StringProperty(required=True);
    avaliacao = ndb.StringProperty(required=True);
    data = ndb.StringProperty(required=True);
