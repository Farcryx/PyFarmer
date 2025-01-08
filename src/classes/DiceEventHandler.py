class DiceEventHandler:
    def __init__(self, main_herd: dict[str, int], player_animals: dict[str, int], player_dogs: dict[str, int]):
        self.main_herd = main_herd
        self.player_animals = player_animals
        self.player_dogs = player_dogs
        self.last_roll = ("", "")
    
    def handle_roll(self, dice1_result: str, dice2_result: str) -> tuple[bool, str]:
        """Obsługuje wynik rzutu kostkami i zwraca (sukces, wiadomość)"""
        self.last_roll = (dice1_result, dice2_result)
        
        # Sprawdź zdarzenia specjalne
        if "wilk" in (dice1_result, dice2_result):
            return self._handle_wolf()
        if "lis" in (dice1_result, dice2_result):
            return self._handle_fox()
            
        # Zlicz zwierzęta z rzutu
        animals_to_add = self._count_animals_from_roll()
        return self._update_player_herd(animals_to_add)
    
    def _handle_wolf(self) -> tuple[bool, str]:
        """Obsługuje atak wilka"""
        if self.player_dogs.get("big_dog", 0) > 0:
            return True, "Duży pies obronił stado przed wilkiem!"
        
        # Utrata wszystkich zwierząt oprócz koni
        lost_animals = {k: v for k, v in self.player_animals.items() if k != "koń"}
        self.player_animals.update({k: 0 for k in lost_animals.keys()})
        return False, "Wilk pożarł wszystkie zwierzęta oprócz koni!"
    
    def _handle_fox(self) -> tuple[bool, str]:
        """Obsługuje atak lisa"""
        if self.player_dogs.get("small_dog", 0) > 0:
            return True, "Mały pies obronił króliki przed lisem!"
        
        # Utrata wszystkich królików
        lost_rabbits = self.player_animals.get("królik", 0)
        self.player_animals["królik"] = 0
        return False, f"Lis pożarł wszystkie króliki! ({lost_rabbits})"
    
    def _count_animals_from_roll(self) -> dict[str, int]:
        """Zlicza zwierzęta z rzutu kostkami"""
        animals = {}
        for result in self.last_roll:
            if result not in ("wilk", "lis"):
                animals[result] = animals.get(result, 0) + 1
        return animals
    
    def _update_player_herd(self, new_animals: dict[str, int]) -> tuple[bool, str]:
        """Aktualizuje stado gracza o nowe zwierzęta"""
        message = []
        for animal, count in new_animals.items():
            available = self.main_herd.get(animal, 0)
            if available >= count:
                self.player_animals[animal] = self.player_animals.get(animal, 0) + count
                self.main_herd[animal] -= count
                message.append(f"+{count} {animal}")
                
        return True, ", ".join(message) if message else "Brak nowych zwierząt"