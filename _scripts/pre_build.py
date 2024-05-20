# -*- coding: utf-8 -*-
'''.'''

import pathlib
import subprocess

BASE_DIR = pathlib.Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent
SRC_DIR = ROOT_DIR.joinpath('src')
PROJ_DIR = SRC_DIR.joinpath('app_pyside_qml')
RESOURCES_DIR = SRC_DIR.joinpath('resources')
LOCALES_DIR = RESOURCES_DIR.joinpath('locales')

UI_DIR = RESOURCES_DIR.joinpath('ui')

RESOURCES = RESOURCES_DIR.joinpath('resources.qrc')
RESOURCES_RC = PROJ_DIR.joinpath('resources_rc.py')

APP_NAME = 'br.com.justcode.Qt'
SOURCE_LANGUAGE = 'pt_BR'
TARGET_LANGUAGES = ['en_US']


def format_qml_files() -> None:
    print('[!] Formatando arquivos QML [!]')
    print('Arquivos formatados:')
    for file in UI_DIR.rglob('*.qml'):
        if file.is_file() and file.suffix == '.qml':
            print(f'- {file.name}.')
            print(file)
            subprocess.run(args=['pyside6-qmlformat', '-i', '-n', file])
    print('[!] Concluído [!]')


def create_or_update_translations() -> None:
    print('[!] Gerando ou atualizando as traduções (*.ts) [!]')
    for lang in TARGET_LANGUAGES:
        output = LOCALES_DIR.joinpath(lang, f'{APP_NAME}.{lang}.ts')
        output.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            args=['pyside6-lupdate', '-no-obsolete', '-extensions', 'qml,py',
                  '-source-language', SOURCE_LANGUAGE, '-target-language', lang,
                  ROOT_DIR, '-ts', output]
        )
    print('[!] Concluído [!]')


def compile_translations() -> None:
    print('[!] Compilando as traduções (*.qm) [!]')
    for file in LOCALES_DIR.rglob('*.ts'):
        if file.is_file() and file.suffix == '.ts':
            output = file.parent.joinpath(f'{file.stem}.qm')
            subprocess.run(args=['pyside6-lrelease', file, output])
    print('[!] Concluído [!]')


def compile_resources() -> None:
    print('[!] Gerando resources_rc.py, aguarde... [!]')
    subprocess.run(args=['pyside6-rcc', RESOURCES, '-o', RESOURCES_RC])
    print('[!] Concluído [!]')


if __name__ == '__main__':
    format_qml_files()
    create_or_update_translations()
    compile_translations()
    compile_resources()
