from __future__ import annotations

import time

from watchdog.observers import Observer
from os import path

class FileWatcher:
    """
    Class used to watch a directory for file changes
    The class will call the FileSystem handler
    """
    __watch_dir__: str = "DOES NOT EXIST"

    def __init__(self, path: str):
        """
        Input:
            path: str - The directory to watch

        Constructor for the file watcher
        """
        self.observer = Observer()
        self.__watch_dir__ = path

    def run(self, handler):
        """
        Input: 
            handler: Handler - The event handler to handle directory changes
        
        Runnable method that starts the watcher.
        """

        assert self.__watch_dir__ != "DOES NOT EXIST"
        assert path.exists(self.__watch_dir__)

        self.handler = handler

        print(f'Watching directory \'{self.__watch_dir__}\' for new publication files')

        self.observer.schedule(self.handler, self.__watch_dir__, recursive=True)
        self.observer.start()
        self.isRunning = True
        try:
            while self.observer.isAlive():
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
            print("Watcher stopped successfully")
        except:
            self.observer.stop()
            print("Watcher stopped unexpectedly")

        self.observer.join()

    def stop(self):
        """
        Stops the watcher
        """
        self.observer.stop()
        print('Watcher stopped successfully')
        self.observer.join()