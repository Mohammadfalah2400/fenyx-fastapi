
import copy
import uuid

_GAMES_STORAGE = {
    1: {
        "id": 1,
        "player_id":1,
        "player_id_2":1,
        "game_side":game_side_,
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

_PLAYER_SORTED = {
     1:{
     "score_player1":0,
     "score_player2":0,
     }
}

def get_score(counter1, counter2 ):

    _PLAYER_SORTED[counter1 , counter2] = {
         1:{
         "score_player1": counter1,
         "score_player2" : counter2,
         }
    }
    return _PLAYER_SORTED[counter1,counter2]

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

    _GAMES_STORAGE[id_ , player_id ,player_id_2,game_side_] = {
        "id": id_,
        "player_id" : player_id,
        "player_id_2" :player_id_2, 
        "status": "new",
        "game_side":game_side_,
        "current_move": "x",
        "field": [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ],
    }

    return _GAMES_STORAGE[id_ ,player_id,player_id_2,game_side_]


def get_game(id: int, player_id:int, player_id_2:int ,game_side:str) -> dict | None:
    global game_side_
    game_side_ = game_side
    game = _GAMES_STORAGE.get(id , player_id,player_id_2 , game_side)
    return copy.deepcopy(game , player_id,player_id_2, game_side)


def update_game(id: int,player_id:int,player_id_2:int ,  data: dict):
    if id not in _GAMES_STORAGE or player_id not in _GAMES_STORAGE or player_id_2 not in _GAMES_STORAGE :
        raise ValueError(f"No game with id {id} and player1 id {player_id} and player2 {player_id_2}")

    _GAMES_STORAGE[id ,player_id,player_id_2] = data
