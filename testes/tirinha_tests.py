# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import unittest
import json
from google.appengine.ext import testbed
from core.tirinha.model import Tirinha
from core.web import tmpl
from web.leitura import tirinha
from zen import router

class HandlerMock(object):
    def redirect(self, url):
        self.url = url

class WriterMock(object):
    def write(self, json):
        self.json = json

class TirinhaTests(unittest.TestCase):
    #CRIA UMA INSTACIA DO BANCO POR TESTE
    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()

    def tearDown(self):
        self.testbed.deactivate()

    def test_salvar(self):
        handler = HandlerMock()
        tirinha.salvar(handler,"C:\Tirinha.jpg","Sensualizando","Esse cara tem mais teta do que umas amigas minhas…","0","20/06/92")
        salvo = Tirinha.query().get()
        self.assertEquals("C:\Tirinha.jpg",salvo.img_tirinha)
        self.assertEquals("Sensualizando",salvo.titulo_tirinha)
        self.assertEquals("Esse cara tem mais teta do que umas amigas minhas…",salvo.legenda)
        self.assertEquals("0",salvo.avaliacao)
        self.assertEquals("20/06/92",salvo.data)
        url = router.to_path(tirinha.listar)
        self.assertEquals(url, handler.url)

    def test_listar(self):
        def write_tmpl(tmpl_name, dct):
            self.tmpl_name = tmpl_name
            self.values = dct
            tmpl.render(tmpl_name, dct)

        tirinha.listar(write_tmpl)
        self.assertEquals("/leitura/templates/tirinha_list.html",self.tmpl_name)
        self.assertDictEqual({"list_url":router.to_path(tirinha.listar_ajax)},self.values)

    def test_editar(self):
        salvo = Tirinha(img_tirinha="1", titulo_tirinha="2", legenda="3", avaliacao="4", data="5")
        salvo.put()
        handler = HandlerMock()
        id = salvo.key.id()
        tirinha.salvar(handler,"C:\Tirinha.jpg","Sensualizando","Esse cara tem mais teta do que umas amigas minhas…","0","20/06/92",str(id))
        salvo = Tirinha.query().get()
        self.assertEquals("C:\Tirinha.jpg",salvo.img_tirinha)
        self.assertEquals("Sensualizando",salvo.titulo_tirinha)
        self.assertEquals("Esse cara tem mais teta do que umas amigas minhas…",salvo.legenda)
        self.assertEquals("0",salvo.avaliacao)
        self.assertEquals("20/06/92",salvo.data)

    def test_listar_ajax(self):
        resp = WriterMock()
        tirinha.listar_ajax(resp)
        jsonCompara = json.loads(resp.json)
        self.assertDictEqual({"tirinha":[],
                              "nextPageUrl":router.to_path(tirinha.listar_ajax,2),
                              "editar_url":router.to_path(tirinha.editar),
                              "apagar_url":router.to_path(tirinha.apagar)},
                              jsonCompara)









