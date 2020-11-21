from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from controllers.VoiceRecognizerController import VoiceRecognizerController
from controllers.FireBaseController import FirebaseController

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def hello():
    print('aqui filha da puta')
    # fc = FirebaseController()
    # fc.FireStoreClient.collection('Voices').document('UserVoices').set({'message': 'hello world2'})
    return jsonify({"success": True}), 200

@app.route('/new-voice', methods = ['POST'])
def newAutorizedVoice():
    VoiceRecognizerController.SaveBinaryFile(request.get_data(),'Lucas_Silva')
    return {'response': True}, 200



if __name__ == "__main__":
    #controller = VoiceRecognizerController()
    #controller.ExecuteTrain()
    app.run(host='192.168.100.9',port=8000, debug=True)

    