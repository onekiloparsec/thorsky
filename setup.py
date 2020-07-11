"""
Python based skycalc GUI
"""

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="thorsky",
    version='1.0.1',
    author="John Thorstensen",
    author_email="John.Thorstensen@dartmouth.edu",
    description="Python based skycalc GUI",  # is it accurate enough?
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://www.dartmouth.edu",  # project homepage?
    license='BSD 2-Clause License',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    python_requires='>=3.5, <4',
    install_requires=[
        'astropy>=3',
        'pytz',
        'dateutil'
    ],
    package_data={  # Optional
        'thorsky': [
            'cartesian_bright.dat',
            'observatories_rev.dat'
        ],
    },
    # entry_points={  # Optional
    #     'console_scripts': [
    #         'thorsky=thorsky:main',
    #     ],
    # },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Astronomers',
        'License :: OSI Approved :: BSD 2-Clause License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
