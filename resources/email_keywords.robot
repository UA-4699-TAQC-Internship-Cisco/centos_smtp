*** Settings ***
Library    Collections
Library    OperatingSystem
Library    ../libraries/yuliashap_mail_send_and_read.py


*** Keywords ***
Verify SMTP Connection
    ${response}=    Evaluate    __import__('smtplib').SMTP("${HOST}", ${PORT_INT}).noop()
    Log    SMTP NOOP response: ${response}
    Should Be Equal As Integers    ${response[0]}    250

Get Email Count
    ${emails}=    Get Emails    ${USER}    ${PASS}
    ${count}=     Get Length    ${emails}
    [Return]     ${count}

Verify Email Count Increased
    [Arguments]    ${before}    ${after}
    Should Be Equal As Integers    ${after}    ${before + 1}

Verify Last Email Contents
    ${last_email}=    Fetch Last Email    ${USER}    ${PASS}
    Log Many    ${last_email}
    Should Contain    ${last_email['from']}    ${SENDER}
    Should Be Equal    ${last_email['subject']}    ${EMAIL_SUBJECT}
    Should Contain    ${last_email['body']}    ${EMAIL_BODY}

Send Test Email
    Send Email    ${SENDER}    ${RECIPIENT}    ${EMAIL_SUBJECT}    ${EMAIL_BODY}    ${HOST}    ${PORT_INT}

Get Emails
    [Arguments]    ${username}=${USER}    ${password}=${PASS}
    ${emails}=    Read All Emails    ${HOST}    ${SSH_PORT_INT}    ${username}    ${password}    ${EMAIL_DIR}
    [Return]    ${emails}

Fetch Last Email
    [Arguments]    ${username}=${USER}    ${password}=${PASS}
    ${email}=    Get Last Email    ${HOST}    ${SSH_PORT_INT}    ${username}    ${password}    ${EMAIL_DIR}
    [Return]    ${email}
