conda create --name {{cookiecutter.conda_env_name}} python={{cookiecutter.python_version}}
conda activate {{cookiecutter.conda_env_name}}
conda env export > environment.yml
conda deactivate
conda env list
