from setuptools import find_packages,setup
from typing import List

dote='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this will return list
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if dote in requirements:
            requirements.remove(dote)
        
    return requirements

setup(
    name='ML',
    version='0.0.1',
    author='priya',
    author_email='kmpriya374@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)