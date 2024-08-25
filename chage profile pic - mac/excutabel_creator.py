# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_submodules
from PyInstaller import __main__ as pyi_main

args = [
    '--onefile',
       '--add-data=main.py:.',  # Include the_gui.py in the root
       '--add-data=login_handeling.py:.',  # Include captcha_solver_selen.py in the root
    '--hidden-import', ','.join(collect_submodules('.')),  # Collect hidden imports
    # '--noconsole',  # Set console to False
    '--name=linkedin profile pic changer',  # Set the app name to YourAppName
    'main.py'  # Set the main script to daily_checker.py
]


pyi_main.run(args)
