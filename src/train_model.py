# train_model.py file
import sys
import yaml
from pathlib import Path
import pickle
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

def train_model(train_features, target,n_estimators,max_depth):
    # Here is the code to train ml model
    model = RandomForestClassifier(n_estimators=n_estimators,max_depth=max_depth)
    model.fit(train_features,target)
    return model
    
def save_model(model, output_path):
    # save the trained model to specified output path
    filename = output_path+'finalized_model.pkl'
    pickle.dump(model, open(filename, 'wb'))
    

def main():
    curr_dir = Path(__file__)
    home_dir = Path.cwd()
    params_file = home_dir.as_posix()+'/params.yaml'
    params = yaml.safe_load(open(params_file))["train_model"]
    
    data_path = home_dir.as_posix()+'/data/processed/train.csv'
    
    output_path = home_dir.as_posix()+'/models/'
    
    TARGET = 'Class'
    Path(output_path).mkdir(parents=True,exist_ok=True)
    train_features = pd.read_csv(data_path)
    X_train = train_features.drop(TARGET,axis=1)
    y_train = train_features[TARGET]
    y_train=y_train.values.ravel()
    
    trained_model = train_model(X_train, y_train,params['n_estimators'],params['max_depth'])
    save_model(trained_model, output_path)
    
if __name__ =="__main__":
    main()