from tmdbv3api.tmdb import TMDb
from tmdbv3api.as_obj import AsObj
from tmdbv3api.endpoints import Endpoint

try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote


class Person(TMDb):
    def get_by_id(self, id):
        """
        Get the primary person details by id.
        :param id:
        :return:
        """
        return AsObj(**self._call(Endpoint.PERSON % str(id), ''))

    def search(self, term, page=1):
        """
        Search for people.
        :param term:
        :param page:
        :return:
        """
        return self._get_obj(self._call(Endpoint.SEARCH_PERSON, 'query=' + quote(term) + '&page=' + str(page)))