from setuptools import find_packages,setup
from typing import List

Hypen = "-e ."

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("/n","") for req in requirements]




setup(
    name='MLPROJECT',
    version = '0.0.1',
    author='Sandarbh',
    author_email = 'sandarbhparoha1203@gmail.com',
    packages=find_packages(), # whchever folder will consist of file name '__init__.py' will automatically get selected
    install_requires=get_requirements('requirements.txt')


)