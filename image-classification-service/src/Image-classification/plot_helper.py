from matplotlib import pyplot as plt

def plot_model(probabilities, predictions, labels, save=False, filename='model_predictions.png'):
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.hist(probabilities, bins=100, alpha=0.7)
    plt.title('Predictions')
    plt.xlabel('Prob')
    plt.ylabel('Freq')

    plt.subplot(1, 2, 2)
    plt.scatter(range(len(predictions)), predictions, c=labels, cmap='viridis', alpha=0.7)
    plt.title('Predictions Against True Labels')
    plt.xlabel('Sample Index')
    plt.ylabel('Prediction')
    plt.tight_layout()
    if save:
            plt.savefig(filename)
    plt.show()
    plt.close()