PyAnsys Math
============

|pyansys| |pypi| |PyPIact| |GH-CI| |codecov| |zenodo| |MIT| |black|

.. |pyansys| image:: https://img.shields.io/badge/Py-Ansys-ffc107.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAABDklEQVQ4jWNgoDfg5mD8vE7q/3bpVyskbW0sMRUwofHD7Dh5OBkZGBgW7/3W2tZpa2tLQEOyOzeEsfumlK2tbVpaGj4N6jIs1lpsDAwMJ278sveMY2BgCA0NFRISwqkhyQ1q/Nyd3zg4OBgYGNjZ2ePi4rB5loGBhZnhxTLJ/9ulv26Q4uVk1NXV/f///////69du4Zdg78lx//t0v+3S88rFISInD59GqIH2esIJ8G9O2/XVwhjzpw5EAam1xkkBJn/bJX+v1365hxxuCAfH9+3b9/+////48cPuNehNsS7cDEzMTAwMMzb+Q2u4dOnT2vWrMHu9ZtzxP9vl/69RVpCkBlZ3N7enoDXBwEAAA+YYitOilMVAAAAAElFTkSuQmCC
   :target: https://docs.pyansys.com/
   :alt: PyAnsys

.. |pypi| image:: https://img.shields.io/pypi/v/ansys-math-core.svg?logo=python&logoColor=white
   :target: https://pypi.org/project/ansys-math-core/

.. |PyPIact| image:: https://img.shields.io/pypi/dm/ansys-math-core.svg?label=PyPI%20downloads
   :target: https://pypi.org/project/ansys-math-core/

.. |codecov| image:: https://codecov.io/gh/pyansys/ansys-math/branch/main/graph/badge.svg
   :target: https://codecov.io/gh/pyansys/ansys-math

.. |GH-CI| image:: https://github.com/pyansys/ansys-math/actions/workflows/ci_cd.yml/badge.svg
   :target: https://github.com/pyansys/ansys-math/actions/workflows/ci_cd.yml

.. |zenodo| image:: https://zenodo.org/badge/70696039.svg
   :target: https://zenodo.org/badge/latestdoi/70696039

.. |MIT| image:: https://img.shields.io/badge/License-MIT-yellow.svg
   :target: https://opensource.org/licenses/MIT

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg?style=flat
  :target: https://github.com/psf/black
  :alt: black


PyAnsys Math is a Python repository holding Ansys mathematical libraries.
To use them, you must have a local installation of Ansys Mechanical APDL.

For more information on getting a licensed copy of Ansys Mechanical APDL, visit
the `Ansys web site <ansys_>` .



Installation
------------

For users
~~~~~~~~~
The ``ansys.math.core`` package currently supports Python 3.7 through
Python 3.10 on Windows, Mac OS, and Linux.

.. code::

   pip install ansys-math-core

Alternatively, install the latest from 
`PyAnsys Math GitHub <pymath_github_>`_ via:

.. code::

   pip install git+https://github.com/pyansys/ansys-math.git



For developers
~~~~~~~~~~~~~~
For a local *development* version, install with:

.. code::

   git clone https://github.com/pyansys/ansys-math.git
   cd ansys-math
   pip install -e .

This allows you to install and edit the ``ansys-math-core`` module locally.
The changes that you make are reflected in your setup
after restarting the Python kernel.


Verify your installation
------------------------

Check that you can start PyAnsys Math from Python by running this code:

.. code:: python

    import ansys.math.core.math as pymath

    # Start PyAnsys Math.
    mm = pymath.AnsMath()
    print(mm)


If you see a response from the server, congratulations. You're ready
to start using PyAnsys Math as a service.

Ansys software requirements
---------------------------

You must have a copy of Ansys 2021 R1 or later installed locally.

.. note::

    The latest versions of Ansys provide significantly better support
    and features. PyAnsys Math is not supported on Ansys versions earlier than 2021 R1.
