letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
           "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1,
          3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_point = {value:key for value, key in zip(letters, points)}
letter_to_point[""] = 0

def score_word(word):
    return sum(letter_to_point.get(letter.upper()) for letter in word if letter.upper() in letter_to_point)

# brownie_points = score_word("Brownie")
# print(brownie_points)

players_to_words = {"player1" : ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

player_to_points = {}

def update_point_totals():
    for player, words in players_to_words.items():
        player_points = sum(score_word(word) for word in words)
        player_to_points[player] = player_points

# The function allows to add or update a player with multiple words at once:
def playword(player, *words):
    for word in words:
        try:
            players_to_words[player].append(word.upper())
        except: 
            players_to_words[player] = [word.upper()]
    

playword("Dylan", "CHOCOLATE", "Lizard", "GLASSES", "CAT") # New player
playword("player1", "SOCKET")
playword("wordNerd", "Alphabet")
playword("Lexi Con", "COPY")
playword("Prof Reader", "Reader")
print(players_to_words)

update_point_totals()
print(player_to_points)
