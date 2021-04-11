# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import json
import os
import azure.functions as func
import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):
    # get payload passed from httpstarter fn
    payload = context.get_input()

    # send slack notification
    slackNotification = yield context.call_activity('notifySlackChannel', payload)

    # TODO: update to mongodb
    result3 = yield context.call_activity('Hello', "Seattle")

    # TODO: check if email exists
    isEmailExists = yield context.call_activity('isEmailExists', payload)

    # TODO: send auto email, if valid email
    if (isEmailExists == True):
        yield context.call_activity('Hello', "Seattle")
        # TODO: send email block to slack only if email is valid

    return [slackNotification, isEmailExists, result3]


main = df.Orchestrator.create(orchestrator_function)
