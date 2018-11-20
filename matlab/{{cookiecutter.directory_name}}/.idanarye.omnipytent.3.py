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
            yield line.replace('\\t', '    ')

    VAR['@+'] = '\\n'.join(gen_result())
