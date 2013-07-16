from distutils.core import setup
VERSION='1.0'

long_description = open('README.md').read()

setup(
    name='gdiff',
    version=VERSION,
    packages=['gdiff', 
              ],
    description='google diff match library.',
    long_description=long_description,
    author='neil fraser @ google',
    author_email='neil.fraser@gmail.com',
    license='Apache License v2.0',
    url='https://github.com/fengli/google-diff-match-python',
    platforms=["any"],
    classifiers=[
        'Development Status :: 1 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
