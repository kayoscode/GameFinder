import webd
import getpass
import emailService
import time

print("Login to email server to receive email from after availability is found!")
emailContent = open("./res/username.txt")

username = emailContent.readline()
targetEmail = emailContent.readline()

try:
    password = getpass.getpass(prompt='Password: ', stream=None)
except Exception as error:
    print("Error receiving password", error)
else:
    print('Successfully entered password!')

emailService.verifyLogin(username, password)

games = {
    "Pokemon Platinum": "https://www.gamestop.com/video-games/more-gaming/nintendo-ds/games/products/pokemon-platinum-version/10073548.html",
    "Pokemon Diamond": "https://www.gamestop.com/video-games/more-gaming/nintendo-ds/games/products/pokemon-diamond/10064184.html",
    "Pokemon Pearl": "https://www.gamestop.com/video-games/more-gaming/nintendo-ds/games/products/pokemon-pearl/10064185.html",
    "Pokemon HeartGold": "https://www.gamestop.com/video-games/more-gaming/nintendo-ds/games/products/pokemon-heartgold---game-only/10077722.html",
    "Pokemon SoulSilver": "https://www.gamestop.com/video-games/more-gaming/nintendo-ds/games/products/pokemon-soulsilver-game-only/10077723.html",
    "Pokemon Black 2": "https://www.gamestop.com/video-games/more-gaming/nintendo-ds/games/products/pokemon-black-version-2/10101472.html",
    "Pokemon White 2": "https://www.gamestop.com/video-games/more-gaming/nintendo-ds/games/products/pokemon-white-version-2/10101473.html",
    "Pokemon White": "https://www.gamestop.com/video-games/more-gaming/nintendo-ds/games/products/pokemon-white/10078062.html",
}

gameChecker = webd.GameChecker()

while True:
    for game in games.copy():
        if gameChecker.isAvailable(games[game]):
            print(game, "is available - removing from search!")
            emailService.sendEmail(username, password, targetEmail, "\n\nFOUND GAME: {game}, buy it now!".format(game = game))
            games.pop("Pokemon Sword", None)
        else:
            print(game, "isn't available")

        time.sleep(3)

    time.sleep(60 * 10)
