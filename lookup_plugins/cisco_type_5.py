from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
from ansible.plugins.lookup import LookupBase
from passlib.hash import md5_crypt


EXAMPLES = """
- name: return fabric node id
  set_fact:
    cisco_type_5: "{{ lookup('cisco', '$1$2ZW8$ADFVs6Pb0zP.r2mr6FgZs1' }}"

"""

RETURN = """
  boolean:
    description: True if hash matches expected password
"""


class LookupModule(LookupBase):

    def run(self, args, variables=None, **kwargs):
        expected_pw = args[0]
        hash = args[1]
        return [md5_crypt.verify(expected_pw, hash)]
