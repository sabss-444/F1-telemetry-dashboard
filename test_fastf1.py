import fastf1
session = fastf1.get_session(2025, "British Grand Prix", "Q")
session.load()
fastest_lap = session.laps.pick_fastest()
telemetry = fastest_lap.get_telemetry()
print("Driver:", fastest_lap["Driver"])
print("Lap Time:", fastest_lap["LapTime"])
print("Number of telemetry Points:", len(telemetry))
print(telemetry.head())

