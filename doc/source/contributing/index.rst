.. _ref_contributing:

Contributing
============

Overall guidance on contributing to a PyAnsys library appears in the
`Contributing <dev_guide_contributing_>`_ topic
in the *PyAnsys Developer's Guide*. Ensure that you are thoroughly familiar
with it and all `Coding style <dev_guide_coding_style_>`_ before attempting to
contribute to PyMAPDL.
 
The following contribution information is specific to PyMAPDL.

Cloning the AnsysMath repository
--------------------------------

Run this code to clone and install the latest version of PyMAPDL in development mode::

    git clone https://github.com/pyansys/ansys-math
    cd ansys-math
    python -m pip install --upgrade pip
    pip install -e .

Posting issues
--------------

Use the `AnsysMath Issues <amath_issues_>`_ page to submit questions,
report bugs, and request new features. When possible,use these issue
templates:

* Bug report template
* Feature request template

If your issue does not fit into one of these categories, create your own issue.

To reach the project support team, email `pyansys.support@ansys.com <pyansys_support_>`_.


Building documentation
----------------------

To build the AnsysMath documentation locally, in the root directory of the repository, run::
    
    pip install .[doc]
    .\doc\make.bat html 

Documentation for the latest stable release of AnsysMath is hosted at
`AnsysMath Documentation <amath_docs_>`_.

Documentation for the latest development version, which tracks the
``main`` branch, is hosted at 
`Development AnsysMath Documentation <amath_dev_docs_>`_.
This version is automatically kept up to date via GitHub actions.


Code style
----------

AnsysMath follows PEP8 standard as outlined in the `PyAnsys Development Guide
<dev_guide_pyansys_>`_ and implements style checking using
`pre-commit <precommit_>`_.

To ensure your code meets minimum code styling standards, run::

  pip install pre-commit
  pre-commit run --all-files

You can also install this as a pre-commit hook by running::

  pre-commit install

This way, it's not possible for you to push code that fails the style checks. For example::

  $ pre-commit install
  $ git commit -am "added my cool feature"
  black....................................................................Passed
  blacken-docs.............................................................Passed
  isort....................................................................Passed
  flake8...................................................................Passed
  codespell................................................................Passed
  check for merge conflicts................................................Passed
  debug statements (python)................................................Passed
  Validate GitHub Workflows................................................Passed

