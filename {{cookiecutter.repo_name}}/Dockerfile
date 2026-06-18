FROM python:{{cookiecutter.python_version}}-alpine
WORKDIR /{{cookiecutter.project_name}}
COPY pyproject.toml README.md LICENSE ./
RUN mkdir -p {{cookiecutter.package_name}} && touch {{cookiecutter.package_name}}/__init__.py \
    && pip install --no-cache-dir . \
    && rm -rf {{cookiecutter.package_name}}
COPY {{cookiecutter.package_name}}/ {{cookiecutter.package_name}}/
RUN pip install --no-cache-dir --no-deps .
CMD ["entrypoint"]
