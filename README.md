# BP3D ML Prediction
Series of Jupyter Notebooks to try to predict the runtimes of the Burn Pro 3D program based on inputs to the simulation before it gets run. This will provide a useful metric to users to give them some basic idea of how much time the simulation is going to take before they run it.

## Metadata
- `README.md`
    - This document describing what all is contained in this repository and the different parts of it
- `BP3D Predictions.pptx`
    - Slides explaining what all has been done on this project and explaining the dataset a bit. I recommend putting it in present mode because the slides are hard to read otherwise with the animations.

## Notebooks
- `oldgatherdata.ipynb`
  - Before `collectdata.ipynb` this was done for initial data collection. Will be necessary to run again, maybe with minor modifications to gather paths into paths.txt if we are to use future runs that haven't been collected as of August 2023. 
- `collectdata.ipynb`
    - This notebook takes the paths found in `paths.txt` and extracts them from the API that contains all the data about those simulations. Make sure to include the ACCESS_KEY and SECRET_KEY as environment variables.
- `exploration.ipynb`
  - Notebook used for Exploratory Data Analysis on the dataset collected above. Look into features that might be more or less useful to include, and how the data is structured overall. Maybe useful ways to transform the dataset.
- `regression.ipynb`
  - Initial ML approaches on the problem that are all regression based - predicting an exact number of seconds for runtime. Results on this task were fairly poor so classification was the next approach.
- `classification.ipynb`
    - Notebook to create models that do predictions in the form of classification. Guessing run time as a category of time intervals like *0-25 min* instead of guessing *330 seconds*. Many simple models were tried and a neural net with a little bit of experimentation but not too much. I tried lots of ways to transform the dataset before giving it to the models such as normalization and standard scaling (although good results may yield from trying this more). So far results are fairly decent but not amazing from the best models, acheiving roughly 64-72% accuracy depending on number of categories. 

## Locally Saved Data
- `paths.txt`
  - all the paths of simulation runs extracted and saved as text. 
- `simulation_runs.csv`
  - all the simulation data collected as raw data and saved along with the path it was extracted from
- `runs_db.csv`
  - Extra data on ignition and fuels that can be matched up with the paths (from uuid) to add additional data to the training dataset. This was found to not be very helpful in my research (see powerpoint)
- `training_data.csv`
  - Stored dataset that has been filtered and deemed appropriate to be fed to the ML models. Still some preprocessing is done after reading them sometimes like normalization but this is essentially the raw training data.

