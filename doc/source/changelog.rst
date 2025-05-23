.. _ref_release_notes:

Release notes
#############

This document contains the release notes for the PyAnsys Math project.

.. vale off

.. towncrier release notes start

`0.2.3 <https://github.com/ansys/pyansys-math/releases/tag/v0.2.3>`_ - May 23, 2025
===================================================================================

.. tab-set::


  .. tab-item:: Added

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - feat: update changelog template
          - `#480 <https://github.com/ansys/pyansys-math/pull/480>`_

        * - feat: supporting python ``3.13``
          - `#511 <https://github.com/ansys/pyansys-math/pull/511>`_


  .. tab-item:: Dependencies

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - maint: bump jupyterlab from 4.3.4 to 4.3.5
          - `#471 <https://github.com/ansys/pyansys-math/pull/471>`_

        * - maint: bump pypandoc from 1.14 to 1.15
          - `#473 <https://github.com/ansys/pyansys-math/pull/473>`_

        * - maint: bump scipy from 1.14.1 to 1.15.2
          - `#477 <https://github.com/ansys/pyansys-math/pull/477>`_

        * - maint: bump pytest from 8.3.3 to 8.3.5
          - `#478 <https://github.com/ansys/pyansys-math/pull/478>`_

        * - maint: bump trame from 3.7.0 to 3.8.1
          - `#483 <https://github.com/ansys/pyansys-math/pull/483>`_

        * - maint: bump ansys-sphinx-theme from 1.2.6 to 1.3.3
          - `#488 <https://github.com/ansys/pyansys-math/pull/488>`_

        * - maint: bump numpy from 2.2.2 to 2.2.4
          - `#489 <https://github.com/ansys/pyansys-math/pull/489>`_

        * - maint: bump sphinx-gallery from 0.18.0 to 0.19.0
          - `#491 <https://github.com/ansys/pyansys-math/pull/491>`_

        * - maint: bump jupyterlab from 4.3.5 to 4.3.6
          - `#492 <https://github.com/ansys/pyansys-math/pull/492>`_

        * - maint: bump sphinx-notfound-page from 1.0.4 to 1.1.0
          - `#493 <https://github.com/ansys/pyansys-math/pull/493>`_

        * - maint: bump pyansys-tools-report from 0.8.1 to 0.8.2
          - `#494 <https://github.com/ansys/pyansys-math/pull/494>`_

        * - maint: bump vtk from 9.3.1 to 9.4.2
          - `#495 <https://github.com/ansys/pyansys-math/pull/495>`_

        * - maint: bump pytest-cov from 6.0.0 to 6.1.1
          - `#497 <https://github.com/ansys/pyansys-math/pull/497>`_

        * - maint: bump ansys-sphinx-theme from 1.3.3 to 1.4.2
          - `#498 <https://github.com/ansys/pyansys-math/pull/498>`_

        * - fix: removing ``attrs`` max version as it is no longer an issue
          - `#499 <https://github.com/ansys/pyansys-math/pull/499>`_

        * - maint: bump ansys-mapdl-core from 0.68.6 to 0.69.3
          - `#500 <https://github.com/ansys/pyansys-math/pull/500>`_

        * - maint: bump pyvista from 0.44.2 to 0.45.2
          - `#509 <https://github.com/ansys/pyansys-math/pull/509>`_

        * - maint: bump pyvista[jupyter,trame] from 0.44.2 to 0.45.2
          - `#510 <https://github.com/ansys/pyansys-math/pull/510>`_


  .. tab-item:: Miscellaneous

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - [pre-commit.ci] pre-commit autoupdate
          - `#476 <https://github.com/ansys/pyansys-math/pull/476>`_, `#487 <https://github.com/ansys/pyansys-math/pull/487>`_, `#503 <https://github.com/ansys/pyansys-math/pull/503>`_


  .. tab-item:: Documentation

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - chore: update CHANGELOG for v0.2.2
          - `#470 <https://github.com/ansys/pyansys-math/pull/470>`_


  .. tab-item:: Maintenance

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - ci: not using student for doc build
          - `#479 <https://github.com/ansys/pyansys-math/pull/479>`_

        * - ci: fix ``MAPDL`` version in ``build-test`` action
          - `#482 <https://github.com/ansys/pyansys-math/pull/482>`_

        * - maint: bump docker/login-action from 3.3.0 to 3.4.0 in the actions group
          - `#490 <https://github.com/ansys/pyansys-math/pull/490>`_

        * - docs: Update ``CONTRIBUTORS.md`` with the latest contributors
          - `#496 <https://github.com/ansys/pyansys-math/pull/496>`_

        * - maint: bump ansys/actions from 8 to 9 in the actions group
          - `#502 <https://github.com/ansys/pyansys-math/pull/502>`_


