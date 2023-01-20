
PyAnsys Math documentation
==========================

Introduction
------------

PyAnsys Math aims to gather all the mathematical calculation tools present
in the Ansys software.

This library provides the ability to access and manipulate large
sparse matrices and solve a variety of eigenproblems. It is presented in a
similar manner to the popular `NumPy <numpy_docs_>`_ and
`SciPy <scipy_docs_>`_ libraries.

The PyAnsys Math command set is based on tools for manipulating large mathematical
matrices and vectors that provide access to standard linear algebra operations and the
powerful sparse linear solvers of Ansys Mechanical APDL, providing the ability to solve
eigenproblems.

Python and MATLAB eigensolvers are based on the publicly available
LAPACK libraries and provide reasonable solve time for eigenproblems
with relatively small degrees of freedom (dof), perhaps 100,000.
However, Ansys solvers are designed for the scale of hundreds of
millions of dof, providing a variety of situations where you can
directly leverage Ansys high-performance solvers on a variety of
eigenproblems. Fortunately, you can leverage this without relearning
an entirely new language because PyAnsys Math is written in a similar manner
as the ``NumPy`` and ``SciPy`` libraries. For example, here is a comparison between
the NumPy and SciPy linear algebra solvers and the PyAnsys Math solver:

.. table:: ``NumPy`` and ``SciPy`` vs ``PyAnsys Math`` implementation

   +--------------------------------------------+-----------------------------------+
   | ``NumPy`` and ``SciPy``                    | ``PyAnsys Math``                  |
   +============================================+===================================+
   | .. code:: python                           | .. code:: python                  |
   |                                            |                                   |
   |   k_py = k + sparse.triu(k, 1).T           |   k = mm.matrix(k_py, triu=True)  |
   |   m_py = m + sparse.triu(m, 1).T           |   m = mm.matrix(m_py, triu=True)  |
   |   n = 10                                   |   n = 10                          |
   |   ev = linalg.eigsh(k_py, k=neqv, M=m_py)  |   ev = mm.eigs(n, k, m)           |
   |                                            |                                   |
   +--------------------------------------------+-----------------------------------+


Background
----------

PyAnsys Math is a library using the Ansys Mechanical APDL (MAPDL) solver in the
background.

It is based on the ``launch_mapdl()`` method from the `ansys-mapdl-core
<pymapdl_github_>`_ library. The latter uses `gRPC <grpc_>`_, which allows
the MAPDL solver to function as a server, ready to respond to connecting
clients.

Google Remote Procedure Calls, or gRPC, are used to establish secure 
connections so that a client app can directly call methods on 
a potentially remote MAPDL instance as if it were a local object. The 
use of HTTP/2 makes it friendly to modern internet infrastructures. 
This, along with the use of binary transmission formats, favors higher
performance.


Quick code
----------

Here is a brief example of how you use PyAnsys Math:

.. code:: python

    import ansys.math.core.math as pymath

    mm = pymath.AnsMath()

    u = mm.ones(5)
    v = mm.rand(5)
    w = u + v

    print(w)

.. code:: output

      UDWZKD :
      Size : 5
      1.417e+00   1.997e+00   1.720e+00   1.933e+00   1.000e+00      <       5


For additional PyAnsys Math examples, see :ref:`ref_pymath_examples`.


.. toctree::
   :hidden:
   :maxdepth: 1

   getting_started/index
   api_ref/index
   examples/index
   contributing/index
