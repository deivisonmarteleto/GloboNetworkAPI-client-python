# -*- coding:utf-8 -*-
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from networkapiclient.ApiGenericClient import ApiGenericClient
from utils import build_uri_with_ids


class ApiIpv6(ApiGenericClient):
    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """

        super(ApiIpv6, self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap
        )

    def search(self, **kwargs):
        """
        Method to search ipv6's based on extends search.

        :param search: Dict containing QuerySets to find ipv6's.
        :param include: Array containing fields to include on response.
        :param exclude: Array containing fields to exclude on response.
        :param fields:  Array containing fields to override default fields.
        :param kind: Determine if result will be detailed ('detail') or basic ('basic').
        :return: Dict containing ipv6's
        """

        return super(ApiIpv6, self).get(self.prepare_url("api/v3/ipv6/",
                                                         kwargs))

    def get(self, ids, **kwargs):
        """
        Method to get ipv6's by their ids

        :param ids: List containing identifiers of ipv6's
        :param include: Array containing fields to include on response.
        :param exclude: Array containing fields to exclude on response.
        :param fields: Array containing fields to override default fields.
        :param kind: Determine if result will be detailed ('detail') or basic ('basic').
        :return: Dict containing ipv6's
        """
        url = build_uri_with_ids("api/v3/ipv6/%s/", ids)
        return super(ApiIpv6, self).get(self.prepare_url(url, kwargs))

    def delete(self, ids):
        """
        Method to delete ipv6's by their ids

        :param ids: Identifiers of ipv6's
        :return: None
        """
        url = build_uri_with_ids("api/v3/ipv6/%s/", ids)
        return super(ApiIpv6, self).delete(url)

    def update(self, ipv6s):
        """
        Method to update ipv6's

        :param ipv6s: List containing ipv6's desired to updated
        :return: None
        """

        data = {'ipv6s': ipv6s}
        ipv6s_ids = [str(ipv6.get("id")) for ipv6 in ipv6s]

        return super(ApiIpv6, self).put("api/v3/ipv6/%s/" %
                                        ';'.join(ipv6s_ids), data)

    def create(self, ipv6s):
        """
        Method to create ipv6's

        :param ipv6s: List containing vrf desired to be created on database
        :return: None
        """

        data = {'ipv6s': ipv6s}
        return super(ApiIpv6, self).post("api/v3/ipv6/", data)
