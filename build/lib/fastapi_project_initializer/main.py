import argparse
import os
from fastapi_initializer.fastapi_initializer import FastAPIProjectInitializer

DEFAULT_REPO_URL = 'https://github.com/kmarov17/fastapi_default_structure.git'

def main():
    parser = argparse.ArgumentParser(description='Initialize a FastAPI project.')
    parser.add_argument('project_name', type=str, help='Name of the project to be created')

    args = parser.parse_args()

    project_dir = os.path.join(os.getcwd(), args.project_name)
    initializer = FastAPIProjectInitializer(DEFAULT_REPO_URL, project_dir)
    initializer.initialize()

if __name__ == '__main__':
    main()
