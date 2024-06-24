from setuptools import setup, find_packages

setup(
    name='fastapi_project_initializer',
    version='0.1.5',
    packages=find_packages(),
    install_requires=[
        'gitpython',
    ],
    entry_points={
        'console_scripts': [
            'fastapi-init=fastapi_project_initializer.main:main',
        ],
    },
    author='Kodana Diarra aka(kmarov)',
    author_email='kodanadiarra@gmail.com',
    description='A library to initialize a FastAPI project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/kmarov17/fastapi_project_initializer.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
