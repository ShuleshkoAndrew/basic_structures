from setuptools import setup, find_packages

setup(
    name="basic-structures",
    version="0.0.2",
    description="Module with queue-like doubly linked list and binary search tree",
    long_description=open("README.md").read(),
    long_description_content_type="markdown",
    url="https://github.com/ShuleshkoAndrew/basic_structures",
    author="Andrew Shuleshko",
    author_email="shuleshko.av@phystech.edu",
    packages=find_packages(),
    py_modules=["doubly_linked_list", "binary_search_tree"],
    classifiers=["Programming Language :: Python :: 3.10", "Development Status :: 3 - Alpha"],
)
