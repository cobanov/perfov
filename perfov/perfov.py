from datetime import datetime


class Perfov:
    def __init__(self) -> None:
        self.start_time = datetime.now()
        self.last_checkpoint = None

    def start(self):
        """Mark the start time of the performance measurement."""
        self.start_time = datetime.now()

    def checkpoint(self, label):
        """Create a checkpoint for a specific process."""
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
        """Print the total elapsed time for all processes."""
        duration = datetime.now() - self.start_time
        Perfov._print_duration(duration, label="All")

    def _print_duration(duration, label=None):
        print_string = f"{label} process took {duration:.2f} seconds"
        print(print_string)
