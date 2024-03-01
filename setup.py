import os
from pathlib import Path

from setuptools import setup

MODULE_NAME = 'pycparser-stubs'
PROJECT_ROOT = Path(__file__).parent


def find_stubs():
    src_dir = (PROJECT_ROOT / MODULE_NAME).absolute()
    stubs: list[str] = []
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            path = (Path(root) / file).absolute().relative_to(src_dir)
            if path.suffix == '.pyi' or path.name == 'py.typed':
                stubs.append(str(path))
    return {MODULE_NAME: stubs}


setup(
    name=MODULE_NAME,
    version='0.0.1',
    description='PEP 561 type stubs for pycparser',
    long_description=(PROJECT_ROOT / 'README.md').read_text(encoding='utf-8'),
    long_description_content_type='text/markdown',
    classifiers=['License :: OSI Approved :: MIT License'],
    license='MIT License',
    url='https://github.com/TsXor/pycparser-stubs',
    author='TsXor',
    packages=[MODULE_NAME],
    install_requires=['pycparser>=2.21'],
    python_requires=">=3.5",
    package_data=find_stubs(),
    zip_safe=False,
)