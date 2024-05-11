from setuptools import setup, find_packages
from typing import List


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

HYPEN_E_DOT = '-e .'
def get_requirements(file_name:str) -> List[str]:
    with open(file_name, 'r') as file:
        requirements = [requirement.replace('\n', '') for requirement in file.readlines()]
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    return requirements


__version__ = "0.0.0"
SRC_REPO = "text_summarizer"
AUTHOR_USER_NAME = "DarshanRokkad"
AUTHOR_EMAIL = "darshanrokkad2003@gmail.com"
REPO_NAME = "Text_Summarizer"

setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires = get_requirements('requirements.txt')
)