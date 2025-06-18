import os

import dotenv
import paramiko

dotenv.load_dotenv()


def read_emails(host, port, username, password, mail_file):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, port=port, username=username, password=password)

    _, stdout, _ = ssh.exec_command("cat {}".format(mail_file))
    content = stdout.read().decode('utf-8', 'ignore')

    for msg in content.split("From ")[1:]:
        lines = msg.strip().split("\n")
        frm = next((line[5:].strip() for line in lines if line.lower().startswith("from:")), "")
        subj = next((line[8:].strip() for line in lines if line.lower().startswith("subject:")), "")
        try:
            body = " ".join(lines[lines.index("") + 1:])[:100]
        except ValueError:
            body = ""

        print("From: {}\nSubject: {}\nBody snippet: {}\n{}".format(frm, subj, body, "-" * 40))

    ssh.close()


if __name__ == "__main__":
    read_emails(host=os.getenv("SSH_HOST"),
                port=int(os.getenv("SSH_PORT", 22)),
                username=os.getenv("SSH_USERNAME"),
                password=os.getenv("SSH_PASSWORD"),
                mail_file=os.getenv("EMAIL_DIR"))
