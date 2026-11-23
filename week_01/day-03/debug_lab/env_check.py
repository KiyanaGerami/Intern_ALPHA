import sys
from env_tools import in_virtualenv, check_version, describe_interpreter

version = f"{sys.version_info.major}.{sys.version_info.minor}"
print("venv active:", in_virtualenv(sys.prefix, sys.base_prefix))
print(check_version(version))
print(describe_interpreter(version, sys.executable))
