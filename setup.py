from setuptools import find_packages, setup

setup(
    name="qbpy",
    version="1.0.0",
    packages=find_packages(include=["qbpy", "qbpy.*"]),
)
