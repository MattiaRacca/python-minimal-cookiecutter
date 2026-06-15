import subprocess
import sys

OWNER = "{{ cookiecutter.github_repo_owner }}"
REPO = "{{ cookiecutter.repo_name }}"
PROJECT_NAME = "{{ cookiecutter.project_name }}"
CONDA_ENV = "{{ cookiecutter.conda_env_name }}"
PYTHON_VERSION = "{{ cookiecutter.python_version }}"


def run(cmd):
    print(f"$ {' '.join(cmd)}")
    subprocess.run(cmd, check=True)


def prepare_git():
    answer = input(f"Initialize git repo and commit '{REPO}'? [y/N] ").strip().lower()
    if answer not in ("y", "yes"):
        print("Skipped git initialization.")
        return
    run(["git", "init"])
    run(["git", "branch", "-M", "main"])
    run(["git", "add", "README.md"])
    run(["git", "add", ".gitignore"])
    run(["git", "commit", "-m", "First commit"])
    run(["git", "remote", "add", "origin", f"git@github.com:{OWNER}/{REPO}"])


def prepare_conda():
    answer = (
        input(f"Create conda env '{CONDA_ENV}' (python={PYTHON_VERSION})? [y/N] ")
        .strip()
        .lower()
    )
    if answer in ("y", "yes"):
        run(
            [
                "conda",
                "create",
                "--name",
                CONDA_ENV,
                "--yes",
                f"python={PYTHON_VERSION}",
            ]
        )
        run(["conda", "env", "list"])
    else:
        print("Skipped conda env creation.")


def main():
    prepare_git()
    prepare_conda()
    print(
        f"""
Your new project {PROJECT_NAME} has been created and committed locally.

Next steps:
  1. Create an empty repo '{REPO}' at https://github.com/new
  2. Push it:
       git push -u origin main
"""
    )


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as exc:
        print(f"A setup command failed: {exc}", file=sys.stderr)
        sys.exit(1)
