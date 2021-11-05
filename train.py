import os
import ast
import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression


def get_model():
    return LinearRegression()


def get_xy(processed_df):
    feature_list = processed_df['v']
    feature_list = feature_list.apply(lambda x: ast.literal_eval(x))
    X = pd.DataFrame(feature_list.to_list())    

    y = processed_df['TAC_Reading']

    return X, y


def train():
    processed_df = pd.read_csv(os.path.join('data', 'train', 'processed_data.csv'))
    X, y = get_xy(processed_df)

    model = get_model()
    model.fit(X, y)

    return model


def test(model):
    processed_test_df = pd.read_csv(os.path.join('data', 'test', 'processed_data.csv'))
    X, y = get_xy(processed_test_df)
    score = model.score(X, y)

    return score


def predict(trained_model, X):
    predictions = trained_model.predict(X)

    return predictions

def main():
    trained_model = train()
    score = test(trained_model)
    print(f'Test score: {score}')
    
    if not os.path.exists('trained_models'):
        os.mkdir('trained_models')

    filename = os.path.join('trained_models', 'linear_regression.pkl')
    pickle.dump(trained_model, open(filename, 'wb'))

if __name__ == '__main__':
    main()