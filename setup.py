from setuptools import setup, find_packages

setup(
    name="django-markdown-model",
    version="1.0",
    description="This package allows you to store and render Markdown content effortlessly, making it ideal for applications that require rich text input from users.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Mohit Prajapat",
    author_email="mohitdevelopment2001@gmail.com",
    url="https://github.com/mohitprajapat2001/django-markdown-model",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "django>=5.1",
    ],
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
