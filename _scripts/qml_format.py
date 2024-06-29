# -*- coding: utf-8 -*-
"""."""

import pathlib
import subprocess

BASE_DIR = pathlib.Path(__file__).resolve().parent

INPUT = BASE_DIR.parent / 'resources' / 'ui'


def main() -> None:
    print('[!] Formatting *qml files, please wait... [!]')
    print('Formatted Files:')
    for file in INPUT.rglob('*.qml'):
        if file.is_file() and file.suffix == '.qml':
            print(f'- {file.name}.')
            print(file)
            subprocess.run(
                args=['pyside6-qmlformat', '-i', '-n', file],
                check=False,
            )
    print('[!] Done [!]')


if __name__ == '__main__':
    main()
