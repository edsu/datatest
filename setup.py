from setuptools import setup, find_packages

setup(
    name="datatest",
    version='0.0.1',
    author="Ed Summers",
    author_email="ehs@pobox.com",
    packages=['datatest'],
    description="Example of bundling data with a python package",
    install_requires=['pandas'],
    package_data={"datatest": ["buildings.csv"]},
)
