from sklearn.ensemble import IsolationForest

model = IsolationForest()

def train(data):
    model.fit(data)

def predict(sample):
    return model.predict([sample])
