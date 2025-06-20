*** Settings ***
Resource    ../resources/common/main_keywords.robot
Library    ../resources/scripts/tyakushevych_send_read_mail.py


*** Variables ***
${FROM}       root@localhost
${TO}         user1@localhost
${SUBJECT}    Test subject
${BODY}       Mail after robot tests


*** Test Cases ***
Email Is Sent Successfully
    Load Environment Variables

    ${result}=    Send Mail    ${HOST}    ${PORT_INT}    ${FROM}    ${TO}    ${BODY}    ${SUBJECT}
    Should Be Equal As Strings    ${result}    {}


Email Count Increases After Sending Mail
    Load Environment Variables


    ${before}=    Read Mail    ${HOST}    ${USER}    ${PASS}
    ${count_before}=    Count Emails    ${before}

    Send Mail    ${HOST}    ${PORT_INT}    ${FROM}    ${TO}    ${BODY}    ${SUBJECT}

    ${after}=    Read Mail    ${HOST}    ${USER}    ${PASS}
    ${count_after}=    Count Emails    ${after}

    Should Be True    ${count_after} > ${count_before}

