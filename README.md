# ansible-cisco-type-5 lookup plugin

Ansible lookup plugin to confirm that a type 5 encrypted password is set to what
the user expects.  


Sample Usage:


```
---
- name: common
  tags: common
  become: no
  gather_facts: no
  hosts: localhost
  connection: local
  tasks:
    - name: Check if password is correct
      set_fact:
        pw_correct: "{{ lookup('cisco_type_5', 'cisco', '$1$2ZW8$ADFVs6Pb0zP.r2mr6FgZs1') }}"

    - name: Debug Info
      debug:
        msg: "{{ pw_correct }}"

    - name: Change password
      debug:
        msg: "need to change password"
      when: pw_correct == false

```

# Installation

You can activate a custom lookup by either dropping it into a lookup_plugins directory adjacent to your play, inside a role, or by putting it in one of the lookup directory sources configured in ansible.cfg.


For more information:

https://docs.ansible.com/ansible/2.5/plugins/lookup.html#enabling-lookup-plugins
