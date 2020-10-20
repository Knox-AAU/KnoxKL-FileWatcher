from __future__ import annotations

import time

from watchdog.observers import Observer
import os
from typing import Callable

def process_existing(path: str, callback: Callable[[str], None]) -> None:
    """
    Input:
        path: str - The input directory path, that will be processed

    This method will look through the input directory, and determine whether a file has been processed previously
    When the file has been processed, it will be moved to the output directory.
    """


    if (path == 'DOES NOT EXIST' or not os.path.exists(path)):
        raise FileNotFoundError('Watcher unable to run as no directory was provided or it did not exist', path)

    print(f'Checking for existing files in \'{path}\'...')
    paths = [os.path.join(path, fn) for fn in next(os.walk(path))[2]]
    if len(paths) == 0:
        print('No files were created between sessions')
        return

    for path in paths:
        callback(path)
