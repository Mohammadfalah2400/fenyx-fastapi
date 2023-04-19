
import copy
import uuid

_GAMES_STORAGE = {
    1: {
        "id": 1,
        "player_id":1,
        "player_id_2":1,
        "status": "new",
        "number of the players":1,
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
    global player_id_2
    player_id_2 =uuid.uuid4()
    player_id = uuid.uuid4()
 #   return _GAMES_STORAGE[player_id]

def join_existing_games(game_id):
         if game_id not in _GAMES_STORAGE or player_id_2   : 
            raise ValueError(f"No game with id {game_id} or this game is full  ")
         else: 
              print("you can join this game ")
              player_id_2 = input("pleaser enter the id")
              _GAMES_STORAGE[player_id_2]
         



def create_game():
    id_ = len(_GAMES_STORAGE) + 1

    _GAMES_STORAGE[id_ , player_id ,player_id_2] = {
        "id": id_,
        "player_id" : player_id,
        "player_id_2" :player_id_2, 
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
    game = _GAMES_STORAGE.get(id , player_id,player_id_2)
    return copy.deepcopy(game , player_id,player_id_2)


def update_game(id: int,player_id:int,player_id_2:int ,  data: dict):
    if id not in _GAMES_STORAGE or player_id not in _GAMES_STORAGE or player_id_2 not in _GAMES_STORAGE :
        raise ValueError(f"No game with id {id} and player1 id {player_id} and player2 {player_id_2}")

    _GAMES_STORAGE[id ,player_id,player_id_2] = data
