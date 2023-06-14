from setuptools import setup, find_packages

setup(
    name = 'CustomCLI',
    version = '0.0.1',
    packages = find_packages(),
    install_requires = [
        'click', 'regex'
    ],
    entry_points = '''
    [console_scripts]
    CLI = CLI:CLI
    '''
)