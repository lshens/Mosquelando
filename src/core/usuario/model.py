__author__ = 'lucas.shen'
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb

class Usuario(ndb.Model):
    user_name=ndb.StringProperty;
    email=ndb.StringProperty;
    senha=ndb.StringProperty;
    avatar=ndb.StringProperty;
