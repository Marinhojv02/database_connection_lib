from setuptools import setup, find_packages

setup(
    name='database_connection_lib',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        "sqlalchemy",
        "psycopg2-binary",
        "pika"
    ],
    scripts=[
        # Scripts adicionais, se houver
    ],
    description="A private library to connect to PostgreSQL using SQLAlchemy",
    classifiers=[
        'Programming Language :: Python :: 3',
        # Outras classificações
    ],
)
