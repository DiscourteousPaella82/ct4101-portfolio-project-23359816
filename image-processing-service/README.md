# Image Processing Service

This python application is responsible for the image processing pipeline for extracting features for consumation by machine learning models.

#### Environment Variables:
```
IMAGES_PATH {"/path/to/images"} (Required)
TOTAL_IMAGES_COUNT {non zero integer (preferably even)} (optional)
```

#### Arguments:
```
-v --Verbose (prints what is happening to stdout)
-p --Plot   (sequentially shows graphs of images in the pipeline)
-f --Filename   (choose filename)
-o --Output (choose output path)
```