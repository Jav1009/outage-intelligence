SEED = 42  # same seed = same "random" data every run

# Fictional service zones (centres are made up, not real JPS zones)
ZONES = {
    "Zone North": {"lat": 18.05, "lon": -76.80, "hospital": True},
    "Zone East":  {"lat": 18.00, "lon": -76.74, "hospital": False},
    "Zone West":  {"lat": 17.97, "lon": -76.92, "hospital": False},
    "Zone South": {"lat": 17.93, "lon": -76.85, "hospital": True},
}

DESCRIPTIONS = [
    "No power since evening",
    "Lights flickering then off",
    "Loud bang then power lost",
    "Sparks seen near pole",
    "Line down across road",
    "Whole street is dark",
]