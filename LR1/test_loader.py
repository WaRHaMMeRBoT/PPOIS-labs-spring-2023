import subprocess
from unittest import TestCase


class Test(TestCase):
    def test_my_code(self):
        p = subprocess.Popen(["python", "-m", "unittest", "test_main"], stdin=subprocess.PIPE)

        p.stdin.write(b"sd\n")
        p.stdin.flush()

        p.communicate()
