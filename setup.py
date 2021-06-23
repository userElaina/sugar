import os
import setuptools

setuptools.setup(
    name='userelaina',
    version='0.0.1',
    description='Syntax sugar.',
    long_description=open(os.path.join(os.path.abspath(os.path.dirname(__file__)),'README.rst')).read(),
    py_modules=['userelaina'],
	packages=setuptools.find_packages(),
    install_requires=[
		'setuptools',
		'wheel',
		'twine',
		'requests',
		'pillow',
		'opencv-python',
		'matplotlib',
		'psutil',
		'aiohttp',
		'python-socketio',
		'websocket-client',
		'python-telegram-bot',
		'myqr',
		'qrcode',
		'pyzbar',
		'fastgui',
		'downs',
		'colorsname',
	],

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