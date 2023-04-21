import argparse
import json
import requests

BASE_URL = "localhost:8000"


def check_response(response) -> bool:
    if response.status_code >= 400:
        print(f"Got response {response.status_code}: {response.text}")
        return False
    return True


def parse_args():
    # sys.argv

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "action",
        choices=[
            "list-games",
            "create-game",
            "make-move",
            "register-as-a-player",
            "join_existing_games",
            "player_score",
        ],
        help="Action to perform",
    )
    return parser.parse_args()

def register_as_a_player():
    response = requests.post(
        f"http://{BASE_URL}/register-as-a-player/",
    )
    if not check_response(response):
        return

    print(response.json())
    
def score():
    response = requests.get(
        f"http://{BASE_URL}/score/",
    )
    if not check_response(response):
        return

    data = response.json()
    print(json.dumps(data, indent=4))




def list_games():
    response = requests.get(
        f"http://{BASE_URL}/list-games/",
    )
    if not check_response(response):
        return

    data = response.json()
    print(json.dumps(data, indent=4))



def create_game():
    response = requests.post(f"http://{BASE_URL}/create-game/")
    if not check_response(response):
        return

    print(response.json())

def join_existing_games():
    response =requests.get(f"http://{BASE_URL}/join_existing_games/")
    if not check_response(response):
        return

    print(response.json())
 

def make_move():
    player = int(input("Player ID"))
    game_id = int(input("Game ID: "))
    game_side = str(input("whats is your part?(x / o)"))
    row = int(input("Row: "))
    col = int(input("Col: "))

    response = requests.post(
        f"http://{BASE_URL}/game/{game_id}/{game_side}{player}/move/",
        json={
            "row": row,
            "col": col,
            "player": player,
            "game_side":game_side
        },
    )
    if not check_response(response):
        return

    print(response.json())


def main():
    args = parse_args()

    if args.action == "list-games":
        list_games()
    elif args.action == "create-game":
        create_game()
    elif args.action == "make-move":
        make_move()
    elif args.action == "register-as-a-player":
        register_as_a_player()
    elif args.action == "join_existing_games":
        join_existing_games()
    elif args.action == "player_score":
        score()
    else:
        raise ValueError(f"Unknown action: {args.action}")


if __name__ == "__main__":
    main()
