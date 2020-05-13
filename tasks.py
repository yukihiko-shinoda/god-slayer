"""
Tasks for maintaining the project.

Execute 'invoke --list' for guidance on using Invoke
"""
import shutil
import platform

from invoke import task
from pathlib import Path
import webbrowser


ROOT_DIR = Path(__file__).parent
SETUP_FILE = ROOT_DIR.joinpath("setup.py")
TEST_DIR = ROOT_DIR.joinpath("tests")
SOURCE_DIR = ROOT_DIR.joinpath("godslayer")
TOX_DIR = ROOT_DIR.joinpath(".tox")
COVERAGE_FILE = ROOT_DIR.joinpath(".coverage")
COVERAGE_DIR = ROOT_DIR.joinpath("htmlcov")
COVERAGE_REPORT = COVERAGE_DIR.joinpath("index.html")
PYTHON_DIRS = [str(d) for d in [SOURCE_DIR, TEST_DIR]]


def _delete_file(file):
    try:
        file.unlink(missing_ok=True)
    except TypeError:
        # missing_ok argument added in 3.8
        try:
            file.unlink()
        except FileNotFoundError:
            pass


@task(help={'check': "Checks if source is formatted without applying changes"})
def format(c, check=False):
    """
    Format code
    """
    python_dirs_string = " ".join(PYTHON_DIRS)
    # Run isort
    isort_options = '--recursive {}'.format(
        '--check-only' if check else '')
    c.run("isort {} {}".format(isort_options, python_dirs_string))
    # Run black
    black_options = '{}'.format('--check --diff' if check else '')
    c.run("black {} {}".format(black_options, python_dirs_string))


@task
def lint_flake8(c):
    """
    Lint code with flake8
    """
    c.run("flake8 {}".format(" ".join(PYTHON_DIRS)))


@task
def lint_pylint(c):
    """
    Lint code with pylint
    """
    c.run("pylint {}".format(" ".join(PYTHON_DIRS)))


@task(lint_flake8, lint_pylint)
def lint(c):
    """
    Run all linting
    """


@task
def test(c):
    """
    Run tests
    """
    pty = platform.system() == 'Linux'
    c.run("python {} test".format(SETUP_FILE), pty=pty)


@task(help={
    'publish': "Publish the result via coveralls",
    'xml': "Export report as xml format",
})
def coverage(c, publish=False, xml=False):
    """
    Create coverage report
    """
    c.run("coverage run --source {} -m pytest".format(SOURCE_DIR))
    c.run("coverage report")
    if publish:
        # Publish the results via coveralls
        c.run("coveralls")
        return
    # Build a local report
    if xml:
        c.run("coverage xml")
    else:
        c.run("coverage html")
        webbrowser.open(COVERAGE_REPORT.as_uri())


@task
def clean_build(c):
    """
    Clean up files from package building
    """
    c.run("rm -fr build/")
    c.run("rm -fr dist/")
    c.run("rm -fr .eggs/")
    c.run("find . -name '*.egg-info' -exec rm -fr {} +")
    c.run("find . -name '*.egg' -exec rm -f {} +")


@task
def clean_python(c):
    """
    Clean up python file artifacts
    """
    c.run("find . -name '*.pyc' -exec rm -f {} +")
    c.run("find . -name '*.pyo' -exec rm -f {} +")
    c.run("find . -name '*~' -exec rm -f {} +")
    c.run("find . -name '__pycache__' -exec rm -fr {} +")


@task
def clean_tests(c):
    """
    Clean up files from testing
    """
    _delete_file(COVERAGE_FILE)
    shutil.rmtree(TOX_DIR, ignore_errors=True)
    shutil.rmtree(COVERAGE_DIR, ignore_errors=True)


@task(pre=[clean_build, clean_python, clean_tests])
def clean(c):
    """
    Runs all clean sub-tasks
    """
    pass


@task(clean)
def dist(c):
    """
    Build source and wheel packages
    """
    c.run("python setup.py sdist bdist_wheel")