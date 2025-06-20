*** Settings ***
Resource    ../resources/common/common.robot
Library    OperatingSystem
Library    ../resources/scripts/isssaq_smtp.py

*** Variables ***
${message}    "Hello, this is a test from local"

*** Test Cases ***
Set Connection And Check Hostname
    ${HOST}=    Get Environment Variable    HOST
    ${HOSTNAME}=      Get Environment Variable    HOSTNAME
    ${SMTP}=    Connect Smtp Server    ${HOST}    25
    Check Hostname    ${HOSTNAME}    ${SMTP}

Check That Mail Is Sent
    ${HOST}=    Get Environment Variable    HOST
    ${SENDER}=    Get Environment Variable    FROM_ADDR
    ${RECIPIENT}=    Get Environment Variable    TO_ADDR
    ${user}=    Get Environment Variable    VBOX_USER
    ${password}=    Get Environment Variable    password

    Send Message Via Host    ${HOST}    ${SENDER}    ${RECIPIENT}    ${message}
    ${SENT_MAIL}=    Open Recent Mail    ${HOST}     ${user}    ${password}
    Should Contain    ${SENT_MAIL}    ${message}


