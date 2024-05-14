# from sklearn.ensemble import RandomForestClassifier as rf
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
# import numpy as np
#
# from Transactions import add_data_classify, get_data, add_data
#
#
# def classify(data_instance):
#     print("Start processing data...")
#     df = get_data()
#     X = df.drop(['alvo', 'numero'], axis=1)
#     y = df['alvo']
#
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state=42)
#
#     model = rf(n_estimators=100, random_state=42)
#     model.fit(X_train, y_train)
#     y_pred = model.predict(X_test)
#     acc = accuracy_score(y_test, y_pred)
#     f1 = f1_score(y_test, y_pred, average='macro')
#     precision = precision_score(y_test, y_pred, zero_division=1, average='macro')
#     recall = recall_score(y_test, y_pred, zero_division=1, average='macro')
#
#     data = np.array([[
#         data_instance.idade, data_instance.peso, data_instance.ec, data_instance.ce,
#         data_instance.temp_retal, data_instance.temp_amb, data_instance.umidade,
#         data_instance.mov_flanco, data_instance.turbilhao,
#         data_instance.mot_moveis, data_instance.vigor, data_instance.volume, data_instance.zptz_106,
#         data_instance.zptz_totais, data_instance.def_mai, data_instance.def_men, data_instance.def_mai_percent,
#         data_instance.def_men_percent, data_instance.normais, data_instance.normais_percent
#     ]]).reshape(1, -1)
#
#     prediction = model.predict(data)
#
#     alvo = prediction[0]
#     add_data(data_instance)
#     add_data_classify(alvo)
#
#     print("Finished processing data...")
#     if prediction[0] == 0.0:
#         return {"class": prediction[0], "message": "Animal totalmente apto a reproduçâo", "accuracy": f'{acc * 100:.2f}%'}
#     elif prediction[0] == 1.0:
#         return {"class": prediction[0], "message": "Animal apto a reprodução, porém, com restrições", "accuracy": f'{acc * 100:.2f}%'}
#     elif prediction[0] == 3.0:
#         return {"class": prediction[0], "message": "Animal não apto a reprodução", "accuracy": f'{acc * 100:.2f}%'}
#     else:
#         return "Erro no processamento dos dados"
#
