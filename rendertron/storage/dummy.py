from rendertron.storage.base import RendertronStorage


class DummyStorage(RendertronStorage):
    """ A dummy storage that does not store anything. """

    @staticmethod
    def get_default_options():
        return {}

    def get_stored_response(self, *args):
        return None, None

    def store_response(self, *args):
        pass
