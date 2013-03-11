# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from web import formulario
from zen import router


def index(write_tmpl):
    write_tmpl("/templates/home.html")
