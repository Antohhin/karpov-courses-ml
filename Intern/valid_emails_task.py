"""
Код работает корректно и полностью решает задачу, однако когда ваш TeamLead ревьюил код,
 то оставил комментарий, что его можно ускорить минимум в 2 раза, буквально поменяв две
   строчки. Однако он не сказал, как – лишь оставил ссылку на страницу про регулярные выражения
     в Python в качестве подсказки. 
"""
# how to measure time: python3 -m timeit -n 20 -r 5 -s 'import os' 'os.system("python 00_naive.py")'


import re
from typing import List


def valid_emails(strings: List[str]) -> List[str]:
    """Take list of potential emails and returns only valid ones"""

    # valid_email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    valid_email_regex = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

    def is_valid_email(email: str) -> bool:
        return bool(re.fullmatch(valid_email_regex, email))

    # emails = []
    # for email in strings:
    #     if is_valid_email(email):
    #         emails.append(email)
    emails = list(filter(is_valid_email, strings))

    return emails

if __name__ == '__main__':
    test_emails = ['x', 'xyz', 'x@y.z', 'x.y@z', 'xy@z', 'xy@.z', 'xy@z.']
    valid_emails(test_emails)
    