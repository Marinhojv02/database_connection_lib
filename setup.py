from setuptools import setup, find_packages

setup(
    name='database_connection_lib',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        "sqlalchemy",
        "psycopg2-binary"
    ],
    scripts=[
        # Scripts adicionais, se houver
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        # Outras classificações
    ],
)
