import argparse
import os
from fastapi_initializer.fastapi_initializer import FastAPIProjectInitializer

DEFAULT_REPO_URL = 'https://github.com/kmarov17/fastapi_default_structure.git'

def main():
    parser = argparse.ArgumentParser(description='Initialize a FastAPI project.')
    parser.add_argument('project_name', type=str, help='Name of the project to be created')
    parser.add_argument('--repo_url', type=str, nargs='?', default=DEFAULT_REPO_URL, help='URL of the GitHub repository to clone')
    parser.add_argument('--proxy_url', type=str, nargs='?', help='URL of the proxy server if needed')

    args = parser.parse_args()

    project_dir = os.path.join(os.getcwd(), args.project_name)
    repo_url = args.repo_url or DEFAULT_REPO_URL
    proxy_url = args.proxy_url
    initializer = FastAPIProjectInitializer(repo_url, project_dir, proxy_url)
    initializer.initialize()

if __name__ == '__main__':
    main()
