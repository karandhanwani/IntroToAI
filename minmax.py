class NPlayerTrivialGame:
    def __init__(self, num_players=2):
        self.initial_state = [0]  # Initial state with a single value
        self.num_players = num_players
        self.current_player = 0  # Player index, starting with 0

    def is_terminal(self, state):
        return len(state) == 2

    def utility(self, state):
        return sum(state)

    def actions(self, state):
        return [1, 2, 3]  # Possible moves to add to the current state

    def result(self, state, action):
        new_state = state + [action]
        self.current_player = (self.current_player + 1) % self.num_players  # Switch to the next player
        return new_state


def minimax_search(game, state, maximizing_player=True):
    if maximizing_player:
        value, move = max_value(game, state)
    else:
        value, move = min_value(game, state)
    return move, value


def max_value(game, state):
    if game.is_terminal(state):
        return game.utility(state), None

    v, move = float("-inf"), None
    for a in game.actions(state):
        v2, a2 = min_value(game, game.result(state, a))
        if v2 > v:
            v, move = v2, a
    return v, move


def min_value(game, state):
    if game.is_terminal(state):
        return game.utility(state), None

    v, move = float("inf"), None
    for a in game.actions(state):
        v2, a2 = max_value(game, game.result(state, a))
        if v2 < v:
            v, move = v2, a
    return v, move


if __name__ == "__main__":
    # 2-player game
    print("2-Player Game:")
    game_2player = NPlayerTrivialGame(num_players=2)
    initial_state_2player = game_2player.initial_state
    while not game_2player.is_terminal(initial_state_2player):
        # print(f"\nPlayer {game_2player.current_player} moves:")
        best_move_2player, value_2player = minimax_search(game_2player, initial_state_2player, maximizing_player=True)
        print(f"MAX Move: {best_move_2player}, Value: {value_2player}")
        initial_state_2player = game_2player.result(initial_state_2player, best_move_2player)

    # 4-player game
    print("\n4-Player Game:")
    game_4player = NPlayerTrivialGame(num_players=4)
    initial_state_4player = game_4player.initial_state
    while not game_4player.is_terminal(initial_state_4player):
        # print(f"\nPlayer {game_4player.current_player} moves:")
        best_move_4player, value_4player = minimax_search(game_4player, initial_state_4player, maximizing_player=True)
        print(f"MAX Move: {best_move_4player}, Value: {value_4player}")
        initial_state_4player = game_4player.result(initial_state_4player, best_move_4player)
