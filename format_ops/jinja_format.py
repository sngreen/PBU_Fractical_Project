import os
import sys
import jinja2

def render_template(template, **data) -> str:
    if not os.path.exists(template):
        print('Did not find template file: %s' % template)
        sys.exit(1)

    templateLoader: jinja2.loaders.FileSystemLoader = jinja2.FileSystemLoader(searchpath='/')
    templateEnv: jinja2.environment.Environment = jinja2.Environment(loader=templateLoader)
    templ: jinja2.environment.Template = templateEnv.get_template(template)

    return templ.render(data)
