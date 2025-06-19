import smtplib


def send_mail(host, port, from_addr, to_addrs, body, subject=None):
    """
    :param host:
    :param port:
    :param from_addr:
    :param to_addrs:
    :param body:
    :param subject:
    :return:
    """
    lines = [
        "From: {}".format(from_addr),
        "To: {}".format(', '.join(to_addrs)),
        "Subject: {}".format(subject),
        "",
        body
    ]

    msg = "\r\n".join(lines)

    server = smtplib.SMTP(host, port)
    server.set_debuglevel(1)
    server.sendmail(from_addr, to_addrs, msg)
    server.quit()
