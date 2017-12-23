from setuptools import setup

setup(
    name='greenwavereality',
    version='0.2.5',
    packages=['greenwavereality'],
    install_requires=[
          'requests',
          'xmltodict',
      ],
    url='https://github.com/dfiel/greenwavereality',
    license='MIT',
    author='David Fiel',
    author_email='github@dfiel.com',
    description='Control of Greenwave Reality Lights'
)
