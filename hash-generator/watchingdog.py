from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


class Watchdog:
    eventCheck = False

    def __init__(self, path, patterns=["*"], ignore_patterns=None, ignore_directories=False, case_sensitive=True,
                 go_recursively=True):
        self.path = path
        self.patterns = patterns
        self.ignorePatterns = ignore_patterns
        self.ignoreDirectories = ignore_directories
        self.caseSensitive = case_sensitive
        self.goRecursive = go_recursively

    def eventHandlerConfig(self):
        # Event Handler Configurations
        my_event_handler = PatternMatchingEventHandler(self.patterns, self.ignorePatterns, self.ignoreDirectories,
                                                       self.caseSensitive)
        my_event_handler.on_created = self.on_created
        my_event_handler.on_modified = self.on_modified
        return my_event_handler

    # watch for "create" events in file path
    @staticmethod
    def on_created(event):
        if event:
            Watchdog.eventCheck = True

    # watch for "modified" events in file path and write event to txt file in py path
    @staticmethod
    def on_modified(event):
        getEvent = str(event.src_path)
        fileName = "list.txt"
        with open(fileName, "w+") as file:
            file.write(getEvent)

    def startObserver(self):

        try:
            my_observer = Observer()
            my_observer.start()
            my_observer.schedule(self.eventHandlerConfig(), self.path, recursive=self.goRecursive)
        except FileNotFoundError as e:
            return None