`0.2.2 <https://github.com/ansys/pyansys-math/releases/tag/v0.2.2>`_ - 2025-01-31
=================================================================================

Fixed
^^^^^

- fix: PR commenter added to release job `#469 <https://github.com/ansys/pyansys-math/pull/469>`_


Documentation
^^^^^^^^^^^^^

- chore: update CHANGELOG for v0.2.1 `#468 <https://github.com/ansys/pyansys-math/pull/468>`_

`0.2.1 <https://github.com/ansys/pyansys-math/releases/tag/v0.2.1>`_ - 2025-01-31
=================================================================================

Added
^^^^^

- feat: adding PR comments on release `#467 <https://github.com/ansys/pyansys-math/pull/467>`_


Fixed
^^^^^

- fix: avoid the usage of attrs 24.3.0 (temporary) `#466 <https://github.com/ansys/pyansys-math/pull/466>`_


Dependencies
^^^^^^^^^^^^

- maint: bump sphinx-autodoc-typehints from 2.4.4 to 2.5.0 `#427 <https://github.com/ansys/pyansys-math/pull/427>`_
- maint: bump ansys-mapdl-core from 0.68.5 to 0.68.6 `#428 <https://github.com/ansys/pyansys-math/pull/428>`_
- maint: bump pypandoc from 1.13 to 1.14 `#429 <https://github.com/ansys/pyansys-math/pull/429>`_
- maint: bump sphinx from 8.0.2 to 8.1.3 `#430 <https://github.com/ansys/pyansys-math/pull/430>`_
- maint: bump ansys-sphinx-theme from 1.1.2 to 1.1.4 `#431 <https://github.com/ansys/pyansys-math/pull/431>`_
- maint: bump sphinx-gallery from 0.17.1 to 0.18.0 `#434 <https://github.com/ansys/pyansys-math/pull/434>`_
- maint: bump trame from 3.6.5 to 3.7.0 `#435 <https://github.com/ansys/pyansys-math/pull/435>`_
- maint: bump pyansys-tools-report from 0.8.0 to 0.8.1 `#436 <https://github.com/ansys/pyansys-math/pull/436>`_
- maint: bump ansys-sphinx-theme from 1.1.4 to 1.1.7 `#437 <https://github.com/ansys/pyansys-math/pull/437>`_
- maint: bump pytest-cov from 5.0.0 to 6.0.0 `#440 <https://github.com/ansys/pyansys-math/pull/440>`_
- maint: bump numpy from 2.1.2 to 2.1.3 `#442 <https://github.com/ansys/pyansys-math/pull/442>`_
- maint: bump ansys-sphinx-theme from 1.1.7 to 1.2.1 `#445 <https://github.com/ansys/pyansys-math/pull/445>`_
- maint: bump jupyterlab from 4.2.5 to 4.3.1 `#446 <https://github.com/ansys/pyansys-math/pull/446>`_
- maint: bump ansys-sphinx-theme from 1.2.1 to 1.2.2 `#448 <https://github.com/ansys/pyansys-math/pull/448>`_
- maint: bump pytest-rerunfailures from 14.0 to 15.0 `#449 <https://github.com/ansys/pyansys-math/pull/449>`_
- maint: bump ansys-mapdl-reader from 0.54.1 to 0.54.2 `#450 <https://github.com/ansys/pyansys-math/pull/450>`_
- maint: bump pyvista[jupyter,trame] from 0.44.1 to 0.44.2 `#451 <https://github.com/ansys/pyansys-math/pull/451>`_, `#457 <https://github.com/ansys/pyansys-math/pull/457>`_
- maint: bump jupyterlab from 4.3.1 to 4.3.4 `#460 <https://github.com/ansys/pyansys-math/pull/460>`_
- maint: bump ansys-sphinx-theme from 1.2.2 to 1.2.6 `#462 <https://github.com/ansys/pyansys-math/pull/462>`_
- maint: bump numpy from 2.1.3 to 2.2.2 `#464 <https://github.com/ansys/pyansys-math/pull/464>`_
- maint: bump sphinx-autodoc-typehints from 2.5.0 to 3.0.1 `#465 <https://github.com/ansys/pyansys-math/pull/465>`_


