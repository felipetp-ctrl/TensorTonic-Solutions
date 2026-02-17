import numpy as np

def stratified_split(X, y, test_size, rng, seed=42):
    """
    Split features X and labels y into train/test while preserving class proportions.
    """
    # Write code here
    pass

    X = np.array(X)
    y = np.array(y)

    unique_counts = np.unique(y)

    X_train = []
    X_test = []
    y_train = []
    y_test = []


    if rng is None:
        rng = np.random.default_rng(seed)
    elif isinstance(rng, int):
        rng = np.random.default_rng(rng)

    for c in unique_counts:
        index_per_class = np.where(y == c)[0]
        vinc_index = index_per_class.tolist()
        
        rng.shuffle(vinc_index)
        
        size = round(len(vinc_index) * test_size)
        
        test_idx = sorted(vinc_index[:size])
        train_idx = sorted(vinc_index[size:])

        if X.ndim == 1:
            X_test.extend([int(X[i]) for i in test_idx])
            X_train.extend([int(X[i]) for i in train_idx])
        else:
            X_test.extend([X[i].tolist() for i in test_idx])
            X_train.extend([X[i].tolist() for i in train_idx])

        y_test.extend([int(y[i]) for i in test_idx])
        y_train.extend([int(y[i]) for i in train_idx])

    return [X_train, X_test, y_train, y_test]