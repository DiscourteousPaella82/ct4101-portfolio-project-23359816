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
                fig.savefig(f"output/graphs/{names[i]}_{labelnames[j]}_predictions.png")
            if show:
                plt.show()
                plt.close(fig)

def plot_models_metrics(names, metric_results, save=False, show=False, verbose=False):
    metric_keys = list(metric_results[0])
    for i in range(len(metric_results)):
        metrics = []
        for j in range(len(metric_results[i])):
            metrics.append(metric_results[j][metric_keys[j]])

        fig, ax = plt.subplots(figsize=(10,5))

        p = ax.bar(names, metrics)
        ax.bar_label(p, label_type='center')
            
        ax.set_ylabel(f"{metric_keys[i]}")
        ax.set_title(f"Models {metric_keys[i]} results")

        if save:
            plt.savefig(f"output/graphs/{metric_keys[i]}_results.png")
        if show:
            plt.show()
            plt.close()
