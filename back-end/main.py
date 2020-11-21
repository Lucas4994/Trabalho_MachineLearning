from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from controllers.VoiceRecognizerController import VoiceRecognizerController
from controllers.FireBaseController import FirebaseController

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methodes = ['GET'])
def hello():
    # fc = FirebaseController()
    # fc.FireStoreClient.collection('Voices').document('UserVoices').set({'message': 'hello world2'})
    return jsonify({"messa": "Welcome to voice app!"}), 200

@app.route('/new-voice', methods = ['POST'])
def newAutorizedVoice():
    VoiceRecognizerController.SaveBinaryFile(request.get_data(),'Lucas_Silva')
    return {'response': True}, 200



if __name__ == "__main__":
    port = int(os.environ.get('PORT', 33507))
    app.run(debug=True, port=port)

    