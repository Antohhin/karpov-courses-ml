import re
from typing import List
import time


def valid_emails(strings: List[str]) -> List[str]:
    """Take list of potential emails and returns only valid ones"""

    # valid_email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    valid_email_regex = r"^[\w+?]+?@[\w+?]+?\.[\w+?]+?$"

    def is_valid_email(email: str) -> bool:
        return bool(re.fullmatch(valid_email_regex, email))

    emails = []
    for email in strings:
        if is_valid_email(email):
            emails.append(email)

    return emails


if __name__ == '__main__':
    start = time.time()
    v = valid_emails(['cffssffsv', 'sffsafg@.', 'sfawfgaf@mail.ru',
                       'ffgsaggasgg@224ma.com', '2r2f23f3f!7&@com.com'])
    end = time.time()
    print((end - start) * 1000)
