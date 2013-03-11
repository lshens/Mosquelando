# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals




def index(write_tmpl):
    write_tmpl("/templates/form.html")

def salvar(resp,nome,lg="c",**kwargs):
    resp.write("Executou form nome=%s, lg=%s outros args= %s"%(nome,lg, kwargs))


