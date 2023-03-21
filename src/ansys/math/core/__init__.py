"""This init file allows python to treat directories containing it as modules.

Import any methods you want exposed at your library level here.

For example, if you want to avoid this behavior:

.. code::

   >>> from ansys.product.library.module import add

Then add the import within this module to enable:

.. code::

   >>> from ansys.product import library
   >>> library.add(1, 2)

.. note::
   It's best to import the version here as well so it can be
   referenced at the library level.

"""

BUILDING_GALLERY = False

# Version
# ------------------------------------------------------------------------------

try:
    import importlib.metadata as importlib_metadata
except ModuleNotFoundError:  # pragma: no cover
    import importlib_metadata  # type: ignore

__version__ = importlib_metadata.version(__name__.replace(".", "-"))
"""PyAnsys Math version."""
