import logging
import azure.functions as func
import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):
    # get payload passed from httpstarter fn
    payload = context.get_input()

    # send slack notification
    slackNotification = yield context.call_activity('notifySlackChannel', payload)

    # TODO: future; update data to mongodb
    # not really needed now. works fine with slack + email.
    # addToDB = yield context.call_activity('addToDB', payload)

    # check if email is valid
    isEmailExists = yield context.call_activity('isEmailExists', payload)
    logging.info(f'is existing email? {isEmailExists}')

    # send email if valid email
    sentEmail = False
    if (isEmailExists == True):
        logging.info('Valid email. Sending email.')
        sentEmail = yield context.call_activity('sendEmail', payload)
        logging.info('Email sent.')

    return [slackNotification, isEmailExists, sentEmail]


main = df.Orchestrator.create(orchestrator_function)
