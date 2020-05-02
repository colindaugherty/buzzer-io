from flask import Flask, flash, render_template, request, session, redirect, url_for, jsonify
app = Flask(__name__)

app.config["SERVER_NAME"] = "buzz.colindaugherty.net"

@app.route("/api")
def index():
    return render_template("api.html")

@app.route("/api/startGame/<int:gameID>")
def startGame(gameID):
    setUpDone = True
    return jsonify({'setUpDone' : setUpDone})

@app.route("/api/getPlayerList/<int:gameID>", methods=['GET'])
def getPlayerList(gameID):
    player_list = "Coming soon"
    return jsonify({'player_list' : player_list})

@app.route("/api/getPlayerBuzzes/<int:gameID>", methods=['GET'])
def getPlayerBuzzes(gameID):
    player_buzzes = "Coming soon"
    return jsonify({'player_buzzes' : player_buzzes})

@app.route("/api/updatePlayerList/<int:gameID>", methods=['PUT'])
def updatePlayerList(gameID):
    updatedList = []
    return jsonify({'updatedPlayerList' : updatedList})

@app.route("/api/deleteGame/<int:gameID>", methods=['DELETE'])
def deleteGame(gameID):
    deletedGame = True
    return jsonify({'deletedGame' : deletedGame})

if __name__ == "__main__":
    app.run()