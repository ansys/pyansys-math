"""
Perform sparse factorization and solve operations
-------------------------------------------------

Using PyAnsys-Math, you can solve linear systems of equations
based on sparse or dense matrices.

"""
from ansys.mapdl.core.examples import vmfiles

import ansys.math.core.math as pymath

# Start PyAnsys-Math
mm = pymath.AnsMath()

###############################################################################
# Factorize and Solve Sparse Linear Systems
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# First, run a MAPDL solve to create a .full file
# We use a model from the official verification manual.
#
# After a solve command, the full contains the assemblied stiffness
# matrix, mass matrix, and the load vector.
#
out = mm._mapdl.input(vmfiles["vm153"])

###############################################################################
# List the files in current directory
#
mm._mapdl.list_files()

###############################################################################
# Extract the Stiffness matrix from the ``FULL`` file, in a sparse
# matrix format.
#
# You can get help on the stiff function with ``help(mm.stiff)``
#
# Printout the dimensions of this Sparse Matrix
#
k = mm.stiff(fname="PRSMEMB.full")
k

###############################################################################
# Get a copy of the K Sparse Matrix as a Numpy Array
#
ky = k.asarray()
ky

###############################################################################
# Extract the load vector from the ``FULL`` file.
#
# Printout the norm of this vector.
#
b = mm.rhs(fname="PRSMEMB.full")
b.norm()

###############################################################################
# Get a copy of the load vector as a numpy array
#
by = b.asarray()

###############################################################################
# Factorize the stifness matrix using PyAnsys-Math
#
s = mm.factorize(k)

###############################################################################
# Solve the linear system
#
x = s.solve(b)

###############################################################################
# Print the **norm** of the solution vector
#
x.norm()

###############################################################################
# We check the accuracy of the solution, by verifying that
#
# :math:`KX - B = 0`
#
kx = k.dot(x)
kx -= b
print("Residual error:", kx.norm() / b.norm())

###############################################################################
# Summary of all allocated AnsMath Objects
#
mm.status()

######################################################################
# Delete all AnsMath Objects
#
mm.free()


###############################################################################
# Stop PyAnsys-Math
mm._mapdl.exit()
