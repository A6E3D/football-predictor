import csv


goals = { }
with open("practice/sample.csv", newline="") as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        goals[row["HomeTeam"]] = goals.get(row["HomeTeam"], 0) + int(row["FTHG"])

        goals[row["AwayTeam"]] = goals.get(row["AwayTeam"], 0) + int(row["FTAG"])
    print(goals)