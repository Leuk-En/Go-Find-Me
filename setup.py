import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="GoFindMe", # Replace with your own username
    version="0.0.1",
    author="Bryan Galbraith, Mikah Hoffman",
    author_email="qpoint@shaw.ca",
    description="A small app to locate usernames on various social media sites",
    url="https://github.com/qpointconsulting/Go-Find-Me",
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
    ],
    python_requires='>=3.6',
)