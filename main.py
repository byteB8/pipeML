from abc import ABC, abstractmethod


class Dataset(ABC):
    @abstractmethod
    def load(self) -> None:
        pass

    @abstractmethod
    def clean(self) -> None:
        pass

    @abstractmethod
    def save(self, path: str) -> None:
        pass


class FooDataset(Dataset):
    def __init__(self, path: str) -> None:
        print("Initializing child FooDataset...")
        self.path = path

    def load(self) -> None:
        print(f"Loading {self.path}...")
        # load data...

    def clean(self) -> None:
        print("Cleaning foo...")
        # clean data...

    def save(self, path: str) -> None:
        print(f"Saving {path}...")
        # save data...


class BarDataset(Dataset):
    def __init__(self, path: str) -> None:
        print("Initializing child BarDataset...")
        self.path = path

    def load(self) -> None:
        print(f"Loading {self.path}...")
        # load data...

    def save(self, path: str) -> None:
        print(f"Saving {path}...")
        # save data...


if __name__ == "__main__":
    foo_dataset = FooDataset("/foo")

    foo_dataset.load()
    foo_dataset.clean()
    foo_dataset.save("/foo.clean")
