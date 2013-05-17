# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.api import users, images
from google.appengine.ext import ndb

class Usuario(ndb.Model):
    user_name = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    google_id = ndb.StringProperty(required=True)
    avatar=ndb.BlobKeyProperty()

    @classmethod
    def current_user(cls):
        user = users.get_current_user()
        if user:
            return Usuario.query(Usuario.google_id == user.user_id()).get()

    def avatar_img(self,size=15):
        if self.avatar:
            return images.get_serving_url(self.avatar,size=size)