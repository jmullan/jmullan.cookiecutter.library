import re
import sys

# See https://packaging.python.org/en/latest/specifications/name-normalization/#name-format
MODULE_REGEX = r'^([A-Z0-9]|[A-Z0-9][A-Z0-9._-]*[A-Z0-9])$'

module_name = '{{ cookiecutter.project_slug}}'

if not re.match(MODULE_REGEX, module_name, re.IGNORECASE):
    print(f'ERROR: The project slug {module_name} is not a valid Python module name. '
          'See https://packaging.python.org/en/latest/specifications/name-normalization/#name-format')
    # Exit to cancel project
    sys.exit(1)
