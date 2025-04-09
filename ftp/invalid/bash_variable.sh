# https://github.com/srvrco/getssl/blob/b7919d6341f5c81bd0cc7024695ae894b933ad4d/getssl#L1104

      SFTP_PORT="";
      if [ -n "$FTP_PORT" ]; then SFTP_PORT=":${FTP_PORT}"; fi
      debug "${to:0:5} user=$ftpuser - pass=$ftppass - host=$ftphost port=$FTP_PORT dir=$ftpdirn file=$ftpfile"
      debug "from dir=$fromdir  file=$fromfile"
      if [[ "${to:0:5}" == "ftps:" ]] ; then
        # if no FTP_PORT is specified, then use default
        if [ -z "$FTP_PORT" ]; then
          SFTP_PORT=":990"
        fi
        # shellcheck disable=SC2086
        debug curl ${_NOMETER} $FTPS_OPTIONS --ftp-ssl --ftp-ssl-reqd -u "${ftpuser}:${ftppass}" -T "${fromdir}/${fromfile}" "ftps://${ftphost}${SFTP_PORT}/${ftpdirn}/"
        # shellcheck disable=SC2086
        curl ${_NOMETER} $FTPS_OPTIONS --ftp-ssl-reqd -u "${ftpuser}:${ftppass}" -T "${fromdir}/${fromfile}" "ftps://${ftphost}${SFTP_PORT}/${ftpdirn}/"
      else
        # shellcheck disable=SC2086
        debug curl ${_NOMETER} $FTPS_OPTIONS --ftp-ssl --ftp-ssl-reqd -u "${ftpuser}:${ftppass}" -T "${fromdir}/${fromfile}" "ftp://${ftphost}${SFTP_PORT}/${ftpdirn}/"
        # shellcheck disable=SC2086
        curl ${_NOMETER} $FTPS_OPTIONS --ftp-ssl-reqd -u "${ftpuser}:${ftppass}" -T "${fromdir}/${fromfile}" "ftp://${ftphost}${SFTP_PORT}/${ftpdirn}/"
      fi
