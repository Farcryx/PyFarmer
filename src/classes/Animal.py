class Animal:
    def __init__(self, name: str, value: int, quantity: int, animal_type: str):
        self.name = name
        self.value = value
        self.quantity = quantity
        self.is_protected = False
        self.type = animal_type

    def update_quantity(self, amount: int) -> bool:
        """Update animal quantity. Returns True if successful."""
        if self.quantity + amount >= 0:
            self.quantity += amount
            return True
        return False

    def set_protection(self, status: bool):
        """Set protection status for animal."""
        self.is_protected = status

    def can_exchange_for(self, target_animal: 'Animal') -> bool:
        """Check if this animal can be exchanged for target animal."""
        return self.value * self.quantity >= target_animal.value

    def exchange_to(self, target_animal: 'Animal', quantity: int) -> bool:
        """Convert this animal to target animal type."""
        required_value = target_animal.value * quantity
        if self.value * self.quantity >= required_value:
            self.quantity -= required_value // self.value
            return True
        return False

    def get_total_value(self) -> int:
        """Get total value of all animals of this type."""
        return self.value * self.quantity

    def __str__(self) -> str:
        """String representation of the animal."""
        protection = " (Protected)" if self.is_protected else ""
        return f"{self.name}: {self.quantity}{protection}"

    def __repr__(self) -> str:
        """Detailed string representation of the animal."""
        return f"Animal(name='{self.name}', value={self.value}, quantity={self.quantity}, type='{self.type}')"