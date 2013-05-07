# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import unittest
from google.appengine.ext import testbed
from core.usuario import seguranca
from core.usuario.model import Usuario


@seguranca.usuario_logado
def handle_stub():
    return "stub executado"

class HandlerStub():
    def redirect(self,url):
        self.url=url

GOOGLE_ID="12"
class GoogleUserMock():
    def user_id(self):
        return GOOGLE_ID

class SegurancaTests(unittest.TestCase):
    #CRIA UMA INSTACIA DO BANCO POR TESTE
    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.setup_env(app_id="_")
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_user_stub()
        self.testbed.init_urlfetch_stub()
        self.testbed.init_memcache_stub()
        self.testbed.init_mail_stub()
        self.testbed.init_taskqueue_stub()

    def tearDown(self):
        self.testbed.deactivate()

    def test_usuario_logado_decorator(self):
        #usuario nao logado no google
        seguranca.users.get_current_user= lambda : None
        handler=HandlerStub()
        handle_stub({},handler)
        #to do

        #logado no google
        seguranca.users.get_current_user= lambda : GoogleUserMock()
        handle_stub({},handler)
        self.assertEqual("/usuario/form",handler.url)

        #usuario ja cadastrado
        Usuario(user_name="Renzo",email="blah",google_id=GOOGLE_ID).put()
        retorno=handle_stub({},handler)
        self.assertEqual("stub executado",retorno)


