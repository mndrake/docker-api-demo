from joblib import load
import pkg_resources


features = [
    'RevolvingUtilizationOfUnsecuredLines',
    'age',
    'NumberOfTime30-59DaysPastDueNotWorse',
    'DebtRatio',
    'MonthlyIncome',
    'NumberOfOpenCreditLinesAndLoans',
    'NumberOfTimes90DaysLate',
    'NumberRealEstateLoansOrLines',
    'NumberOfTime60-89DaysPastDueNotWorse',
    'NumberOfDependents']

model_path = pkg_resources.resource_filename(__name__, "model/nb.joblib")
model = load(model_path)

def score(df):
    X = df[features]
    return model.predict_proba(X)