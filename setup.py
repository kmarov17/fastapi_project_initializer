from setuptools import setup, find_packages

setup(
    name='fastapi_project_initializer',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'gitpython',
    ],
    entry_points={
        'console_scripts': [
            'fastapi-init=fastapi_project_initializer.main:main',
        ],
    },
)
