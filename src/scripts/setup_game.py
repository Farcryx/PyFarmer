# Game constants
INITIAL_HERD = {
    "rabbit": 60,
    "sheep": 24,
    "pig": 20,
    "cow": 12,
    "horse": 6
}

EXCHANGE_RATES = {
    "rabbit": {"sheep": 6, "pig": 12, "cow": 36, "horse": 72},
    "sheep": {"rabbit": 1 / 6, "pig": 2, "cow": 6, "horse": 12},
    "pig": {"rabbit": 1 / 12, "sheep": 1 / 2, "cow": 3, "horse": 6},
    "cow": {"rabbit": 1 / 36, "sheep": 1 / 6, "pig": 1 / 3, "horse": 2},
    "horse": {"rabbit": 1 / 72, "sheep": 1 / 12, "pig": 1 / 6, "cow": 1 / 2}
}

DICE1_SIDES = ["rabbit", "rabbit", "rabbit", "rabbit", "rabbit", "rabbit", "rabbit", "rabbit", "sheep", "pig",
               "cow", "fox"]
DICE2_SIDES = ["rabbit", "rabbit", "rabbit", "rabbit", "rabbit", "rabbit", "rabbit", "rabbit", "sheep", "pig",
               "horse", "wolf"]
