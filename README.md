# Environment
Repository to keep all useful notes in regards to environment setup that I work with.

# jupyter Notebooks:

https://www.svds.com/jupyter-notebook-best-practices-for-data-science/
https://towardsdatascience.com/version-control-for-jupyter-notebook-3e6cef13392d

using links above add this to ~/.jupyter/jupyter_notebook_config.py:

import os
from subprocess import check_call

def post_save(model, os_path, contents_manager):
    """post-save hook for converting notebooks to .py scripts"""
    if model['type'] != 'notebook':
        return # only do this for notebooks
    d, fname = os.path.split(os_path)
    check_call(['jupyter', 'nbconvert', '--to', 'script', fname], cwd=d)
    # may want to not save html file
    check_call(['jupyter', 'nbconvert', '--to', 'html', fname], cwd=d)

c.FileContentsManager.post_save_hook = post_save

so your sheets are saved in multiple files for easy use with git
