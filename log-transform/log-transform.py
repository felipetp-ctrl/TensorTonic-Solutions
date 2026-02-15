def log_transform(values):
    """
    Apply the log1p transformation to each value.
    """
    # Write code here
    x_log = []

    for x in values:
        log_transform = (np.log(1 + x))
        x_log.append(log_transform)
    return np.array(x_log)