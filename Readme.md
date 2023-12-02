# TDT4173 - Machine Learning Project

This is the repository for a project in TDT4173 - Machine Learning at NTNU. The project is about forecasting solar energy production. 

The project was done by:

- [Sondre Kolberg](https://github.com/sondrekol)
- [Oscar Timm Marcussen](https://github.com/oscarmarcussen)
- [Magnus Byrkjeland](https://github.com/sleipner01)

The repo is structured into branches, where each branch contains a different approach to the problem, data exploration, data cleaning and model generation. There also exists a branch for the final delivery. 

The project is based on a Kaggle competition. Sadly, the competition is private, but the project and data is described in the section below.

# Solar Dayahead Forecast Data

This dataset provides data for evaluating solar production dayahead forecasting methods.
The dataset contains three locations (A, B, C), corresponding to office buildings with solar panels installed.
There is one folder for each location.

There are 4 files in each folder:

1. train_targets.parquet - target values for the train period (solar energy production)
2. X_train_observed.parquet - actual weather features for the first part of the training period
2. X_train_estimated.parquet - predicted weather features for the remaining part of the training period
2. X_test_estimated.parquet - predicted weather features for the test period

For Kaggle submissions we have two more files: 
1. test.csv — test file with zero predictions (for all three locations)
2. sample_submission_kaggle.csv — sample submission in the Kaggle format (for all three locations)

Kaggle expects you to submit your solutions in the "sample_sumbission_kaggle.csv" format. Namely, you need to have two columns: "id" and "prediction".
The correspondence between id and time/location is in the test.csv file. An example solution is provided in "read_files.ipynb"

All files that are in the parquet format that can be read with pandas:
```shell
pd.read_parquet()
```

Baseline and targets production values have hourly resolution.
Weather has 15 min resolution.
Weather parameter descriptions can be found [here](https://www.meteomatics.com/en/api/available-parameters/alphabetic-list/).

There is a distinction between train and test features.
For training, we have both observed weather data and its forecasts, while for testing we only have forecasts.
While file `X_train_observed.parquet` contains one time-related column `date_forecast` to indicate when the values for the current row apply,
both `X_train_estimated.parquet` and  `X_test_estimated.parquet` additionally contain `date_calc` to indicate when the forecast was produced.
This type of test data makes evaluation closer to how the forecasting methods that are used in production.
Evaluation measure is [MAE](https://en.wikipedia.org/wiki/Mean_absolute_error).