Documentation
^^^^^^^^^^^^^

- chore: update CHANGELOG for v0.2.0 `#426 <https://github.com/ansys/pyansys-math/pull/426>`_


Maintenance
^^^^^^^^^^^

- maint: bump codecov/codecov-action from 4 to 5 in the actions group `#444 <https://github.com/ansys/pyansys-math/pull/444>`_

`0.2.0 <https://github.com/ansys/pyansys-math/releases/tag/v0.2.0>`_ - 2024-10-08
=================================================================================

Changed
^^^^^^^

- chore: update CHANGELOG for v0.1.5 `#328 <https://github.com/ansys/pyansys-math/pull/328>`_
- maint: adding `update-changelog` as a CICD dependency `#329 <https://github.com/ansys/pyansys-math/pull/329>`_
- [pre-commit.ci] pre-commit autoupdate `#351 <https://github.com/ansys/pyansys-math/pull/351>`_
- maint: implement `ansys/actions/check-vulnerabilities` in CICD `#355 <https://github.com/ansys/pyansys-math/pull/355>`_
- maint: bump docker/login-action from 3.1.0 to 3.2.0 in the actions group `#356 <https://github.com/ansys/pyansys-math/pull/356>`_
- maint: bump docker/login-action from 3.2.0 to 3.3.0 in the actions group `#388 <https://github.com/ansys/pyansys-math/pull/388>`_


Fixed
^^^^^

- fix: adding a waiting time for MAPDL service to start `#354 <https://github.com/ansys/pyansys-math/pull/354>`_


Dependencies
^^^^^^^^^^^^

