from setuptools import setup

packages = [
    'rendermarkdown'
]

requirements = [
    'click',
    'requests'
]

setup(
    author='Matt Chung',
    author_email='mchung@whalerockindustries.com',
    description=('A simple CLI to preview markdown files (i.e "README.md") '
                 'files using GitHubs API'),
    entry_points='''
    [console_scripts]
    rendermarkdown=rendermarkdown.cli:cli
    ''',
    install_requires=requirements,
    name='rendermarkdown',
    packages=packages,
    url='https://github.com/whalerock/rendermarkdown',
    version='0.0.2'
)
