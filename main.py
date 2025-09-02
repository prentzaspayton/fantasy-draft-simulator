def banner(title, ch="="):
    print("\n" + ch * 60)
    print(title.center(60))
    print(ch * 60)

def subhead(title, ch="-"):
    print("\n" + ch * 60)
    print(f"{title}")
    print(ch * 60)

def fmt_player_row(p, idx=None):
    # formats like: "0  Justin Jefferson           WR   325"
    left = f"{idx:<2} " if idx is not None else ""
    name = f"{p['name']:<25}"
    pos  = f"{p['pos']:^3}"
    proj = f"{int(p['proj']):>4}"
    return f"{left}{name} {pos} {proj}"

def print_options_table(players, show_index=True, title=None):
    if title:
        subhead(title)
    header = ("#  " if show_index else "") + f"{'Player':<25} {'POS':^3} {'Proj':>4}"
    print(header)
    print("-" * len(header))
    for i, p in enumerate(players):
        print(fmt_player_row(p, i if show_index else None))

# Fantasy-Draft
banner("Fantasy Football Draft")

# Each Participant Can only Draft 1 qb, 2 rb, 2, wr, 1 te, 1 k

ROSTER_LIMITS = {
    "QB": 1,
    "RB": 2,
    "WR": 2,
    "TE": 1,
    "K": 1,
    "FLEX": 1, # RB/WR/TE can go here
}
# Player Info, Players by Position, 

# Ranked by Amount of Points Projected (proj)

# QB: 10, RB: 20, WR: 20, TE: 10, K: 8

players = {
    "QB": [
        {"name": "Patrick Mahomes", "proj": 325},
        {"name": "Josh Allen", "proj": 368},
        {"name": "Lamar Jackson", "proj": 364},
        {"name": "Jayden Daniels", "proj": 372},
        {"name": "Jalen Hurts", "proj" : 366},
        {"name": "Joe Burrow", "proj": 331},
        {"name": "Baker Mayfield", "proj": 311},
        {"name": "Bo Nix", "proj": 302},
        {"name": "Kyler Murray", "proj": 307},
        {"name": "Brock Purdy", "proj": 306}
    ],
    "RB" : [
        {"name": "Christian McCaffrey", "proj": 318},
        {"name": "Bijan Robinson", "proj": 336},
        {"name": "Saquon Barkley", "proj": 326},
        {"name": "Jahmyr Gibbs", "proj": 317},
        {"name": "Ashton Jeanty", "proj": 300},
        {"name": "De'Von Achane", "proj": 307},
        {"name": "Jonathan Taylor", "proj": 289},
        {"name": "Josh Jacobs", "proj": 283},
        {"name": "Derrick Henry", "proj": 282},
        {"name": "Bucky Irving", "proj": 283},
        {"name": "Chase Brown", "proj": 281},
        {"name": "Kyren Williams", "proj": 279},
        {"name": "James Cook", "proj": 270},
        {"name": "Omarion Hampton", "proj": 259},
        {"name": "Alvin Kamara", "proj": 267},
        {"name": "Chuba Hubbard", "proj": 300},
        {"name": "James Conner", "proj": 336},
        {"name": "TreVeyon Henderson", "proj": 267},
        {"name": "Kenneth Walker III", "proj": 259},
        {"name": "Breece Hall", "proj": 250}
    ],
    "WR": [
        {"name": "Justin Jefferson", "proj": 325},
        {"name": "Ja'Marr Chase", "proj" : 315},
        {"name": "CeeDee Lamb", "proj": 317},
        {"name": "Amon-Ra St. Brown", "proj": 301},
        {"name": "Malik Nabers", "proj": 299},
        {"name": "A.J. Brown", "proj": 290},
        {"name": "Puka Nacua", "proj": 270},
        {"name": "Tyreek Hill", "proj": 275},
        {"name": "Nico Collins", "proj": 267},
        {"name": "Garrett Wilson", "proj": 265},
        {"name": "Drake London", "proj": 264},
        {"name": "Marvin Harrison Jr.", "proj": 253},
        {"name": "Brandon Aiyuk", "proj": 257},
        {"name": "Jaylen Waddle", "proj": 241},
        {"name": "Chris Olave", "proj": 248},
        {"name": "DeVonta Smith", "proj": 230},
        {"name": "DJ Moore", "proj": 241},
        {"name": "Michael Pittman Jr.", "proj": 240},
        {"name": "Brian Thomas Jr.", "proj": 235},
        {"name": "Rome Odunze", "proj": 249}
    ],
    "TE": [
        {"name": "Brock Bowers", "proj": 263},
        {"name": "Trey McBride", "proj": 259},
        {"name": "George Kittle", "proj": 228},
        {"name": "Sam LaPorta", "proj": 192},
        {"name": "TJ Hockenson", "proj": 185},
        {"name": "Travis Kelce", "proj": 180},
        {"name": "David Njoku", "proj": 177},
        {"name": "Mark Andrews", "proj": 173},
        {"name": "Evan Engram", "proj": 168},
        {"name": "Tyler Warren", "proj": 166}
    ],
     "K": [
        {"name": "Jake Bates", "proj": 146},
        {"name": "Chase McLaughlin", "proj": 147},
        {"name": "Cameron Dicker", "proj": 144},
        {"name": "Brandon Aubrey", "proj": 142},
        {"name": "Tyler Bass", "proj": 142},
        {"name": "Jake Elliott", "proj": 141},
        {"name": "Chris Boswell", "proj": 138},
        {"name": "Harrison Butker", "proj": 139},
        {"name": "Cairo Santos", "proj": 140},
        {"name": "Tyler Loop", "proj": 140}
     ]
         }

