import sys
import time

class DynamicProgressBar:
    def __init__(self, total, prefix='Progress:', suffix='Complete', decimals=1, length=50, fill='█', print_end="\r"):
        """
        Create a dynamic progress bar for tracking task completion.
        
        :param total: Total iterations expected
        :param prefix: Prefix string before progress bar
        :param suffix: Suffix string after progress bar
        :param decimals: Number of decimal places for percentage
        :param length: Character length of progress bar
        :param fill: Bar fill character
        :param print_end: End character (default suppresses multiple lines)
        """
        self.total = total
        self.prefix = prefix
        self.suffix = suffix
        self.decimals = decimals
        self.length = length
        self.fill = fill
        self.print_end = print_end
        self.start_time = time.time()

    def update(self, iteration):
        """
        Update the progress bar.
        
        :param iteration: Current iteration
        """
        # Calculate percentages
        percent = ("{0:." + str(self.decimals) + "f}").format(100 * (iteration / float(self.total)))
        
        # Calculate filled length
        filled_length = int(self.length * iteration // self.total)
        
        # Create bar string
        bar = self.fill * filled_length + '-' * (self.length - filled_length)
        
        # Calculate elapsed time and estimated remaining time
        elapsed = time.time() - self.start_time
        if iteration > 0:
            est_total_time = elapsed * (self.total / iteration)
            remaining = max(0, est_total_time - elapsed)
        else:
            remaining = 0
        
        # Construct output string
        output = f'\r{self.prefix} |{bar}| {percent}% {self.suffix} '
        output += f'(Elapsed: {elapsed:.2f}s, Remaining: {remaining:.2f}s)'
        
        # Print and flush to ensure immediate update
        sys.stdout.write(output)
        sys.stdout.flush()
        
        # Print newline when complete
        if iteration == self.total:
            print()

def log_with_progress(iterable, prefix='Progress:', **kwargs):
    """
    Decorator/generator to add progress bar to any iterable.
    
    :param iterable: Iterable to track
    :param prefix: Prefix for progress bar
    :param kwargs: Additional arguments for DynamicProgressBar
    :return: Yields items from iterable with progress tracking
    """
    total = len(iterable)
    progress_bar = DynamicProgressBar(total, prefix=prefix, **kwargs)
    
    for i, item in enumerate(iterable, 1):
        progress_bar.update(i)
        yield item