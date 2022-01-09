class Watchdog:

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
        my_event_handler.on_created = on_created
        my_event_handler.on_modified = on_modified
        return my_event_handler

    def setObserver(self):
        my_observer = Observer()
        my_observer.schedule(self.eventHandlerConfig(), self.path, recursive=self.goRecursive)

    # watch for "create" events in file path
    @staticmethod
    def on_created(event):
        if event:
            return True

    # watch for "modified" events in file path and write event to txt file in py path
    @staticmethod
    def on_modified(event):
        # t = str(event.src_path)
        getEvent = str(event)
        fileName = "list.txt"
        with open(fileName, "w+") as file:
            file.write(getEvent)
        return fileName