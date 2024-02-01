from models.engine.file_storage import FileStorage
import unittest


storage = FileStorage()


class TestFileStore(unittest.TestCase):
    """test the filestore class"""

    def test_all(self):
        """ test the all method"""
        r = storage.all()
        self.assertEqual(type(r), type({}))

    def test_new(self):
        """ test new method """
        pass

    def test_save(self):
        """ test the save method """
        pass

class TestReload(unittest.TestCase):
    """ rest reload method"""
    def test_reload(self):
        """ test reload method """
        print('ira')