- maint: bump pyvista from 0.43.5 to 0.43.6 `#331 <https://github.com/ansys/pyansys-math/pull/331>`_
- maint: bump pytest from 8.1.1 to 8.2.0 `#332 <https://github.com/ansys/pyansys-math/pull/332>`_
- maint: bump jupyterlab from 4.1.6 to 4.1.8 `#333 <https://github.com/ansys/pyansys-math/pull/333>`_
- maint: bump sphinx-gallery from 0.15.0 to 0.16.0 `#334 <https://github.com/ansys/pyansys-math/pull/334>`_
- maint: bump pyvista[jupyter,trame] from 0.43.5 to 0.43.6 `#335 <https://github.com/ansys/pyansys-math/pull/335>`_
- maint: bump pyvista from 0.43.6 to 0.43.7 `#337 <https://github.com/ansys/pyansys-math/pull/337>`_
- maint: bump pyvista[jupyter,trame] from 0.43.5 to 0.43.7 `#338 <https://github.com/ansys/pyansys-math/pull/338>`_
- maint: bump jupyterlab from 4.1.8 to 4.2.0 `#339 <https://github.com/ansys/pyansys-math/pull/339>`_
- maint: bump pytest from 8.2.0 to 8.2.1 `#341 <https://github.com/ansys/pyansys-math/pull/341>`_
- maint: bump pyvista from 0.43.7 to 0.43.8 `#342 <https://github.com/ansys/pyansys-math/pull/342>`_
- maint: bump ansys-sphinx-theme from 0.15.2 to 0.16.0 `#343 <https://github.com/ansys/pyansys-math/pull/343>`_
- maint: bump pyvista[jupyter,trame] from 0.43.7 to 0.43.8 `#344 <https://github.com/ansys/pyansys-math/pull/344>`_, `#357 <https://github.com/ansys/pyansys-math/pull/357>`_
- maint: bump jupyterlab from 4.2.0 to 4.2.1 `#346 <https://github.com/ansys/pyansys-math/pull/346>`_
- maint: bump sphinx-design from 0.5.0 to 0.6.0 `#347 <https://github.com/ansys/pyansys-math/pull/347>`_
- maint: bump pyansys-tools-report from 0.7.0 to 0.7.3 `#348 <https://github.com/ansys/pyansys-math/pull/348>`_
- maint: bump sphinx-notfound-page from 1.0.0 to 1.0.2 `#349 <https://github.com/ansys/pyansys-math/pull/349>`_
- maint: bump scipy from 1.13.0 to 1.13.1 `#350 <https://github.com/ansys/pyansys-math/pull/350>`_
- maint: bump trame from 3.6.0 to 3.6.2 `#358 <https://github.com/ansys/pyansys-math/pull/358>`_
- maint: bump ansys-sphinx-theme from 0.16.0 to 0.16.5 `#359 <https://github.com/ansys/pyansys-math/pull/359>`_
- maint: bump pytest from 8.2.1 to 8.2.2 `#360 <https://github.com/ansys/pyansys-math/pull/360>`_
- maint: bump pyvista[jupyter,trame] from 0.43.8 to 0.43.9 `#361 <https://github.com/ansys/pyansys-math/pull/361>`_, `#366 <https://github.com/ansys/pyansys-math/pull/366>`_
- maint: bump pyvista from 0.43.8 to 0.43.9 `#362 <https://github.com/ansys/pyansys-math/pull/362>`_
- maint: bump jupyterlab from 4.2.1 to 4.2.2 `#363 <https://github.com/ansys/pyansys-math/pull/363>`_
- maint: bump sphinx-autodoc-typehints from 2.1.0 to 2.1.1 `#364 <https://github.com/ansys/pyansys-math/pull/364>`_
- maint: bump numpy from 1.26.4 to 2.1.2 `#367 <https://github.com/ansys/pyansys-math/pull/367>`_
- maint: bump sphinx-autodoc-typehints from 2.1.1 to 2.2.2 `#369 <https://github.com/ansys/pyansys-math/pull/369>`_
- maint: bump pyvista[jupyter,trame] from 0.43.9 to 0.43.10 `#370 <https://github.com/ansys/pyansys-math/pull/370>`_
- maint: bump pyvista from 0.43.9 to 0.43.10 `#371 <https://github.com/ansys/pyansys-math/pull/371>`_
- maint: bump ansys-sphinx-theme from 0.16.5 to 0.16.6 `#372 <https://github.com/ansys/pyansys-math/pull/372>`_
- maint: bump jupyterlab from 4.2.2 to 4.2.3 `#374 <https://github.com/ansys/pyansys-math/pull/374>`_
- maint: bump vtk from 9.3.0 to 9.3.1 `#375 <https://github.com/ansys/pyansys-math/pull/375>`_
- maint: bump trame from 3.6.2 to 3.6.3 `#376 <https://github.com/ansys/pyansys-math/pull/376>`_
- maint: bump scipy from 1.13.1 to 1.14.0 `#379 <https://github.com/ansys/pyansys-math/pull/379>`_
- maint: bump pyvista from 0.43.10 to 0.44.0 `#380 <https://github.com/ansys/pyansys-math/pull/380>`_
- maint: bump ansys-mapdl-core from 0.68.1 to 0.68.4 `#383 <https://github.com/ansys/pyansys-math/pull/383>`_
- maint: bump pytest from 8.2.2 to 8.3.1 `#384 <https://github.com/ansys/pyansys-math/pull/384>`_
- maint: bump sphinx-gallery from 0.16.0 to 0.17.0 `#385 <https://github.com/ansys/pyansys-math/pull/385>`_
- maint: bump sphinx-autodoc-typehints from 2.2.2 to 2.2.3 `#386 <https://github.com/ansys/pyansys-math/pull/386>`_
- maint: bump pyvista from 0.44.0 to 0.44.1 `#387 <https://github.com/ansys/pyansys-math/pull/387>`_
- maint: bump pytest from 8.3.1 to 8.3.2 `#390 <https://github.com/ansys/pyansys-math/pull/390>`_
- maint: bump sphinx-notfound-page from 1.0.2 to 1.0.4 `#391 <https://github.com/ansys/pyansys-math/pull/391>`_
- maint: bump pyvista[jupyter,trame] from 0.44.0 to 0.44.1 `#393 <https://github.com/ansys/pyansys-math/pull/393>`_
- maint: bump jupyterlab from 4.2.3 to 4.2.4 `#396 <https://github.com/ansys/pyansys-math/pull/396>`_
- maint: bump numpydoc from 1.7.0 to 1.8.0 `#397 <https://github.com/ansys/pyansys-math/pull/397>`_
- maint: bump sphinx-gallery from 0.17.0 to 0.17.1 `#398 <https://github.com/ansys/pyansys-math/pull/398>`_
- maint: bump pyansys-tools-report from 0.7.3 to 0.8.0 `#400 <https://github.com/ansys/pyansys-math/pull/400>`_
- maint: bump ansys-sphinx-theme from 1.0.3 to 1.0.5 `#401 <https://github.com/ansys/pyansys-math/pull/401>`_
- maint: bump ansys-sphinx-theme from 1.0.5 to 1.0.7 `#402 <https://github.com/ansys/pyansys-math/pull/402>`_
- maint: bump scipy from 1.14.0 to 1.14.1 `#404 <https://github.com/ansys/pyansys-math/pull/404>`_
- maint: bump sphinx-autodoc-typehints from 2.2.3 to 2.3.0 `#406 <https://github.com/ansys/pyansys-math/pull/406>`_
- maint: bump jupyterlab from 4.2.4 to 4.2.5 `#407 <https://github.com/ansys/pyansys-math/pull/407>`_
- maint: bump sphinx-autobuild from 2024.4.16 to 2024.9.3 `#408 <https://github.com/ansys/pyansys-math/pull/408>`_
- maint: bump pytest from 8.3.2 to 8.3.3 `#409 <https://github.com/ansys/pyansys-math/pull/409>`_
- maint: bump trame from 3.6.3 to 3.6.5 `#410 <https://github.com/ansys/pyansys-math/pull/410>`_
- maint: bump ansys-sphinx-theme from 1.0.7 to 1.0.9 `#411 <https://github.com/ansys/pyansys-math/pull/411>`_
- maint: bump ansys-mapdl-reader from 0.53.0 to 0.54.1 `#412 <https://github.com/ansys/pyansys-math/pull/412>`_
- maint: bump ansys-sphinx-theme from 1.0.9 to 1.0.11 `#413 <https://github.com/ansys/pyansys-math/pull/413>`_
- maint: bump sphinx-autodoc-typehints from 2.3.0 to 2.4.4 `#414 <https://github.com/ansys/pyansys-math/pull/414>`_
- maint: bump sphinx-autobuild from 2024.9.3 to 2024.9.19 `#415 <https://github.com/ansys/pyansys-math/pull/415>`_
- maint: bump sphinx-autobuild from 2024.9.19 to 2024.10.3 `#421 <https://github.com/ansys/pyansys-math/pull/421>`_
- maint: bump ansys-sphinx-theme from 1.0.11 to 1.1.2 `#422 <https://github.com/ansys/pyansys-math/pull/422>`_


