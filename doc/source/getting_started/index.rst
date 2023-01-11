Getting started
===============
To use AnsysMath, you must have a local installation of Ansys.

For more information on getting a licensed copy of Ansys, visit
`Ansys <ansys_>`_ .



Installation
------------

For users
~~~~~~~~~
The ``ansys.math.core`` package currently supports Python 3.7 through
Python 3.10 on Windows, Mac OS, and Linux.

.. code::

   pip install ansys-math-core

Alternatively, install the latest from 
`AnsysMath GitHub <ansys_math_github_>`_ via:

.. code::

   pip install git+https://github.com/pyansys/ansys-math.git



For developers
~~~~~~~~~~~~~~~
For a local *development* version, install with:

.. code::

   git clone https://github.com/pyansys/ansys-math.git
   cd ansys-math
   pip install -e .

This allows you to install the ``ansys-math-core`` module
and modify it locally and have the changes reflected in your setup
after restarting the Python kernel.


Verify your installation
------------------------

Check that you can start AnsysMath from Python by running:

.. code:: python

    import ansys.math.core.math as amath

    # Start AnsysMath
    mm = amath.Math()
    print(mm)


If you see a response from the server, congratulations. You're ready
to get started using AnsysMath as a service.

Ansys software requirements
---------------------------

You must have a copy of Ansys 2021 R1 or later installed locally.

.. note::

    The latest versions of Ansys provide significantly better support
    and features. AnsysMath is not supported on earlier Ansys versions.
