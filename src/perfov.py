from datetime import datetime


class Perfov:
    def __init__(self) -> None:
        self.start_time = datetime.now()
        self.last_checkpoint = None

    def start(self):
        self.start_time = datetime.now()

    def checkpoint(self, label):
        start_time = (
            self.last_checkpoint
            if self.last_checkpoint is not None
            else self.start_time
        )
        now = datetime.now()
        duration = now - start_time
        self.last_checkpoint = now
        Perfov._print_duration(duration, label)

    def finish(self):
        duration = datetime.now() - self.start_time
        Perfov._print_duration(duration, label="All")

    def _print_duration(duration, label=None):
        print_string = f"{label} process took {duration}"
        print(print_string)
