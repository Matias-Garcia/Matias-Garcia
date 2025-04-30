import requests
import pandas as pd

def fetch_nba_scores_json():
    url = "https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard"
    resp = requests.get(url)
    resp.raise_for_status()
    data = resp.json()

    games = []
    for evt in data["events"]:
        comp = evt["competitions"][0]
        status = comp["status"]["type"]["shortDetail"]
        away = comp["competitors"][0]
        home = comp["competitors"][1]
        games.append({
            "away_team": away["team"]["displayName"],
            "away_score": int(away["score"]),
            "home_team": home["team"]["displayName"],
            "home_score": int(home["score"]),
            "status": status
        })

    return pd.DataFrame(games)

if __name__=="__main__":
    print(fetch_nba_scores_json())
