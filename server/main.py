from fastapi import FastAPI
from fastapi import HTTPException

import storage
import schemas


app = FastAPI()


@app.get("/list-games/")
async def list_games():
    return {
        "games": storage.get_games(),
    }

@app.get("/score/")
async def score():
    print_board()
    return{
        "score": storage.get_score(counter1 , counter2),
    }


@app.post("/register-as-a-player/")
async def register_as_a_player(name: str):
    return storage.register_player(name)


@app.post("/join_existing_games/")
async def join_existing_games(game_id : int) : 
    return storage.join_existing_games(game_id)

@app.post("/create-game/")
async def create_game():
    return storage.create_game()


def check_winner(game: dict) -> str | None:
    """
    >>> check_winner({
    ...     "field": [
    ...         ["x", "x", "x"],
    ...         [None, None, None],
    ...         [None, None, None],
    ...     ],
    ... })
    'x'
    >>> check_winner({
    ...     "field": [
    ...         [None, None, None],
    ...         ["o", "o", "o"],
    ...         [None, None, None],
    ...     ],
    ... })
    'o'
    """
    global field
    field = game["field"]
    for row in field:
        if row[0] == row[1] == row[2] and row[0] is not None:
            game["status"] = "finished"
            return row[0]

    for col in range(3):
        if (
            field[0][col] == field[1][col] == field[2][col]
            and field[0][col] is not None
        ):
            game["status"] = "finished"
            return field[0][col]

    if field[0][0] == field[1][1] == field[2][2] and field[0][0] is not None:
        game["status"] = "finished"
        return field[0][0]

    if field[0][2] == field[1][1] == field[2][0] and field[0][2] is not None:
        game["status"] = "finished"
        return field[0][2]

    return None

def print_board():
    for row in range(3):
        print("|".join(field[row]))
        if row !=2 :
            print("---------------------------")



@app.post("/game/{game_id}/{player_id}/{player_id_2}/{game_side}/move/")
async def make_move(game_id: int,player_id:int,player_id_2:int,game_side:str ,move: schemas.Move):
    game = storage.get_game(game_id ,player_id,player_id_2,game_side)

    if game is None:
        raise HTTPException(status_code=404, detail="Game not found")
    if player_id is None : 
        raise HTTPException(status_code=404 , detail="player id not found ")
    if player_id_2 is None : 
        raise HTTPException(status_code= 404 , detail="player id 2 not found ")
    if game["status"] != "new":
        raise HTTPException(status_code=400, detail="Game is not new")

    if game["field"][move.row][move.col] is not None:
        raise HTTPException(status_code=400, detail="Cell is not empty")

    if game["current_move"] != move.player:
        raise HTTPException(status_code=400, detail="Wrong player")

    game["current_move"] = game_side  if move.player == "o" else "x"
    game["field"][move.row][move.col] = move.player

    winner = check_winner(game)

    storage.update_game(game_id, game)
    global counter1
    global counter2
    counter1 = 0
    counter2 = 0

    resp = {"status": "ok"}
    if winner is not None:
        resp["winner"] = winner
        counter1 += 1 
    elif winner is None :
        resp["not winner"] = winner
        counter2 +=1

    return resp


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
