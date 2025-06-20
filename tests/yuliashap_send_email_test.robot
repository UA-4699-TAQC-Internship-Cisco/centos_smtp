*** Settings ***
Library           OperatingSystem
Library           Collections
Library           String
Library           BuiltIn
Library           Process
Resource          ../resources/common/yuliashap_keywords.robot

Suite Setup       Setup Variables

*** Test Cases ***
Verify Email Delivery And Content
    ${before}=    Get Email Count
    Send Email
    ${after}=     Get Email Count
    Should Be True    ${after} == ${before} + 1    Email count should increase by 1
    ${last}=     Get Last Email
    Should Be Equal    ${last['from']}     ${SENDER}
    Should Be Equal    ${last['subject']}  ${EMAIL_SUBJECT}
    Should Contain     ${last['body']}     ${EMAIL_BODY}
