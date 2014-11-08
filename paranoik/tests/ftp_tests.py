import unittest
import mock

from paranoik.storage.ftp import FTP


class FTPTests(unittest.TestCase):
    @mock.patch("ftplib.FTP")
    def test_ftp(self, ftplib_ftp):
        with mock.patch("builtins.open", mock.mock_open()) as mock_open:
            ftp = FTP("localhost", "test", "password")
            ftp.add_file("/path/to/some/file")
            ftp.close()
            self.assertTrue(ftplib_ftp.called)


if __name__ == "__main__":
    unittest.main()