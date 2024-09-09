import random

def player(prev_play, opponent_history=[]):
    moves = ["R", "P", "S"]
    
    if prev_play == "":
        # First move: choose randomly
        return random.choice(moves)
    
    # Track opponent's last moves
    opponent_history.append(prev_play)
    
    # Example strategy: counter the most frequent move
    if len(opponent_history) > 1:
        last_move = opponent_history[-2]
        if last_move == "R":
            return "P"
        elif last_move == "P":
            return "S"
        elif last_move == "S":
            return "R"
    
    # Default to random choice if no pattern is detected
    return random.choice(moves)