Miscellaneous
^^^^^^^^^^^^^

- [pre-commit.ci] pre-commit autoupdate `#336 <https://github.com/ansys/pyansys-math/pull/336>`_, `#340 <https://github.com/ansys/pyansys-math/pull/340>`_, `#345 <https://github.com/ansys/pyansys-math/pull/345>`_, `#365 <https://github.com/ansys/pyansys-math/pull/365>`_, `#368 <https://github.com/ansys/pyansys-math/pull/368>`_, `#373 <https://github.com/ansys/pyansys-math/pull/373>`_, `#377 <https://github.com/ansys/pyansys-math/pull/377>`_, `#382 <https://github.com/ansys/pyansys-math/pull/382>`_, `#389 <https://github.com/ansys/pyansys-math/pull/389>`_, `#394 <https://github.com/ansys/pyansys-math/pull/394>`_, `#399 <https://github.com/ansys/pyansys-math/pull/399>`_, `#405 <https://github.com/ansys/pyansys-math/pull/405>`_, `#416 <https://github.com/ansys/pyansys-math/pull/416>`_, `#424 <https://github.com/ansys/pyansys-math/pull/424>`_


Documentation
^^^^^^^^^^^^^

- maint: bump sphinx from 7.3.7 to 8.0.2 `#392 <https://github.com/ansys/pyansys-math/pull/392>`_