# Combined all players from dict -> single list
all_players = []
for pos, lst in players.items():
    for p in lst:
       all_players.append({"name": p["name"], "proj": p["proj"], "pos": pos})

# Start the available pool
available = [p for p in all_players if isinstance(p.get("proj"), (int, float))]

# Best Available Player List
sorted_players = sorted(available, key=lambda p: p["proj"], reverse=True)

# Sanity check
print("Total players:", len(all_players))
print("Available now:", len(available))
print("Top 3:", [(p["name"], p["proj"]) for p in sorted_players[:3]])

# 6 Teams with position counts
teams = []
for i in range (6):
    teams.append({
        "name": f"Team {i+1}",
        "roster": [],
        "counts": {k: 0 for k in ROSTER_LIMITS} # QB/RB/WR/TE/K/FLEX
    })
    
# Make Team 1 your team
USER_TEAM_NAME = "Payton"
teams[0]["name"] = USER_TEAM_NAME

picks_log = []  # each item: {round, overall, team, name, pos, proj}


# Tiny helpers: can_add and add_player_to_team
def can_add(player, team):
    pos = player["pos"]
    # Dedicated slot available?
    if team["counts"][pos] < ROSTER_LIMITS[pos]:
        return True
    # Otherwise try FLEX (only for RB/WR/TE)
    if pos in ("RB", "WR", "TE") and team["counts"]["FLEX"] < ROSTER_LIMITS["FLEX"]:
        return True
    return False

# Scoring helper
def add_player_to_team(player, team):
    pos = player["pos"]
    # Prefer dedicated slot
    if team ["counts"][pos] < ROSTER_LIMITS[pos]:
        team["counts"][pos] +=1
        slot = pos
    # Else FLEX for RB/WR/TE
    elif pos in ("RB", "WR", "TE") and team["counts"]["FLEX"] < ROSTER_LIMITS["FLEX"]:
        team["counts"]["FLEX"] += 1
        slot = "FLEX"
    else:
        return False # not allowed
    # record the pick (save which slot it used- nice for debugging)
    team["roster"].append({
        "name": player["name"],
        "proj": player["proj"],
        "pos": pos,
        "slot": slot
    })
    return True
def pick_score(p, team, r, num_rounds):
    base = p["proj"]
    w = 1.0

    # Delay QBs early; ease up later; add urgency late if no QB yet
    if p["pos"] == "QB":
        if r <= 2:
            w *= 0.55      # strong early penalty
        elif r <= 4:
            w *= 0.85      # softer mid penalty
        else:
            w *= 1.00
        if r >= num_rounds - 1 and team["counts"]["QB"] == 0:
            w *= 1.20      # late nudge to grab a QB

    # Mild push to RB/WR early (optional)
    if p["pos"] in ("RB", "WR") and r <= 2:
        w *= 1.10

    # Small “need” bonus if you don’t have that position yet
    if team["counts"].get(p["pos"], 0) == 0:
        w *= 1.05

    return base * w

# Final Standings Helper
def team_total(team):
    return sum(p["proj"] for p in team["roster"])

def print_standings(teams):
    rows = sorted([(team["name"], team_total(team)) for team in teams],
                  key=lambda x: x[1], reverse=True)
    subhead("Final Standings (by total projected points)")
    print(f"{'Rank':<5} {'Team':<20} {'Total':>6}")
    print("-" * 36)
    for i, (name, total) in enumerate(rows, start=1):
        print(f"{i:<5} {name:<20} {int(total):>6}")

# Snake Draft order
num_rounds = 8
num_teams = len(teams)
draft_order = []
for r in range(num_rounds):
    if r % 2 == 0:
        draft_order.extend(range(num_teams))
    else:
        draft_order.extend(reversed(range(num_teams)))

# Simulated picks (round-aware)
for pick_idx, team_index in enumerate(draft_order):
    current_round = pick_idx // num_teams + 1  # 1-based round number
    team = teams[team_index]

    # Build eligible once per pick
    eligible = [p for p in available if can_add(p, team)]

    if team["name"] == USER_TEAM_NAME:
        if not eligible:
            print("No eligible players left for your roster limits!")
            continue

        # Show suggestions ranked by our weighted score
        top5 = sorted(
            eligible,
            key=lambda x: pick_score(x, team, current_round, num_rounds),
            reverse=True
        )[:5]

        # Show suggestions ranked by your pick_score
        top5 = sorted(
            eligible,
            key=lambda x: pick_score(x, team, current_round, num_rounds),
            reverse=True
        )[:5]
        
        print_options_table(top5, show_index=True, title=f"Round {current_round}: Your turn! Top options")
        
        while True:
            s = input("Pick a player (0-4): ").strip()
            if s.isdigit():
                choice = int(s)
                if 0 <= choice < len(top5):
                    break
            print("Please enter a number 0–4.")
        pick = top5[choice]


    else:
        if not eligible:
            # Nothing fits this team’s limits (rare if your pool is big)
            continue

        # Bot: choose best by weighted score
        pick = max(
            eligible,
            key=lambda x: pick_score(x, team, current_round, num_rounds)
        )

    add_player_to_team(pick, team)
    available.remove(pick)

picks_log.append({
    "round": current_round,
    "overall": pick_idx + 1,
    "team": team["name"],
    "name": pick["name"],
    "pos": pick["pos"],
    "proj": pick["proj"],
})


# Print Results after Draft Ends
for team in teams:
    total = sum(p["proj"] for p in team["roster"])
    print(team["name"], "->", [p["name"] for p in team["roster"]], "TOTAL:", total)
print_standings(teams)

