#!/usr/bin/env python3
# add import and helper functions here
import numpy as np

if __name__ == "__main__":
    # code goes here
    print("Hello World")
    np.random.seed(42)
    A = np.random.normal(size=(4, 4))
    B = np.random.normal(size=(4, 2))
    print(A@B)

    np.random.seed(42)
    x = np.random.normal(size=(4, 10))

    diffs = x[:, None, :] - x[None, :, :] #(4, 1, 10)-(1, 4, 10) = (4, 4, 10)
    D = np.sum(diffs**2, axis=2)
    print(D)
