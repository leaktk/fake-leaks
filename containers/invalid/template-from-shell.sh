#! /bin/bash

tmp_config="$(mktemp)"
cat <<EOF > "${tmp_config}"
{
  "auths": {
    "registry.redhat.io": {
      "auth": "$(echo -n "${RH_REG_USR}:${RH_REG_PWD}" | base64 -w0)"
    }
  }
}
EOF
