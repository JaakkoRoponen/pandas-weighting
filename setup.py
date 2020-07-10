import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='pandas-weighting',
    version='0.0.2',
    author='Jaakko Roponen',
    description='General level weighting of Pandas Dataframes',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/JaakkoRoponen/pandas-weighting',
    packages=setuptools.find_packages(),
    install_requires=['pandas'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
