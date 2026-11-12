from matplotlib import pyplot as plt

def plot_models_predictions(names, probabilities, predictions, labels, labelnames,save=False, show=False, verbose=False):
    for i in range(len(names)):
        for j in range(2):
            if(verbose):
                print(f"Plotting {names[i]} on {labelnames[j]}")
            fig, axs = plt.subplots(1, 2, figsize=(10, 5))
            fig.suptitle(f"{names[i]} on {labelnames[j]}")

            axs[0].hist(probabilities[j][i], bins=100, alpha=0.7)
            axs[0].set_title('Predictions')
            axs[0].set_xlabel('Prob')
            axs[0].set_ylabel('Freq')

            axs[1].scatter(range(len(predictions[j][i])), predictions[j][i], c=labels[j], cmap='viridis', alpha=0.7)
            axs[1].set_title('Predictions Against True Labels')
            axs[1].set_xlabel('Sample Index')
            axs[1].set_ylabel('Prediction')
            fig.tight_layout()
            if save:
                fig.savefig(f"{names[i]}_{labelnames[j]}_predictions.png")
            if show:
                plt.show()
                plt.close(fig)