# ct4101-portfolio-project-23359816
Machine Learning python project to classify between bicycles & motorbicycles.

## Repo Structure

```
assets/
image-classification-service/
image-processing-service/
output/
```

#### assets:
* Contains raw images of bikes & motorbikes in their respective subdirectory

#### [image-classification-service](image-classification-service/README.md):
* Python application which tests models using generated data by the image-processing-service

#### [image-processing-service](image-processing-service/README.md):
* Python application which generates feature data from assets

#### output:
* output directory for processed data.

## Project Report Documentation
### Data Audit
As this project generates the engineered features at the runtime of the processing service, data auditing is primarily done during the process of generating our features.

This includes:
* Resizing images to a standard size.
* Reducing noise in the dataset by gaussian smoothing.
* Thresholding images to further reduce noise & get edges.

This means that there is no explicit data auditing functionality in the image classification service as data read is expected to already be interpretable.

Note:
* The features produced by this algorithm is primarily edges.
* Data represents pixel values which are thresholded, as such duplicates are to be expected.


## Setup & Usage
### Quick Start

```shell
python -m venv .venv/   # Create virtual environment

source ./venv/bin/activate
```

### Useful Commands

#### Activate Environment
```shell
source ./venv/bin/activate
```
---
#### Install Package in Virtual Environment
```shell
pip install <package-name>
```
---
#### Deactivate Environment
```shell
deactivate
```

---
### Notes:
* Docker currently works with the image-processing-service, full compatability will be added shortly with usage instructions