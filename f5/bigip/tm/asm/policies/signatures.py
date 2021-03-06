# coding=utf-8
#
# Copyright 2017 F5 Networks Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from f5.bigip.resource import AsmResource
from f5.bigip.resource import Collection
from f5.sdk_exception import UnsupportedOperation


class Signatures_s(Collection):
    """BIG-IP® ASM Signatures sub-collection."""
    def __init__(self, policy):
        super(Signatures_s, self).__init__(policy)
        self._meta_data['object_has_stats'] = False
        self._meta_data['allowed_lazy_attributes'] = [Signature]
        self._meta_data['required_json_kind'] = 'tm:asm:policies:signatures:signaturecollectionstate'
        self._meta_data['attribute_registry'] = {
            'tm:asm:policies:signatures:signaturestate': Signature
        }


class Signature(AsmResource):
    """BIG-IP® ASM Signature resource."""
    def __init__(self, signatures_s):
        super(Signature, self).__init__(signatures_s)
        self._meta_data['required_json_kind'] = 'tm:asm:policies:signatures:signaturestate'

    def create(self, **kwargs):
        """Create is not supported for Signature resources

        :raises: UnsupportedOperation
        """
        raise UnsupportedOperation(
            "%s does not support the create method" % self.__class__.__name__
        )

    def delete(self, **kwargs):
        """Delete is not supported for Signature resources

        :raises: UnsupportedOperation
        """
        raise UnsupportedOperation(
            "%s does not support the delete method" % self.__class__.__name__
        )
