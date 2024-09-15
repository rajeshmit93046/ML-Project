from setuptools import find_packages, setup
from typing import List

HYPEN_DOT_E = "-e ."

def get_req(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()  # Make sure to call readlines()
        requirements = [req.strip() for req in requirements]  # Use strip() to remove both \n and leading/trailing whitespace
        if HYPEN_DOT_E in requirements:
            requirements.remove(HYPEN_DOT_E)
    return requirements

setup(
    name="MLProject",
    version="0.0.1",
    author="rajesh",
    author_email="rajeshkumar1998.shiv@gmail.com",
    packages=find_packages(),
    install_requires=get_req("requirements.txt"),
    # Optional fields
    description="A machine learning project",
    long_description=open('README.md').read(),  # Ensure you have a README.md file for this
    long_description_content_type='text/markdown',  # Or 'text/x-rst' if using reStructuredText
    url="https://github.com/rajeshmit93046/ML-Project",  # Update with your actual repository URL
)
