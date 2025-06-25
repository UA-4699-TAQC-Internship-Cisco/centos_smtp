*** Settings ***
Library    Process
Library    OperatingSystem

*** Variables ***
${SMTP_SCRIPT_PATH}      ./scripts/get_email.py
${SMTP_EXPECTED_OUTPUT}  Email sent successfully!
#${ENV_FILE}         ./env

*** Test Cases ***
Test SMTP Email Sending
    ${env}=    Create Dictionary
    ...    SMTP_SERVER=192.168.1.7
    ...    SMTP_PORT=25
    ...    FROM_ADDR=sender@example.com
    ...    TO_ADDR=recipient@example.com
    ${result}=    Run Process    python    ${SMTP_SCRIPT_PATH}
    ...    env=${env}
    ...    timeout=30s
