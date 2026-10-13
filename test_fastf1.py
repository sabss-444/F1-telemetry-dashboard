import fastf1
session = fastf1.get_session(2025, "British Grand Prix", "Q")
session.load()
print(session.results [
    ["Abbreviation", "Position", "Points", "Status"]
])
print("Number of Laps", len(session.laps))
print(session.laps.head())
