from abc import ABC, abstractmethod


class Dataset(ABC):
    __name: str

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value) -> None:
        self.__name = value

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
        self.name = "FooDataset"
        self.path = path

    def load(self) -> None:
        print(f"Loading {self.path}...")
        # load data...

    def clean(self) -> None:
        print(f"Cleaning {self.name}...")
        # clean data...

    def save(self, path: str) -> None:
        print(f"Saving {path}...")
        # save data...


if __name__ == "__main__":
    foo_dataset = FooDataset("/foo")

    print(foo_dataset.name)

    foo_dataset.load()
    foo_dataset.clean()
    foo_dataset.save("/foo.clean")
