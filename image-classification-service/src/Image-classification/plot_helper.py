from matplotlib import pyplot as plt

def plot_model(probabilities, predictions, labels, modelname, labelset, save=False, filename='model_predictions.png'):
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    fig.suptitle(f"{modelname} on {labelset}")

    axs[0].hist(probabilities, bins=100, alpha=0.7)
    axs[0].set_title('Predictions')
    axs[0].set_xlabel('Prob')
    axs[0].set_ylabel('Freq')

    axs[1].scatter(range(len(predictions)), predictions, c=labels, cmap='viridis', alpha=0.7)
    axs[1].set_title('Predictions Against True Labels')
    axs[1].set_xlabel('Sample Index')
    axs[1].set_ylabel('Prediction')
    fig.tight_layout()
    if save:
            fig.savefig(filename)
    plt.show()
    plt.close(fig)