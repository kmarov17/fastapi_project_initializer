import os
import subprocess
import git
import venv
import platform

class FastAPIProjectInitializer:
    def __init__(self, repo_url, project_dir):
        self.repo_url = repo_url
        self.project_dir = project_dir

    def clone_repo(self):
        if not os.path.exists(self.project_dir):
            os.makedirs(self.project_dir)
        git.Repo.clone_from(self.repo_url, self.project_dir)
        print(f"Cloned repository from {self.repo_url} to {self.project_dir}")

    def create_virtualenv(self):
        env_dir = os.path.join(self.project_dir, 'venv')
        venv.create(env_dir, with_pip=True)
        print(f"Created virtual environment in {env_dir}")
        return env_dir

    def activate_virtualenv(self, env_dir):
        # Detect the operating system
        os_name = platform.system()
        if os_name == 'Windows':
            activate_script = os.path.join(env_dir, 'Scripts', 'activate')
            command = f'{activate_script} && echo "Virtual environment activated"'
        else:
            activate_script = os.path.join(env_dir, 'bin', 'activate')
            command = f'source {activate_script} && echo "Virtual environment activated"'

        # Execute the activation command
        subprocess.call(command, shell=True)
        print(f"Activated virtual environment in {env_dir}")

    def install_dependencies(self, env_dir):
        requirements_path = os.path.join(self.project_dir, 'requirements.txt')
        if os.path.exists(requirements_path):
            pip_path = os.path.join(env_dir, 'bin', 'pip')
            subprocess.check_call([pip_path, 'install', '-r', requirements_path])
            print(f"Installed dependencies from {requirements_path}")
        else:
            print(f"No requirements.txt found in {self.project_dir}")

    def initialize(self):
        self.clone_repo()
        env_dir = self.create_virtualenv()
        self.activate_virtualenv(env_dir)
        self.install_dependencies(env_dir)

