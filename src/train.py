


if __name__ == "__main__":

    from src.dataset import load_dataset
    from src.targets import create_targets
    
    print("Loading dataset...")
    df = load_dataset()

    print("Creating targets...")
    df = create_targets(df, type = "binary")
    
    print(df.head())
    print(df.shape)
    
    # Preprocessing
    

    # Split 
    FEATURES = ["feature_" + str(i) for i in range(0,129)]
    target = "target_binary"

    y = df[target].values
    X = df[FEATURES]

    print(f"Target is: {target}")
    print(f"Features for training: {X.columns}")
    assert len(X) == len(y)


    # Select and Train ML model
    from src import dispatcher

    MODEL = "logistic_regression"

    clf = dispatcher.MODELS[MODEL]
    print(f"Selected model is {MODEL}, with parameters {clf}")

    clf.fit(X, y)

    # Save trained model
    import joblib
    joblib.dump(clf, f"models/{MODEL}_v0.pkl")