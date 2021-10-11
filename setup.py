from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="nimiqclient",
    version="0.1.2",
    description="A python client for the Nimiq JSON-RPC API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nimiq-community/python-client",
    author="The Nimiq Foundation",
    author_email="info@nimiq.com",
    license="Apache 2.0",
    packages=['nimiqclient', 'nimiqclient.models'],
    zip_safe=True,
    install_requires=["requests", "enum34"],
    python_requires=">=2.4",
    test_suite="test",
)
