*** Settings ***
Resource    resources/get_env.robot
Resource    resources/email_keywords.robot
Library     Collections
Test Setup  Load Environment Variables

*** Variables ***

${EMAIL_SUBJECT}    Test email
${EMAIL_BODY}       This is a test email body.



*** Test Cases ***
Test SMTP Connection
    Verify SMTP Connection

Send Test Email And Check Count
    ${count_before}=    Get Email Count
    Send Test Email
    Sleep    5s
    ${count_after}=     Get Email Count
    Verify Email Count Increased    ${count_before}    ${count_after}

Verify Email Contents
    Verify Last Email Contents

