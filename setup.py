import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="way3",
    version="0.0.19",
    author="aboutmydreams",
    author_email="aboutmydreams@163.com",
    description="Simplified file path management for Python developers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aboutmydreams/way3",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
