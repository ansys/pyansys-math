"""
.. _ref_ansys-math_basic:

PyAnsys Math basic operations
-----------------------------

This tutorial shows how you can use PyAnsys Math for basic
operations on AnsMath vectors and matrices in the APDL memory
workspace.

"""

import matplotlib.pyplot as plt
import numpy as np

import ansys.math.core.math as pymath

# Start PyAnsys Math as a service.
mm = pymath.AnsMath()

###############################################################################
# Create and manipulate vectors.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Create two AnsMath vectors of size 5. The :math:`\vec{v}` method is initialized with
# ones, and $\vec{w}$ is filled with random values.
#

v = mm.ones(2)
w = mm.rand(2)
print(v)
print(w)

###############################################################################
# Plot the created vectors.
# ~~~~~~~~~~~~~~~~~~~~~~~~~
#

origin = np.array([[0, 0], [0, 0]])
plt.title("Vectors V and W")
plt.quiver(*origin, v, w, angles="xy", scale_units="xy", scale=1, color=["orange", "gray"])
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.show()


###############################################################################
# Use operators on vectors.
# ~~~~~~~~~~~~~~~~~~~~~~~~~
# Like NumPy vectors, AnsMath vectors can use most of the
# standard operators (``+, -, +=, -=, *=``).
#
# Here this form is used :math:`\vec{z}=\vec{v}+\vec{w}`
#
# Then compute :math:`\|z\|_2` (the default `norm` is nrm2. Note that you
# can use `.norm('nrm1')` or `.norm('nrminf')` for different normals.
# For additional information, see `help(z.norm)`.
#

z = v + w
z.norm()


###############################################################################
# Methods
# ~~~~~~~
# Alternatively you can use methods, following the numpy
# standards. Available methods are:
#
# - ``mm.add()``
# - ``mm.subtract()``
# - ``mm.dot()``
#
# Equivalent operator:
# ``z = v + w``
#

z = mm.add(v, w)
z.norm()

###############################################################################
# Subtraction
#
# Equivalent operator:
# ``z = v - w``
#

z = mm.subtract(v, w)
print(z)

###############################################################################
# Dot product of 2 vectors
#

vw = mm.dot(v, w)
print("Dot product :", str(vw))


###############################################################################
# Perform an in-place operations (without copying vectors)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# Perform in-place addition.

v += v
print(v)


###############################################################################
# Perform in-place multiplication.

v *= 2
print(v)

###############################################################################
# In-Place Multiplication

v /= 2.0
print(v)


###############################################################################
# Working with dense matrices.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Allocate two dense matrices with random values.

m1 = mm.rand(4, 5)
m2 = mm.ones(4, 5)
m1, m2

###############################################################################
# **Add** these 2 dense matrices and **scale** the result matrix.

m3 = m1 + m2
print(m3)

m3 *= 2
print(m3)

###############################################################################
# **Transpose** a Matrix

m4 = m3.T
print(m4)


###############################################################################
# As for vectors, methods are also available as an alternative to operators.

m3 = mm.add(m1, m2)
print(m3)


###############################################################################
# Compute a matrix vector multiplication

mw = m3.dot(m4)
print(mw)

###############################################################################
# AnsMath matrices can be identified by printing, viewing their types, or
# using the `__repr__` method by simply typing out the variable.
#
# Here is an example with an AnsMath matrix.
#

type(m1)
print(m1)
m1

###############################################################################
# Here is an example with an AnsMath vector.
#

type(w)
print(w)
w

###############################################################################
# Use NumPy methods on AnsMath objects.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Regardless of the underlying AnsMath object type, you are generally
# able to perform most NumPy or SciPy operations on these arrays. You
# can do this in one of two ways. First, you can convert a matrix to a NumPy array:

apdl_mat = mm.rand(5, 5)
np_mat = apdl_mat.asarray()
print(np_mat)


###############################################################################
# Alternatively, you can use NumPy to compute the maximum of the array.
#
# This works because PyAnsys Math copies over the matrix to the local
# Python memory and then computes the maximum using NumPy.

print(np.max(apdl_mat))


###############################################################################
# This works for most numpy operations, but keep in mind that
# operations that are supported within PyAnsys Math (such as adding or
# multiplying arrays) compute much faster because the data is not copied.

apdl_arr = mm.rand(5, 5)
np_array = apdl_mat.asarray()
print(np.allclose(apdl_mat, np_array))

###############################################################################
# Stop PyAnsys Math.

mm._mapdl.exit()
