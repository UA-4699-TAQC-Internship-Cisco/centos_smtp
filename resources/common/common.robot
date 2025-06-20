*** Settings ***
Library    OperatingSystem
Library    ../scripts/isssaq_smtp.py

*** Keywords ***
Connect Smtp Server
    [Arguments]    ${HOST}    ${SMTP_PORT}=25
    ${SMTP_SRV}=    Connect Server    ${HOST}    ${SMTP_PORT}
    [Return]    ${SMTP_SRV}

Check Hostname
    [Arguments]    ${HOSTNAME}    ${SMTP_SRV}
    @{response}=    Validate Hostname    ${HOSTNAME}    ${SMTP_SRV}
    Should Be Equal    ${response}[0]    ${250}
    
Send Message Via Host
    [Arguments]    ${HOST}    ${FROM_ADDR}    ${TO_ADDR}    ${MESSAGE}    
    ${SMTP_SRV}=    Connect Server    ${HOST}
    Send Message Smtp    ${FROM_ADDR}    ${TO_ADDR}    ${MESSAGE}    ${SMTP_SRV}

Open Recent Mail
    [Arguments]    ${HOST}    ${username}    ${password}
    ${RECEIVED_MAIL}    Read Recent Mail    ${username}    ${password}    ${HOST}
    [Return]    ${RECEIVED_MAIL}