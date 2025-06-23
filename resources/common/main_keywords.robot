*** Settings ***
Library    OperatingSystem

*** Keywords ***
Load Environment Variables
    ${HOST}=    Get Environment Variable    HOSTNAME
    ${PORT}=    Get Environment Variable    SMTP_PORT
    ${PORT_INT}=    Evaluate    int(${PORT})
    ${USER}=    Get Environment Variable    SSH_USERNAME
    ${PASS}=    Get Environment Variable    PASSWORD

    Set Suite Variable    ${HOST}
    Set Suite Variable    ${PORT_INT}
    Set Suite Variable    ${USER}
    Set Suite Variable    ${PASS}

Count Emails
    [Arguments]    ${mail_output}
    ${lines}=    Evaluate    '''${mail_output}.split("\\n")'''
    ${count}=    Evaluate    '''sum(1 for line in """${mail_output}""".splitlines() if line.startswith("From "))'''
    [Return]    ${count}



