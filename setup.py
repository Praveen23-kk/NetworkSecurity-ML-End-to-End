from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list requirements
    """
    requirement_list:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            # read lines from the file
            
            lines=file.readlines()
            
            ## Process each line
            for line in lines:
                requirement=line.strip()
                ##ignore empty lines -e.
                if requirement and requirement !='-e.':
                    requirement_list.append(requirement)
                    
    except FileNotFoundError:
        print("requiremnts.txt file not found")
        
    
    return requirement_list

print(get_requirements())


setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="K Praveen Kumar",
    author_email="Praveennaaz23@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
    
        
                        
                
