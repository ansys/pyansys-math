"""
Use PyAnsys-Math to solve a dense matrix linear system
---------------------------------------------------
This example shows how so use PyAnsys-Math to solve a dense matrix linear system.

"""

import time

import numpy.linalg as npl

import ansys.math.core.math as pymath

# Start PyAnsys-Math
mm = pymath.AnsMath()

###############################################################################
# Allocate a Dense Matrix in the MAPDL workspace
#
mm._mapdl.clear()
dim = 1000
a = mm.rand(dim, dim)
b = mm.rand(dim)
x = mm.zeros(dim)

###############################################################################
# Copy the matrices as numpy arrays before they are modified by
# factorization call
#
a_py = a.asarray()
b_py = b.asarray()

###############################################################################
# Solve using PyAnsys-Math
#
print(f"Solving a ({dim} x {dim}) dense linear system using PyAnsys-Math...")

t1 = time.time()
s = mm.factorize(a)
x = s.solve(b, x)
t2 = time.time()
print(f"Elapsed time to solve the linear system using PyAnsys-Math: {t2 - t1} seconds")

###############################################################################
# Norm of the PyAnsys-Math solution
mm.norm(x)


###############################################################################
# Solve the solution using numpy
#
print(f"Solving a ({dim} x {dim}) dense linear system using numpy...")

t1 = time.time()
x_py = npl.solve(a_py, b_py)
t2 = time.time()
print(f"Elapsed time to solve the linear system using numpy: {t2 - t1} seconds")

###############################################################################
# Norm of the numpy Solution
#
npl.norm(x_py)

###############################################################################
# Stop PyAnsys-Math
mm._mapdl.exit()
