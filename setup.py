from setuptools import setup, find_packages


setup(
    name="jobhunter",
    version="0.0.1",
    author="JJ Espinoza",
    description="Automated job discovery using machine learning",
    packages=find_packages(),
    install_requires=[
        "boto3",
        "black",
        "brotlipy",
        "bs4",
        "certifi",
        "nltk",
        "numpy",
        "pyyaml",
        "pandas",
        "pylint",
        "pytest-cov",
        "pytest-cov",
        "requests-oauthlib",
        "scipy",
        "scikit-learn",
    ],
    entry_points={
        "console_scripts": [
            "jobhunter = jobhunter.utils.search_linkedin_jobs:entrypoint",
        ]
    },
)
