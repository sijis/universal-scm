"""Package installer."""
from setuptools import find_packages, setup

with open('requirements.txt', 'rt') as requirements:
    REQUIREMENTS = requirements.readlines()

with open('README.rst', 'rt') as readme:
    README = readme.read()

setup(
    name='universalscm',
    description='SCM Api',
    long_description=README,
    author='Sijis Aviles',
    author_email='sijis.aviles@gmail.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    setup_requires=['setuptools_scm'],
    use_scm_version=True,
    install_requires=REQUIREMENTS,
    keywords='git gitlab github',
    url='https://github.com/gogoair/universal_scm',
    download_url='https://github.com/gogoair/universal_scm',
    platforms=['OS Independent'],
    license='Apache 2',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
)
