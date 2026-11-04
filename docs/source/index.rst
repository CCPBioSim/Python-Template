:html_theme.sidebar_secondary.remove:

CCPBioSim-Python-Template
=========================

.. Banner for the home page. Add your logos to _static/logos/ and set
   :logo-light: (dark text, for light mode) and :logo-dark: (white text, for
   dark mode). See https://ccpbiosim-sphinx-theme.readthedocs.io/

.. ccpbiosim-hero::
   :tagline: CCPBioSim-Python-Template
   :button: reference/example_package/index | API reference
   :github: CCPBioSim/Python-Template

   Short description of your package

Add an introduction to your package here. See the
`reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
documentation for details on writing pages.

Quick start
-----------

.. tab-set::

   .. tab-item:: pip

      .. code-block:: bash

         pip install example_package

   .. tab-item:: Conda

      .. code-block:: bash

         conda install -c conda-forge -c ccpbiosim example_package

Explore the documentation
-------------------------

.. Add a card for each section of your documentation.

.. grid:: 1 2 2 2
   :gutter: 3

   .. grid-item-card:: 📖 API Reference
      :link: reference/example_package/index
      :link-type: doc

      Reference for the example_package package.

   .. grid-item-card:: 💻 Source Code
      :link: https://github.com/CCPBioSim/Python-Template

      The repository on GitHub.

.. toctree::
   :maxdepth: 2
   :hidden:

   API Reference <reference/example_package/index>
