# -*- coding:utf-8 -*-
'''
Title: Infrastructure NetworkAPI
Author: globo.com / TQI
Copyright: ( c )  2009 globo.com todos os direitos reservados.
'''

from networkapiclient.GenericClient import GenericClient
from networkapiclient.utils import get_list_map, is_valid_int_param
from networkapiclient.exception import InvalidParameterError


class Marca(GenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """
        super(Marca, self).__init__(networkapi_url, user, password, user_ldap)

    def listar(self):
        """List all Brand.

        :return: Dictionary with the following structure:

        ::

            {‘brand’: [{‘id’: < id >,
            ‘nome’: < nome >}, ... too Brands ...]}

        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        code, map = self.submit(None, 'GET', 'brand/all/')

        key = 'brand'
        return get_list_map(self.response(code, map, [key]), key)

    def inserir(self, name):
        """Inserts a new Brand and returns its identifier

        :param name: Brand name. String with a minimum 3 and maximum of 100 characters

        :return: Dictionary with the following structure:

        ::

            {'marca': {'id': < id_brand >}}

        :raise InvalidParameterError: Name is null and invalid.
        :raise NomeMarcaDuplicadoError: There is already a registered Brand with the value of name.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        brand_map = dict()
        brand_map['name'] = name

        code, xml = self.submit({'brand': brand_map}, 'POST', 'brand/')

        return self.response(code, xml)

    def alterar(self, id_brand, name):
        """Change Brand from by the identifier.

        :param id_brand: Identifier of the Brand. Integer value and greater than zero.
        :param name: Brand name. String with a minimum 3 and maximum of 100 characters

        :return: None

        :raise InvalidParameterError: The identifier of Brand or name is null and invalid.
        :raise NomeMarcaDuplicadoError: There is already a registered Brand with the value of name.
        :raise MarcaNaoExisteError: Brand not registered.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_brand):
            raise InvalidParameterError(
                u'The identifier of Brand is invalid or was not informed.')

        url = 'brand/' + str(id_brand) + '/'

        brand_map = dict()
        brand_map['name'] = name

        code, xml = self.submit({'brand': brand_map}, 'PUT', url)

        return self.response(code, xml)

    def remover(self, id_brand):
        """Remove Brand from by the identifier.

        :param id_brand: Identifier of the Brand. Integer value and greater than zero.

        :return: None

        :raise InvalidParameterError: The identifier of Brand is null and invalid.
        :raise MarcaNaoExisteError: Brand not registered.
        :raise MarcaError: The brand is associated with a model.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_brand):
            raise InvalidParameterError(
                u'The identifier of Brand is invalid or was not informed.')

        url = 'brand/' + str(id_brand) + '/'

        code, xml = self.submit(None, 'DELETE', url)

        return self.response(code, xml)
