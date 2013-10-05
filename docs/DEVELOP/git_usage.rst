###################
First Course in Git
###################

Learn Git
=========

Here are some resources learning git

- Learning Git interactively http://try.github.io/

- Offical Guide http://git-scm.com/documentation

- Using Git on pandas Wiki https://github.com/pydata/pandas/wiki/Using-Git

Search git tutorial you will find out more resources

Write Commit Log
================

See http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html for format guide.

Each commit should be an atomic change and try to make it small. For example, if we want to change the API calling from ``nb.io.read_sam_file`` to ``nb.io.read_sam``, all these changes should be made in the same commit. Keeping them in two more commits may confuse others. Otherwise one should note in an independent commit like::

    Fix API change again

    Original API change should be in commit xxxxxx.

So if any part of the commit break, it is easier to recover (or revert) the broken part and leave most change intact.


Git Branching
=============

There are two main branches:

- ``master``: for stable code release, **never** code in this branch!
- ``develop``: for development

For normal user, use code on ``master``; for developer, use code on ``develop``.

All code should be first merged to ``develop``, and then merged to ``master`` for every version jump.

For new features or large development, check out a new branch from ``develop``. For example, code for SAM file support in branch ``sam_file``.
