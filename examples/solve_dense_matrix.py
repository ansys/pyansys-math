"""
Use Ansys Math to Solve a Dense Matrix Linear System
----------------------------------------------------
Use Ansys Math to solve a Dense Matrix Linear System.

"""

import time

import numpy.linalg as npl

import ansys.math.core.math as amath

# Start Ansys Math
mm = amath.Math()

###############################################################################
# Allocate a Dense Matrix in the APDLMath workspace
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
# Solve using APDLMath
#
print(f"Solving a ({dim} x {dim}) dense linear system using MAPDL...")

t1 = time.time()
s = mm.factorize(a)
x = s.solve(b, x)
t2 = time.time()
print(f"Elapsed time to solve the linear system using Mapdl: {t2 - t1} seconds")

###############################################################################
# Norm of the MAPDL Solution
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
# stop mapdl
mm._mapdl.exit()
