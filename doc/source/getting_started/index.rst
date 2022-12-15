===============
Getting started
===============
To use Ansys Math, you must have a local installation of Ansys.

For more information on getting a licensed copy of Ansys, visit
`Ansys <ansys_>`_ .



************
Installation
************

Python module
~~~~~~~~~~~~~
The ``ansys.mapdl.core`` package currently supports Python 3.7 through
Python 3.10 on Windows, Mac OS, and Linux.

.. code::

   pip install ansys-ansys-math-core

Alternatively, install the latest from 
`Ansys Math GitHub <ansys_math_>`_ via:

.. code::

   pip install git+https://github.com/pyansys/ansys-math.git


For a local *development* version, install with:

.. code::

   git clone https://github.com/pyansys/ansys-math.git
   cd pymapdl
   pip install -e .

This allows you to install the ``ansys-math-core`` module
and modify it locally and have the changes reflected in your setup
after restarting the Python kernel.


Verify your installation
~~~~~~~~~~~~~~~~~~~~~~~~
Check that you can start Ansys Math from Python by running:

.. code:: python

    >>> from ansys.math.core.math import launch_math
    >>> mm = launch_math()
    >>> print(mm)

        !!!!!!!!! TO BE MODIFIED  !!!!!!!!!!!!!!!!!


If you see a response from the server, congratulations. You're ready
to get started using Ansys Math as a service.