import os
import setuptools

r=lambda x:open(os.path.join(os.path.abspath(os.path.dirname(__file__)),x),'rb').read().decode('utf-8')

setuptools.setup(
    name='userelaina',
    version='0.0.3',
    description='Syntax sugar.',
    long_description=r('README.rst'),
    py_modules=['userelaina'],
    packages=setuptools.find_packages(),
    install_requires=r('requirements.txt').split('\n'),

    author='userElaina',
    author_email='userElaina@google.com',
    url='https://github.com/userElaina',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python :: 3',
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    project_urls={
        "Source": "https://github.com/userelaina/sugar",
    },
    keywords='userelaina',
    python_requires='>=3.6',
)