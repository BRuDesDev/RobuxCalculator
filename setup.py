from setuptools import setup

setup(
    name='robux_calculator',
    version='1.0',
    packages=['robux_calculator'],
    entry_points={
        'console_scripts': [
            'robux_calculator = robux_calculator.__main__:main',
        ],
    },
)