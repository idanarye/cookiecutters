from omnipytent import *
from omnipytent.ext.idan import *


gradle = local['gradle']['-q']


def get_class_path():
    return gradle['printClasspath']().strip() + ':build/classes/main'


@task
def compile(ctx):
    gradle['build'] & ERUN.bang


@task
def run(ctx):
    gradle['run'] & BANG


@task
def test(ctx):
    gradle['test'] & BANG


# @task
# def debug(ctx):
    # FN['vebugger#jdb#start']('App', {'classpath': get_class_path(), 'srcpath': 'src/main/java', 'args': []})
