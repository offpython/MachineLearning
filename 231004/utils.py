import numpy as np
import matplotlib.pyplot as plt

def vis_geometric_dataset(X, y, alpha=0.5):
    n_classes = len(np.unique(y))
    fig, ax = plt.subplots(figsize=(10, 10))

    for class_idx in range(n_classes):
        class_X = X[y == class_idx]
        ax.scatter(class_X[:, 0], class_X[:, 1], alpha=alpha,
                   label=f"Class {class_idx}")

    ax.legend(fontsize=20)
    ax.tick_params(labelsize=15)
    ax.set_xlabel("Feature 1", fontsize=20)
    ax.set_ylabel("Feature 2", fontsize=20)
    fig.tight_layout()
    return fig, ax