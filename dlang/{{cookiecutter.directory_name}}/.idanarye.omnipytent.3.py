from omnipytent import *
from omnipytent.ext.idan import *
from omnipytent.completers import file_completer

exe = local['./app']
dub = local['dub']['-q']


@task
def compile(ctx):
    dub['build']['--compiler=dmd'] & ERUN.bang


@task
def run(ctx):
    dub['run'] & BANG


@task
def test(ctx):
    dub['test']['--compiler=dmd'] & BANG


@task
def debug(ctx):
    CMD.VBGstartGDBForD(exe)


def mkpath(path):
    if not path.exists():
        mkpath(path.dirname)
        path.mkdir()


@task.complete(file_completer('/files/code/wekapp/weka'))
def copy_from_wekapp(ctx, *paths):
    print(paths)
    for path in paths:
        source_file = local.path('/files/code/wekapp/weka') / path
        target_file = local.path('source/weka') / path
        if not target_file.exists():
            mkpath(target_file.dirname)
            local['ln']('-s', source_file, target_file)


@task
def copy_fake_weka(ctx):
    target_root = local.path('source/weka')
    assert not target_root.islink(), "%s is symlink" % target_root
    mkpath(target_root)
    for faked_weka_module in local.path('../0zfake_libs'):
        target = target_root / faked_weka_module.basename
        if target.exists():
            print('%s exists. %ssymlink' % (target, '' if target.islink() else 'not '))
        else:
            local['ln']('-s', faked_weka_module, target)

