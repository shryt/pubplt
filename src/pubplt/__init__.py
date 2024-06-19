import os
from matplotlib import pyplot as plt
import japanize_matplotlib  # noqa: F401


class SimpleFigure:
    def __init__(
        self, file_path=None, title=None, xlabel=None, ylabel=None
    ):
        self.file_path = file_path
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel

    def __enter__(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        if self.xlabel is not None:
            self.ax.set_xlabel(self.xlabel)
        if self.ylabel is not None:
            self.ax.set_ylabel(self.ylabel)
        if self.title is not None:
            self.ax.set_title(self.title)
        return self.ax

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file_path is not None:
            os.makedirs(
                os.path.dirname(self.file_path), exist_ok=True
            )
            self.fig.savefig(self.file_path)
        plt.close(self.fig)
