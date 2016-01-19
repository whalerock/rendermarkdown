from setuptools import setup

packages = [
    'rendermarkdown'
]

requirements = [
    'click',
    'requests'
]

test_requirements = [
    'tox'
]

setup(
    author='Matt Chung',
    author_email='mchung@whalerockindustries.com',
    entry_points='''
    [console_scripts]
    rendermarkdown=rendermarkdown.cli:cli
    ''',
    install_requires=requirements,
    name='rendermarkdown',
    packages=packages,
    tests_require=test_requirements,
    test_suite="tox",
    version='0.0.1'
)
