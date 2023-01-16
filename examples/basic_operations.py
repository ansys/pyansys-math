"""
.. _ref_ansys-math_basic:

PyAnsys-Math basic operations
--------------------------

This tutorial shows how you can use PyAnsys-Math for basic
operations on AnsMath vectors and matrices in the APDL memory
workspace.

"""

import numpy as np

import ansys.math.core.math as amath

# Start PyAnsys-Math as a service.
mm = amath.AnsMath()

###############################################################################
# Create and Manipulate Vectors
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Create 2 AnsMath vectors of size 5. :math:`\vec{v}` is initialized with
# ones, $\vec{w}$ is filled with random values
#

v = mm.ones(5)
w = mm.rand(5)
print(w)


###############################################################################
# Use operators on vectors
# ~~~~~~~~~~~~~~~~~~~~~~~~
# Just like `numpy` PyAnsys-Math vectors can use most of the
# standard operators (e.g. ``+, -, +=, -=, *=``)
#
# Here this form is used :math:`\vec{z}=\vec{v}+\vec{w}`
#
# Then we compute :math:`\|z\|_2` (the default `norm` is nrm2, but you
# can use `.norm('nrm1')` or `.norm('nrminf')` for different normals.
# See `help(z.norm)` for additional details.
#

z = v + w
z.norm()


###############################################################################
# Methods
# ~~~~~~~
# Alternatively you can use methods, following the numpy
# standards. Available methods are:
#
# - `mm.add()`
# - `mm.subtract()`
# - `mm.dot()`
#
# Equivalent operator:
# `z = v + w`
#

z = mm.add(v, w)
z.norm()

###############################################################################
# Subtraction
#
# Equivalent operator:
# z = v - w
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
# In-place addition

v += v
print(v)


###############################################################################
# In-place multiplication

v *= 2
print(v)

###############################################################################
# In-Place Multiplication

v /= 2.0
print(v)


###############################################################################
# Working with dense matrices
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
# ***Transpose*** a Matrix

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
# AnsMath matrices can be identified by printing, viewing their types, or with
# using the `__repr__` method by simply typing out the variable
#
# AnsMath Matrix
# ~~~~~~~~~~~~~~~

type(m1)
print(m1)
m1


###############################################################################
# AnsMath Vector

type(w)
print(w)
w

###############################################################################
# Numpy methods on AnsMath objects
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Regardless of the underlying AnsMath object type, you are generally
# able to perform most numpy or scipy operations on these arrays.  You
# can do this one of two ways.  First, you can convert a matrix to a numpy array:

apdl_mat = mm.rand(5, 5)
np_mat = apdl_mat.asarray()
print(np_mat)


###############################################################################
# Alternatively, you can use NumPy to compute the maximum of the array.
#
# This works because PyAnsys-Math copies over the matrix to the local
# Python memory and then computes the maximum using NumPy.

print(np.max(apdl_mat))


###############################################################################
# This works for most numpy operations, but keep in mind that
# operations that are supported within PyAnsys-Math (such as adding or
# multiplying arrays) compute much faster because the data is not copied.

apdl_arr = mm.rand(5, 5)
np_array = apdl_mat.asarray()
print(np.allclose(apdl_mat, np_array))

###############################################################################
# Stop PyAnsys-Math

mm._mapdl.exit()
