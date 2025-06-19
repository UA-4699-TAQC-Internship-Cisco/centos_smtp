*** Settings ***
Library    ../TYakushevych_smtp/send_read_mail.py


*** Variables ***
${HOST}       192.168.1.43
${PORT}       25
${USER}       user1
${PASS}       Test12345
${FROM}       root@localhost
${TO}         user1@localhost
${SUBJECT}    Test subject
${BODY}       Mail after robot tests

*** Test Cases ***
Email Is Sent Successfully
    ${result}=    Send Mail    ${HOST}    ${PORT}    ${FROM}    ${TO}    ${BODY}    ${SUBJECT}
    Should Be Equal As Strings    ${result}    {}

Email Count Increases After Sending Mail
    ${before}=    Read Mail    ${HOST}    ${USER}    ${PASS}
    ${count_before}=    Count Emails    ${before}

    Send Mail    ${HOST}    ${PORT}    ${FROM}    ${TO}    ${BODY}    ${SUBJECT}

    ${after}=    Read Mail    ${HOST}    ${USER}    ${PASS}
    ${count_after}=    Count Emails    ${after}

    Should Be True    ${count_after} > ${count_before}

*** Keywords ***
Count Emails
    [Arguments]    ${mail_output}
    ${lines}=    Evaluate    '''${mail_output}.split("\\n")'''
    ${count}=    Evaluate    '''sum(1 for line in """${mail_output}""".splitlines() if line.startswith("From "))'''
    [Return]    ${count}
