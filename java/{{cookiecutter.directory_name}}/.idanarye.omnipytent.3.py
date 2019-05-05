from omnipytent import *
from omnipytent.ext.idan import *


gradle = local['gradle']['-q']


@task
def compile(ctx):
    gradle['build'] & ERUN.bang


@task
def run(ctx):
    gradle['run'] & BANG


@task
def test(ctx):
    gradle['test'] & BANG


@task
def debug(ctx):
    classpath = list(get_gradle_deps())
    classpath.append(local.path('./build/classes/java/main/'))
    classpath = ':'.join(map(str, classpath))
    FN['vebugger#jdb#start']('App', {'classpath': classpath, 'srcpath': 'src/main/java', 'args': []})
