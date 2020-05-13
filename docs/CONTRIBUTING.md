# Contributing

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

## Types of Contributions

### Report Bugs

<!-- markdownlint-disable no-bare-urls -->
Report bugs at https://github.com/yukihiko-shinoda/god-slayer/issues.
<!-- markdownlint-enable no-bare-urls -->

If you are reporting a bug, please include:

- Your operating system name and version.
- Any details about your local setup that might be helpful in troubleshooting.
- Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

### Write Documentation

God Slayer could always use more documentation, whether as part of the
official God Slayer docs, in docstrings, or even on the web in blog posts,
articles, and such.

### Submit Feedback

<!-- markdownlint-disable no-bare-urls -->
The best way to send feedback is to file an issue at https://github.com/yukihiko-shinoda/god-slayer/issues.
<!-- markdownlint-enable no-bare-urls -->

If you are proposing a feature:

- Explain in detail how it would work.
- Keep the scope as narrow as possible, to make it easier to implement.
- Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

<!-- markdownlint-disable no-trailing-punctuation -->
## Get Started!
<!-- markdownlint-enable no-trailing-punctuation -->

Ready to contribute? Here's how to set up `god-slayer` for local development.

1. Fork the `god-slayer` repo on GitHub.
2. Clone your fork locally:

    ```console
    git clone git@github.com:your_name_here/god-slayer.git
    ```

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development:

    ```console
    mkvirtualenv god-slayer
    cd god-slayer/
    python setup.py develop
    ```

4. Create a branch for local development:

    ```console
    git checkout -b name-of-your-bugfix-or-feature
    ```

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass flake8 and the
   tests, including testing other Python versions with tox:

    ```console
    flake8 godslayer tests
    python setup.py test or pytest
    tox
    ```

   To get flake8 and tox, just pip install them into your virtualenv.

6. Commit your changes and push your branch to GitHub:

    ```console
    git add .
    git commit -m "Your detailed description of your changes."
    git push origin name-of-your-bugfix-or-feature
    ```

7. Submit a pull request through the GitHub website.

## Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for Python 3.5, 3.6, 3.7 and 3.8, and for PyPy. Check
<!-- markdownlint-disable no-bare-urls -->
   https://travis-ci.com/yukihiko-shinoda/god-slayer/pull_requests
<!-- markdownlint-enable no-bare-urls -->
   and make sure that the tests pass for all supported Python versions.

## Tips

To run a subset of tests:

```console
pytest tests.test_godslayer
```

## Deploying

A reminder for the maintainers on how to deploy.
Make sure all your changes are committed (including an entry in HISTORY.rst).
Then run:

```console
bump2version patch # possible: major / minor / patch
git push
git push --tags
```

Travis will then deploy to PyPI if tests pass.
