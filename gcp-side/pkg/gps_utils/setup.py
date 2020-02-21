import setuptools

setuptools.setup(
    name="gps-utils",
    version="0.0.1",
    author="Robert Howie",
    author_email="robertzhowie@gmail.com",
    description="utils for the app to use",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)