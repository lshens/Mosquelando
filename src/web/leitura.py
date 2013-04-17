# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from zen import router

def index(write_tmpl):
    write_tmpl("tirinha/templates/tirinha_list.html")
