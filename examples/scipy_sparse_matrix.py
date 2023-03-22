"""
AnsMath sparse matrices and SciPy sparse matrices
-------------------------------------------------

This example shows how to get AnsMath sparse matrices into SciPy
sparse matrices.

"""
###############################################################################
# Perform required imports and start PyAnsys
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Perform required imports.

from ansys.mapdl.core.examples import vmfiles
import matplotlib.pylab as plt

import ansys.math.core.math as pymath

# Start PyAnsys Math as a service.
mm = pymath.AnsMath()

################################################################################
# Get matrices
# ~~~~~~~~~~~~
# Run the input file from Verification Manual 153 and then
# get the stiff (``k``) matrix from the FULL file.

out = mm._mapdl.input(vmfiles["vm153"])
k = mm.stiff(fname="PRSMEMB.full")

################################################################################
# Copy AnsMath sparse matrix to SciPy CSR matrix and plot
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Copy the AnsMath sparse matrix to a SciPy CSR matrix. Then, plot the
# graph of the sparse matrix.

pk = k.asarray()
plt.spy(pk, color="orange", markersize=3)
plt.title("AnsMath sparse matrix")
plt.show()


################################################################################
# Access vectors
# ~~~~~~~~~~~~~~
# You can access the three vectors that describe this sparse matrix with:
#
# - ``pk.data``
# - ``pk.indices``
# - ``pk.indptr``
#
# For more information, see SciPy's class description for the
# `CSR (compressed sparse row) matrix
# <https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csr_matrix.html>`_.

print(pk.data[:10])
print(pk.indices[:10])
print(pk.indptr[:10])


################################################################################
# Create AnsMath sparse matrix from SciPy sparse CSR matrix
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Create an AnsMath sparse matrix from a SciPy sparse CSR matrix.
# Then, transfer the SciPy CSR matrix back to PyAnsys Math.
#
# While this code uses a matrix that was originally within MAPDL, you can
# load any CSR matrix into PyAnsys Math.

my_mat = mm.matrix(pk, "my_mat", triu=True)
my_mat

################################################################################
# Check that the matrices ``k`` and ``my_mat`` are exactly the sames. The
# norm of the difference should be zero.

msub = k - my_mat
mm.norm(msub)


################################################################################
# Print CSR representation in PyAnsys Math
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# Printing the list of objects for the CSR representation in the PyAnsys Math
# space finds these objects:
#
# - Two SMAT objects, corresponding to the ``k``, ``MSub`` matrices,
#   with encrypted names.
# - The ``my_mat`` SMAT object. Its size is zero because the three
#   vectors are stored separately.
# - The three vectors of the CSR ``my_mat`` structure: ``MY_MAT_PTR``,
#   ``MY_MAT_IND``, and ``MY_MAT_DATA``.

mm.status()


################################################################################
# Access ID of Python object
# ~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# To determine which PyAnsys Math object corresponds to which Python object,
# access the ``id`` property of the Python object.

print("name(k)=" + k.id)
print("name(my_mat)=" + my_mat.id)
print("name(msub)=" + msub.id)


###############################################################################
# Stop PyAnsys Math
# ~~~~~~~~~~~~~~~~~
# Stop PyAnsys Math.

mm._mapdl.exit()
