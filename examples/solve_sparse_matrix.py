"""
Perform sparse factorization and solve operations
-------------------------------------------------

Using PyAnsys Math, you can solve linear systems of equations
based on sparse or dense matrices.

"""
# Perform required imports and start PyAnsys
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Perform required imports.

from ansys.mapdl.core.examples import vmfiles
import matplotlib.pyplot as plt

import ansys.math.core.math as pymath

# Start PyAnsys Math as a server.
mm = pymath.AnsMath()

###############################################################################
# Factorize and solve sparse linear systems
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Run a MAPDL solve to create a Full file. This code
# uses a model from the official verification manual.
#
# After a solve command, the ``FULL`` file contains the assembled stiffness
# matrix, mass matrix, and load vector.
#
out = mm._mapdl.input(vmfiles["vm153"])

###############################################################################
# List files in current directory
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# List the files in current directory.
#
mm._mapdl.list_files()

###############################################################################
# Extract stiffness matrix
# ~~~~~~~~~~~~~~~~~~~~~~~~
# Extract the stiffness matrix from the FULL file in a sparse
# matrix format. For help on the ``stiff`` function, use the
# ``help(mm.stiff)`` command.
#
# Print dimensions of sparse matrix
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Print the dimensions of the sparse matrix.

k = mm.stiff(fname="PRSMEMB.full", name="K")
k

################################################################################
# Copy AnsMath sparse matrix to SciPy CSR matrix and plot
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Copy the AnsMath sparse matrix to a SciPy CSR matrix. Then, plot the
# graph of the sparse matrix.

pk = k.asarray()
plt.spy(pk, color="orange")
plt.title("AnsMath sparse matrix")
plt.show()

###############################################################################
# Get a copy of sparse matrix as a NumPy array
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Get a copy of the ``k`` sparse matrix as a NumPy array

ky = k.asarray()
ky

###############################################################################
# Extract load vector from FULL file and print norm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Extract the load vector from the FULL file and print the norm of this
# vector.

b = mm.rhs(fname="PRSMEMB.full", name="B")
b.norm()

###############################################################################
# Get a copy of load vector as a NumPy array
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Get a copy of the load vector as a NumPy array.

by = b.asarray()

###############################################################################
# Factorize stiffness matrix
# ~~~~~~~~~~~~~~~~~~~~~~~~~~
# Factorize the stiffness matrix using PyAnsys Math.
#
s = mm.factorize(k)

###############################################################################
# Solve linear system
# ~~~~~~~~~~~~~~~~~~~
# Solve the linear system.

x = s.solve(b)

###############################################################################
# Print norm** of solution vector
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Print the norm of the solution vector.

x.norm()

###############################################################################
# Check accuracy of solution
# ~~~~~~~~~~~~~~~~~~~~~~~~~~
# Check the accuracy of the solution by verifying that
# :math:`KX - B = 0`.

kx = k.dot(x)
kx -= b
print("Residual error:", kx.norm() / b.norm())

###############################################################################
# Get a summary of allocated objects
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Get a summary of all allocated AnsMath objects.

mm.status()

######################################################################
# Delete all AnsMath objects
# ~~~~~~~~~~~~~~~~~~~~~~~~~~
# Delete all AnsMath objects.

mm.free()

###############################################################################
# Stop PyAnsys Math
# ~~~~~~~~~~~~~~~~~
# Stop PyAnsys Math.

mm._mapdl.exit()
