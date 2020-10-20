import setuptools

with open('README.md') as rm:
    long_description = rm.read()

setuptools.setup(
    name='Knox-FileWatcher',
    version='0.0.1',
    author='Knox-18',
    author_email='sample@student.aau.dk',
    description='File watcher for knox repo',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://git.its.aau.dk/Knox/KnoxKL-FileWatcher.git',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='==3.8'
)