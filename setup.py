import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="workast",
    version="0.1.0",
    author="Omer Enbar",
    author_email="opensource@sensibo.com",
    description="API class wrapper for controlling workast.io task manager",
    python_requires=">=3.6.0",
    long_description=long_description,
    url="https://github.com/Sensibo/workast",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Environment :: Console',
        'Intended Audience :: Developers',
    ],
    keywords='Workast, todo',
    py_modules=['workast'],
    include_package_data=True,
    install_requires=['requests'],
    entry_points={
        'console_scripts': [
            'Workast = workast.workast:Workast',
        ],
    },
)
