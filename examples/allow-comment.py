SECRET_KEY = "uxJcj20y@s%kvfhjc4#&ira)g(isr-ee0wqr18wr)(s0k^3g%k" # notsecret


- name: Retrieve an approle role ID
  ansible.builtin.debug:
  msg: >-
    {{
      lookup(
        'community.hashi_vault.vault_read',
        'auth/approle/role/role-name/role-id',
        url='https://vault:8201',
        secret_id='dd3cf500-f9f9-4052-a768-1f22ac57d107',
      )
    }}"
