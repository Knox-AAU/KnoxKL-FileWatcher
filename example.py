from watcher.FileWatcher import FileWatcher
from watchdog.events import FileSystemEventHandler
from watcher import process_existing

class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'modified':
            if event.src_path.endswith('.json'):
                print('Received file', event.src_path)

def processor_callback(path: str):
    print(path)

if __name__ == "__main__":
    process_existing('./in/', processor_callback)
    fw = FileWatcher('./in/')
    fw.run(Handler())
    pass