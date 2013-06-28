sinarngo.service Installation
-----------------------------

To install sinarngo.service using zc.buildout and the plone.recipe.zope2instance
recipe to manage your project, you can do this:

* Add ``sinarngo.service`` to the list of eggs to install, e.g.:

    [buildout]
    ...
    eggs =
        ...
        sinarngo.service

* Re-run buildout, e.g. with:

    $ ./bin/buildout

