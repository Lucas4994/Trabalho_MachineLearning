import librosa
import librosa.display
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import os
import pathlib
from sklearn.preprocessing import LabelEncoder, StandardScaler 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix, classification_report
import wave

import warnings

class VoiceRecognizerController:

    autorizedVoices = ["Lucas_Carvalho", "Tales_Carneiro"]

    def __init__(self):
        header = ''
        for i in range(1, 21):
            header += f' mfcc{i}'
        header += f' nome_pessoa autorizado'
        header = header.split()


        file = open('dataset.csv', 'w', newline='')
        with file:
            writer = csv.writer(file)
            writer.writerow(header)
        
        for filename in os.listdir(f'AudioSet'):
            nome = filename.split()[0]
            data, sr = librosa.load(f'AudioSet/{filename}', sr=44100)
            mfccs = librosa.feature.mfcc(y=data, sr=sr)
            to_append = ''
            for e in mfccs:
                to_append += f' {np.mean(e)}'
                
            if(nome not in self.autorizedVoices):
                to_append += f' {nome} {0}'
            else:
                to_append += f' {nome} {1}'

            file = open('dataset.csv', 'a', newline='')
            with file:
                writer = csv.writer(file)
                writer.writerow(to_append.split())

    def ExecuteTrain(self):
        data = pd.read_csv('dataset.csv')
        people_list = data.iloc[:, 21]
        print(people_list)
        encoder = LabelEncoder()
        y = encoder.fit_transform(people_list)
        scaler = StandardScaler()
        X = scaler.fit_transform(np.array(data.iloc[:, :-2], dtype = float))#Dividing data into training and Testing set
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

        mlp = MLPClassifier(solver='lbfgs', random_state=0, hidden_layer_sizes=[100, 60])
        mlp.fit(X_train, y_train)
        y_pred = mlp.predict(X_test)


        print("Camadas da rede: {}".format(mlp.n_layers_))
        print("Neurônios na camada oculta: {}".format(mlp.hidden_layer_sizes))
        print("Neurônios na camada de saída: {}".format(mlp.n_outputs_))
        print("Pesos na camada de entrada: {}".format(mlp.coefs_[0].shape))
        print("Pesos na camada oculta: {}".format(mlp.coefs_[1].shape))

        print("Acurácia da base de treinamento: {:.2f}".format(mlp.score(X_train, y_train)))
        print("Acurácia da base de teste: {:.2f}".format(mlp.score(X_test, y_test)))

        cnf_matrix = confusion_matrix(y_test, y_pred)
        print(cnf_matrix)
    
    @staticmethod
    def SaveBinaryFile(data, name):
        with open(f'{name}.wav', mode='bx') as f:
            f.write(data) 
        # nameList = name.split()
        # fileName = nameList[0] + '_' + nameList[1]
        # fp = open(f'temp_files/{fileName}', 'wb')
        # fp.write(data.encode('utf_8'))
        # fp.close()
        # return fileName

    @staticmethod
    def ConvertBinaryFileToWav(fileName):  
        file = open(f'temp_files/{filename}' 'rb')
        output = wave.open(path,'w')
        output.setparams((2,2,rate,0,'NONE','not compressed'))
        output.writeframes(frames)
        output.close()




        