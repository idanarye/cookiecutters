#!/usr/bin/python3

import re
import os

from plumbum import local
from cookiecutter.main import cookiecutter

num_pattern = re.compile(r'^\d+$')

here = local.path('.')

def max_number():
    for path in here:
        try:
            num = int(path.basename)
        except ValueError:
            pass
        else:
            yield num
max_number = max(max_number(), default=0)

new_number = max_number + 1

template_name = here.basename
templates_repo = local.path(os.readlink(__file__)).parent

cookiecutter(str(templates_repo / template_name),
             no_input=True,
             extra_context=dict(
                 directory_name=str(new_number),
             ))
print(new_number)
