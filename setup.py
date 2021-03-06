import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-GoFindMe", # Replace with your own username
    version="0.0.1",
    packages=['GoFindMe'],
    package_data={'':['web_accounts_list.json']},
    include_package_data=True,
    author="Bryan Galbraith, Micah Hoffman",
    author_email="qpoint@shaw.ca",
    description="A small app to locate usernames on various social media sites",
    url="https://github.com/qpointconsulting/Go-Find-Me",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
    ],
    python_requires='>=3.6',
)
