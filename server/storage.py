
import copy
import uuid

_GAMES_STORAGE = {
    1: {
        "id": 1,
        "player_id":1,
        "status": "new",
        "current_move": "x",
        "field": [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ],
    },
}





def get_games():
    return list(_GAMES_STORAGE.values())

def register_player():
    global player_id 
    player_id = uuid.uuid4()
 #   return _GAMES_STORAGE[player_id]


def create_game():
    id_ = len(_GAMES_STORAGE) + 1

    _GAMES_STORAGE[id_ , player_id] = {
        "id": id_,
        "player_id" : player_id,
        "status": "new",
        "current_move": "x",
        "field": [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ],
    }

    return _GAMES_STORAGE[id_ ,player_id]


def get_game(id: int) -> dict | None:
    game = _GAMES_STORAGE.get(id , player_id)
    return copy.deepcopy(game , player_id)


def update_game(id: int,player_id:int, data: dict):
    if id not in _GAMES_STORAGE or player_id not in _GAMES_STORAGE :
        raise ValueError(f"No game with id {id} and player id {player_id}")

    _GAMES_STORAGE[id ,player_id] = data
