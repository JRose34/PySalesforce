from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pysalesforce',
    version='1.0',
    author='Glen Barger',
    author_email='gbarger@gmail.com',
    description='Python module to wrap the Salesforce APIs',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/gbarger/PySalesforce',
    py_modules=[
        'pysalesforce',
        'webservice'],
    install_requires=[
        'boto3',
        'pymysql',
        'requests'
    ])