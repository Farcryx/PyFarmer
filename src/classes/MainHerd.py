from src.scripts.setup_game import INITIAL_HERD


class MainHerd:
    def __init__(self):
        self.herd = INITIAL_HERD
        self.herd_size = sum(self.herd.values())

    def __str__(self):
        return f"MainHerd: {self.herd_size}, {self.herd}"

    def __getitem__(self, key):
        return self.herd[key]

    def __setitem__(self, key, value):
        self.herd[key] = value

    def __len__(self):
        return self.herd_size

    def reset(self):
        self.herd = INITIAL_HERD
        self.herd_size = sum(self.herd.values())
        return self.herd_size

    def remove_animal(self, animal_type: str, quantity: int = 1) -> bool:
        if animal_type in self.herd and self.herd[animal_type] >= quantity:
            self.herd[animal_type] -= quantity
            self.herd_size -= quantity
            return True
        return False

    def add_animal(self, animal_type: str, quantity: int = 1) -> bool:
        if animal_type in self.herd:
            self.herd[animal_type] += quantity
            self.herd_size += quantity
            return True
        return False

    def get_formatted_herd(self) -> str:
        return ", ".join(f"{k}: {v}" for k, v in self.herd.items())