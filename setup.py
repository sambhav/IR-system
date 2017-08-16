from setuptools import setup, find_packages

setup(
    name='irs',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'Flask',
        'Whoosh',
        'praw'
    ],
    entry_points='''
        [console_scripts]
        irs=irs:cli
    ''',
)
