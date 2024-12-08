import pathlib
import os
import sys

THIS_FILE_PATH = pathlib.Path(__file__).resolve() # this file's path
NBS_DIR = THIS_FILE_PATH.parent  # notebooks directory
REPO_DIR = NBS_DIR.parent
DJANGO_BASE_DIR = REPO_DIR / "src"  # django project root folder


def init_django(project_name="home"):
    """Run administrative tasks."""
    os.chdir(DJANGO_BASE_DIR)
    sys.path.insert(0, str(DJANGO_BASE_DIR))
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'{project_name}.settings')
    os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
    import django
    django.setup()