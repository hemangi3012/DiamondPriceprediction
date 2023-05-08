from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        return requirements

setup(
    name='Diamond_Price_prediction',
    version='0.0.1',
    author='hemangi',
    author_email='vagahsiya295@gmail.com',
    install_requies=get_requirements('requirement.txt'),
    packages=find_packages()
)