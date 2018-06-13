from setuptools import setup, find_packages

setup(
    name="eyeblue",
    packages=find_packages(),
    version='0.1',
    description="A utility for digital cash",
    author="banjuanshua",
    author_email='593474341@qq.com',
    url="https://github.com/banjuanshua/lanmuda",
    keywords='Digital Cash Data',
    install_requires=[
        'pandas'
        'numpy',
        'urllib',
    ]
)