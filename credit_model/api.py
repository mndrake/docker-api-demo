from flask import request
import pandas as pd
from flask_restplus import Resource, fields, Namespace, marshal
from credit_model import score

namespace = Namespace('credit', description='credit default model')

credit_request = namespace.model('credit_request_v1', {
 'RevolvingUtilizationOfUnsecuredLines': fields.Float,
 'age': fields.Float,
 'NumberOfTime30-59DaysPastDueNotWorse': fields.Float,
 'DebtRatio': fields.Float,
 'MonthlyIncome': fields.Float,
 'NumberOfOpenCreditLinesAndLoans': fields.Float,
 'NumberOfTimes90DaysLate': fields.Float,
 'NumberRealEstateLoansOrLines': fields.Float,
 'NumberOfTime60-89DaysPastDueNotWorse': fields.Float,
 'NumberOfDependents': fields.Float
})

credit_response = namespace.model('credit_response_v1', {
    'default': fields.Float
})


@namespace.route('/v1')
class CreditModel(Resource):
    @namespace.expect([credit_request])
    @namespace.marshal_with(credit_response, as_list=True)
    def post(self):
        df = pd.DataFrame.from_records(marshal(request.json, credit_request))
        result = pd.DataFrame({'default': score(df)[:, 1]})
        return result.to_dict(orient='records')