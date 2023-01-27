import subprocess
import re

p = subprocess.check_output("poetry version", shell=True)
ver = re.match(".* to (.*)\\.*$", p.decode())[1]
open("formation/__version__.py", "w").write(f'__version__ = "{ver}"')
print(f"git tag v{ver}")
print(subprocess.check_call(f"git tag v{ver}", shell=True))
print("now run poetry publish --build, git push --tags")

