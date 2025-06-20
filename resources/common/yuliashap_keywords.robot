*** Keywords ***
Setup Variables
    ${SSH_HOST}=    Get Environment Variable    SSH_HOST
    Set Suite Variable    ${SSH_HOST}
    ${SSH_PORT}=    Get Environment Variable    SSH_PORT
    Set Suite Variable    ${SSH_PORT}
    ${SSH_USERNAME}=    Get Environment Variable    SSH_USERNAME
    Set Suite Variable    ${SSH_USERNAME}
    ${SSH_PASSWORD}=    Get Environment Variable    SSH_PASSWORD
    Set Suite Variable    ${SSH_PASSWORD}
    ${MAIL_FILE}=    Get Environment Variable    EMAIL_DIR
    Set Suite Variable    ${MAIL_FILE}
    ${SENDER}=    Get Environment Variable    LOCAL_SENDER
    Set Suite Variable    ${SENDER}
    ${RECIPIENT}=    Get Environment Variable    REMOTE_RECIPIENT
    Set Suite Variable    ${RECIPIENT}
    ${EMAIL_SUBJECT}=    Get Environment Variable    EMAIL_SUBJECT
    Set Suite Variable    ${EMAIL_SUBJECT}
    ${EMAIL_BODY}=    Get Environment Variable    EMAIL_BODY
    Set Suite Variable    ${EMAIL_BODY}

Get Email Count
    ${output}=    Run Process    python    -c    from scripts.yuliashap_mail_send_and_read import read_all_emails; import os; from dotenv import load_dotenv; load_dotenv(); print(len(read_all_emails("${SSH_HOST}", int(${SSH_PORT}), "${SSH_USERNAME}", "${SSH_PASSWORD}", "${MAIL_FILE}")))
    ${stdout}=    Set Variable    ${output.stdout}
    ${count}=     Convert To Integer    ${stdout.strip()}
    [Return]      ${count}

Send Email
    Run Process    python    -c    from scripts.yuliashap_mail_send_and_read import send_email; import os; from dotenv import load_dotenv; load_dotenv(); send_email("${SENDER}", "${RECIPIENT}", "${EMAIL_SUBJECT}", "${EMAIL_BODY}", "${SMTP_HOST}", int(${SMTP_PORT}))

Get Last Email
    ${output}=    Run Process    python    -c    from scripts.yuliashap_mail_send_and_read import get_last_email; import os; from dotenv import load_dotenv; load_dotenv(); import json; print(json.dumps(get_last_email("${SSH_HOST}", int(${SSH_PORT}), "${SSH_USERNAME}", "${SSH_PASSWORD}", "${MAIL_FILE}")))
    ${stdout}=    Set Variable    ${output.stdout}
    ${last}=      Evaluate    json.loads("""${stdout.strip()}""")    json
    [Return]      ${last}