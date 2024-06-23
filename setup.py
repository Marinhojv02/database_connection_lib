from setuptools import setup, find_packages

setup(
    name='database_connection_lib',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        "sqlalchemy",
        "psycopg2-binary"
    ],
)

# from setuptools import setup, find_packages

# setup(
#     name='sua_lib',
#     version='0.1',
#     packages=find_packages(),
#     install_requires=[
#         # Lista de dependências
#     ],
#     scripts=[
#         # Scripts adicionais, se houver
#     ],
#     classifiers=[
#         'Programming Language :: Python :: 3',
#         # Outras classificações
#     ],
# )
