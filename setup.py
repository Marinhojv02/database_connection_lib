from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='LibTestePython',
    url='https://github.com/Marinhojv02/teste-python-lib',
    author='Joao Victor Marinho',
    author_email='joaovm048@gmail.com',
    # Needed to actually package something
    packages=['lib_teste'],
    # Needed for dependencies
    install_requires=[],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='None',
    description='An example of a python package from pre-existing code',
    # We will also need a readme eventually (there will be a warning)
    long_description=open('README.md').read(),
)
