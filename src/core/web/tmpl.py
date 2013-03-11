import jinja2
import os
from zen.dataprocess import filters

_base=os.path.abspath(os.path.join(os.path.dirname(__file__),"../.."))
_base=os.path.join(_base,"web")



#def templatedirs():
#    basedir=os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
#    basedirs=os.listdir(basedir)
#    possibledirs=[basedir+"/"+m+"/templates/html" for m in basedirs]
#    possibledirs+=[basedir+"/"+m+"/templates/xml" for m in basedirs]
#    possibledirs+=[basedir+"/"+m+"/templates/txt" for m in basedirs]
#    dirs=[d for d in possibledirs if os.path.exists(d)]
#    return dirs
  
  
_jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader([_base]),
    trim_blocks=True,autoescape=True)


def render(template_name, values={}):
    template = _jinja_environment.get_template(template_name)
    return template.render(values)

_jinja_environment.filters["brphone"]=filters.brphone
_jinja_environment.filters["cpf"]=filters.cpf
_jinja_environment.filters["brcurrency"]=filters.brcurrency
_jinja_environment.filters["brdate"]=filters.brdate
_jinja_environment.filters["cep"]=filters.cep
_jinja_environment.filters["brfloat"]=filters.brfloat
_jinja_environment.filters["brdate_no_locale"]=filters.brdate_no_locale