import os
import os.path

from setuptools import find_packages
from setuptools import setup


def find_requires():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    requirements = []
    with open('{0}/requirements.txt'.format(dir_path), 'r') as reqs:
        requirements = reqs.readlines()
    return requirements


if __name__ == "__main__":
    setup(
        name="moscow_python",
        version="0.0.1",
        description='my cool package',
        packages=find_packages(), #встроенная функция. кот определяет где искать пакеты
        install_requires=find_requires(), #передаем список зависимостей
        include_package_data=True, #чтобы включить непитон-файлы
        entry_points={ #описывает какие в итоге будут созданы команды в командной строке
            'console_scripts': [
                'my_command = moscow_python.cli:main',
            ],
        },
    )
