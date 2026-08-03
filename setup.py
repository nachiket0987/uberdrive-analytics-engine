from setuptools import setup, find_packages

setup(
    name="uberdrive-analytics-engine",
    version="1.0.0",
    author="Nachiket Gadilohar",
    author_email="nachiketlohar0306@gmail.com",
    description="An end-to-end analytics and intelligence engine for Uber ride data",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/nachiket0987/uberdrive-analytics-engine",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pandas>=2.0.0",
        "numpy>=1.24.0",
        "matplotlib>=3.7.0",
        "seaborn>=0.12.0",
        "streamlit>=1.25.0",
    ],
)
