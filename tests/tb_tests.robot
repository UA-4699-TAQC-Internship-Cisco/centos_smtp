*** Settings ***
Library    BuiltIn
Library    Process
Library    OperatingSystem
Library    SSHLibrary
Library    ../scripts/TetianaBrekhova.py

*** Variables ***

${SMTP_HOST}    ______
${SMTP_PORT}    25
${FROM}         ______
${TO}           ______
${BODY}         This is a test message.
${PASS}         ______


*** Test Cases ***
Test SMTP Connection
    ${banner}=    Evaluate    __import__('smtplib').SMTP("${SMTP_HOST}", ${SMTP_PORT}).noop()
    Log    ${banner}
    Should Be Equal As Integers    ${banner[0]}    250


Check Body In Mail File
    Send Mail   ${SMTP_HOST}    ${FROM}    ${TO}   ${BODY}
    Open Connection    ${SMTP_HOST}
    Login              ${TO}    ${PASS}
    ${mail}=           Execute Command    cat /var/mail/tetiana
    Should Contain     ${mail}    ${BODY}
    Close Connection


#add a method to read the file
