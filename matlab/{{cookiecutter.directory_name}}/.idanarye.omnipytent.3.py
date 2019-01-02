from omnipytent import *
from omnipytent.ext.idan import *


@task
def file_to_run(ctx):
    ctx.pass_data('main')


@task.window
def terminal(ctx):
    shell = local['octave'] & TERMINAL_PANEL
    ctx.pass_data(shell)


@task(terminal, file_to_run)
def run(ctx):
    ctx.dep.terminal << ctx.dep.file_to_run


@task(file_to_run)
def go(ctx):
    local['octave'][ctx.dep.file_to_run + '.m'] & BANG


@task
def prepare_for_lyx(ctx):
    code = VAR['@0']

    def gen_result():
        first = True
        for line in code.splitlines():
            if first:
                first = False
            else:
                yield ''
            yield line.replace('\t', '    ')

    VAR['@+'] = '\n'.join(gen_result())


def image_locations():
    BASE = 'http://u.cs.biu.ac.il/~kapaho/IP/Images/'
    import requests, re
    pattern = re.compile(r'<a href="(.*?)">(.*?)</a>')
    for m in pattern.finditer(requests.get(BASE).text):
        path, name = m.groups()
        yield dict(
            url=BASE + path,
            name=name)

@task
def download_images(ctx):
    chosen = yield CHOOSE(image_locations(), fmt=lambda e: e['name'], multi=True)
    terminal = local['bash'] & TERMINAL_PANEL
    for image in chosen:
        local['wget'][image['url']] & terminal
    terminal << 'exit'
