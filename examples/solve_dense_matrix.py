"""
Use AnsysMath to solve a dense matrix linear system
---------------------------------------------------
This example shows how so use AnsysMath to solve a dense matrix linear system.

"""

import time

import numpy.linalg as npl

import ansys.math.core.math as amath

# Start AnsysMath
mm = amath.AnsMath()

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
# Solve using AnsysMath
#
print(f"Solving a ({dim} x {dim}) dense linear system using AnsysMath...")

t1 = time.time()
s = mm.factorize(a)
x = s.solve(b, x)
t2 = time.time()
print(f"Elapsed time to solve the linear system using AnsysMath: {t2 - t1} seconds")

###############################################################################
# Norm of the AnsysMath solution
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
# Stop AnsysMath
mm._mapdl.exit()
