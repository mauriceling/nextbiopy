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

See http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html.

Git Branching
=============

There are two main branches:

- ``master``: for stable code release
- ``develop``: for development

For normal user, use code on ``master``; for developer, use code on ``develop``.

All code should be first merged to ``develop``, and then merged to ``master`` for every version jump.

For new features or large development, check out a new branch from ``develop``. For example, code for SAM file support in branch ``sam_file``.
