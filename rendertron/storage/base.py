from rendertron.utils import import_string, dict_merge


class RendertronStorage:
    def __init__(self, options):
        """
        :param dict options: The storage options
        """
        self.options = options

    @staticmethod
    def get_default_options():
        """
        Returns the default options for this storage.
        :rtype: dict
        """
        raise NotImplementedError  # pragma: no cover

    def get_stored_response(self, request):
        """
        Returns a stored response if any.
        :param request: The request object. Varies per framework.
        :returns: The stored response or None if there isn't any.
        """
        raise NotImplementedError  # pragma: no cover

    def store_response(self, request, response, meta):
        """
        Stores the response for the given request.
        :param request: The request object. Varies per framework.
        :param str|bytes response:
        :param dict meta: Meta data of the response
        :return:
        """
        raise NotImplementedError  # pragma: no cover


def get_storage(storage_settings):
    """
    Imports and initializes the storage class defined in the given settings and
    returns it's instance.
    :param dict storage_settings: Settings dictionary.
    :return: The storage class instance.
    :rtype: RendertronStorage
    """
    storage_class_path = storage_settings["CLASS"]
    storage_class = import_string(storage_class_path)

    storage_options = dict_merge(
        storage_class.get_default_options(), storage_settings.get("OPTIONS", {})
    )
    return storage_class(storage_options)
