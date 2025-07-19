class Dataset:
    """Parent class."""

    def __init__(self, path: str) -> None:
        print("Initializing parent Dataset...")
        self.path = path

    def load(self) -> None:
        print(f"Loading {self.path}...")
        # load data...

    def clean(self) -> None:
        raise NotImplementedError

    def save(self, path: str) -> None:
        print(f"Saving {path}...")
        # save data...


class FooDataset(Dataset):
    """Child class."""

    def __init__(self, path: str) -> None:
        super().__init__(path)
        print("Initializing child FooDataset...")

    def clean(self) -> None:
        print("Cleaning foo...")
        # clean data...


class BarDataset(Dataset):
    """Child class."""

    def __init__(self, path: str) -> None:
        super().__init__(path)
        print("Initializing chid BarDataset...")

    def clean(self) -> None:
        print("Cleaning bar...")


if __name__ == "__main__":
    foo_dataset = FooDataset("/foo")
    bar_dataset = BarDataset("/bar")

    foo_dataset.load()
    foo_dataset.clean()
    foo_dataset.save("/foo.clean")

    bar_dataset.load()
    bar_dataset.clean()
    bar_dataset.save("/bar.clean")