Maintenance
^^^^^^^^^^^

- maint: bump ansys/actions from 6 to 7 in the actions group `#395 <https://github.com/ansys/pyansys-math/pull/395>`_
- ci: updating supported Python versions `#420 <https://github.com/ansys/pyansys-math/pull/420>`_
- maint: bump ansys/actions from 7 to 8 in the actions group `#423 <https://github.com/ansys/pyansys-math/pull/423>`_
- maint: updating ``CONTRIBUTORS.md`` and ``AUTHORS`` files `#425 <https://github.com/ansys/pyansys-math/pull/425>`_

`0.1.5 <https://github.com/ansys/pyansys-math/releases/tag/v0.1.5>`_ - 2024-04-22
=================================================================================

Changed
^^^^^^^

- chore: update CHANGELOG for v0.1.4 `#325 <https://github.com/ansys/pyansys-math/pull/325>`_
- ci: establish stage dependencies for release `#327 <https://github.com/ansys/pyansys-math/pull/327>`_


Miscellaneous
^^^^^^^^^^^^^

- docs: title level for release notes `#326 <https://github.com/ansys/pyansys-math/pull/326>`_

`0.1.4 <https://github.com/ansys/pyansys-math/releases/tag/v0.1.4>`_ - 2024-04-22
=================================================================================

Added
^^^^^

- feat: implementing `ansys/actions/doc-changelog` `#316 <https://github.com/ansys/pyansys-math/pull/316>`_


Changed
^^^^^^^

- doc: adding release notes in documentation `#324 <https://github.com/ansys/pyansys-math/pull/324>`_


Fixed
^^^^^

- fix: updating CICD (Vale, MAPDL image) `#322 <https://github.com/ansys/pyansys-math/pull/322>`_
- fix: removing `md` Vale checks `#323 <https://github.com/ansys/pyansys-math/pull/323>`_


Dependencies
^^^^^^^^^^^^

- maint: bump sphinx-autodoc-typehints from 2.0.0 to 2.1.0 `#317 <https://github.com/ansys/pyansys-math/pull/317>`_
- maint: bump ansys-sphinx-theme from 0.15.0 to 0.15.2 `#318 <https://github.com/ansys/pyansys-math/pull/318>`_
- maint: bump sphinx-autobuild from 2024.4.13 to 2024.4.16 `#319 <https://github.com/ansys/pyansys-math/pull/319>`_
- maint: bump sphinx from 7.2.6 to 7.3.7 `#320 <https://github.com/ansys/pyansys-math/pull/320>`_
- maint: bump jupyterlab from 4.1.5 to 4.1.6 `#321 <https://github.com/ansys/pyansys-math/pull/321>`_

.. vale on
