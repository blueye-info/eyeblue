from setuptools import setup, find_packages

setup(
    name="eyeblue",
    packages=find_packages(),
    version='1.0',
    description="A utility for digital cash",
    author="banjuanshua",
    author_email='593474341@qq.com',
    url="https://github.com/blueye-info/eyeblue",
    keywords='Digital Cash Data',
    install_requires=[
        'pandas'
        'numpy',
        'urllib',
		'ws4py'
    ]
)