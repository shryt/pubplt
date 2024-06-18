from matplotlib import pyplot as plt
import japanize_matplotlib  # noqa: F401


class SimpleFigure:
    def __init__(
        self, filename=None, title=None, xlabel=None, ylabel=None
    ):
        self.filename = filename
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
        if self.filename is not None:
            self.fig.savefig(self.filename)
