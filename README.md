# FastAPI Project Initializer

The `fastapi_project_initializer` library provides an easy way to initialize a FastAPI project by cloning a GitHub repository, creating a virtual environment, and installing dependencies. This library simplifies the setup process, allowing you to quickly get started with a standardized FastAPI project structure.

```
By
    ***   ***   ******   ******   ***********   ***********   **********   ***  ***
    ***  **     ******   ******   ***********   ***     ***   **********   ***  ***
    ******      *** *** *** ***   ***     ***   ***     ***   ***    ***   ***  ***
    ******      ***   ***   ***   ***********   *********     ***    ***   ***  ***
    ***  **     ***    *    ***   ***     ***   ***     **    **********    **  **
    ***   ***   ***         ***   ***     ***   ***     ***   **********     ****
```

## Features

- Clone a specified GitHub repository
- Create a virtual environment
- Install dependencies from `requirements.txt`
- Easy-to-use command-line interface (CLI)

## Installation

To install the `fastapi_project_initializer` library, run:

```bash
pip install fastapi_project_initializer
```

## Usage

To initialize a new FastAPI project, use the `fastapi-init` command followed by the name of your project:

```bash
fastapi-init project_name
```

This command will:

- Clone the default FastAPI project repository.
- Create a virtual environment.
- Install the dependencies listed in `requirements.txt`.

### Example

```bash
fastapi-init my_fastapi_project
```

This will create a new FastAPI project in the `my_fastapi_project` directory.

## Project Structure

The initialized project will have the following structure:

```
my_fastapi_project/
│
├── app/
│   ├── configs/           # Application configuration files
│   ├── models/            # Data model files
│   ├── routes/            # Routing (routes) files
│   ├── services/          # Application service files
│   ├── utils/             # Utilities and tools
|   └── tests/             # Unit test files for the application
├── main.py                # Main application entry point
├── requirements.txt       # File listing the Python dependencies
├── .gitignore             # File to ignore specific files/folders in git
├── Dockerfile             # File to build fastapi docker image
└── README.md              # Project documentation
```

## Development

To contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

## Setting Up for Development

Clone the repository:

```bash
git clone https://github.com/kmarov17/fastapi_project_initializer.git
cd fastapi_project_initializer
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

- On Windows:

```bash
venv\Scripts\activate
```

- On macOS/Linux:

```bash
source venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## License

This project is licensed under the MIT License. See the LICENSE file for more information.
