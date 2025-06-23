*** Settings ***
Library    BuiltIn
Library    Process
Library    OperatingSystem
Library    SSHLibrary
Library    ../resources/scripts/TetianaBrekhova.py
Library    ../resources/data/bt_data.py


*** Variables ***
${SMTP_PORT}    25
${BODY}         This is a test message.


*** Test Cases ***
Test SMTP Connection
    ${SMTP_HOST}=    Get Env    VR_HOST
    ${banner}=    Evaluate    __import__('smtplib').SMTP("${SMTP_HOST}", ${SMTP_PORT}).noop()
    Log    ${banner}
    Should Be Equal As Integers    ${banner[0]}    250

Check Body In Mail File
    ${SMTP_HOST}=    Get Env    VR_HOST
    ${FROM}=    Get Env    SENDER_USERNAME
    ${TO}=    Get Env    RECEIVER
    ${USER}=    Get Env    VM_USERNAME
    ${PASS}=    Get Env    PASSWORD
    Send Mail   ${SMTP_HOST}    ${FROM}    ${TO}   ${BODY}
    Open Connection    ${SMTP_HOST}
    Login              ${USER}    ${PASS}
    ${mail}=           Execute Command    cat /var/mail/tetiana
    Should Contain     ${mail}    ${BODY}
    Close Connection

Check Count
    ${SMTP_HOST}=    Get Env    VR_HOST
    ${USER}=    Get Env    VM_USERNAME
    ${PASS}=    Get Env    PASSWORD
    ${FROM}=    Get Env    SENDER_USERNAME
    ${TO}=    Get Env    RECEIVER
    ${start_mail_list}=    Get Mail List   ${SMTP_HOST}   ${USER}    ${PASS}
    ${start_mail_length}=    Get Length    ${start_mail_list}
    Send Mail   ${SMTP_HOST}    ${FROM}    ${TO}   ${BODY}
    ${mail_list}=    Get Mail List   ${SMTP_HOST}   ${USER}    ${PASS}
    ${mail_length}=    Get Length    ${mail_list}
    Should Be Equal As Integers     ${mail_length}      ${start_mail_length+1}
