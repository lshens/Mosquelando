# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb

class Tirinha(ndb.Model):
    titulo_tirinha=ndb.StringProperty;
    img_tirinha=ndb.StringProperty;
    legenda=ndb.StringProperty;
    avalicao=ndb.IntegerProperty;
    data=ndb.StringProperty;
