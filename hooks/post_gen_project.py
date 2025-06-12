#!/usr/bin/env python
import pathlib


if __name__ == '__main__':

    cli_path = pathlib.Path(
        'src',
        '{{ cookiecutter.project_namespace }}',
        '{{ cookiecutter.project_package }}',
        'cli.py'
    )
    if '{{ cookiecutter.create_author_file }}' != 'y':
        pathlib.Path('AUTHORS.md').unlink()

    jmullan_path = pathlib.Path(
        'src',
        '{{ cookiecutter.project_namespace }}',
        '{{ cookiecutter.project_package }}',
        '_jmullan_cli.py'
    )
    if 'jmullan.cmd' == '{{ cookiecutter.command_line_interface|lower }}':
        jmullan_path.rename(cli_path)
    else:
        jmullan_path.unlink()

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        pathlib.Path('LICENSE').unlink()
