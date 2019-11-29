from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

with open('LICENSE') as f:
    license_ = f.read()

setup(
    name='skyrim_chopping_wood',
    version='1.0',
    description='Script for chopping wood in Skyrim.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/SalavatD/skyrim_chopping_wood',
    author='Salavat Dautov',
    author_email='49768177+SalavatD@users.noreply.github.com',
    license=license_,
    entry_points={
        'console_scripts': [
            'skyrim_chopping_wood=skyrim_chopping_wood.main:main'
        ]
    }
)
