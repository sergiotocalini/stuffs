#!/usr/bin/env sh

APP_DIR=$(dirname $0)
if [[ ${APP_DIR} == "." ]];then
    APP_DIR=$(pwd)
fi

DOCROOT="~/cdn/nexus-amana.com/cdn/avatar"
LDAP_JPG="${APP_DIR}/ldap_jpegPhoto.py"
SYNC_DIR="${APP_DIR}/syncdir"
REQUIRED=( "${APP_DIR}/index.php" "${APP_DIR}/.htaccess" "${APP_DIR}/default.jpg" )

mkdir ${SYNC_DIR}
cd ${SYNC_DIR}
${LDAP_JPG}

#for i in $(dnsquery -d internal -s 172.25.2.10 -r "web[0-9,].*hon.ar.*" -f host); do
#    rsync --delete -o apache -g apache -avzc -P ${REQUIRED[@]} ${SYNC_DIR}/* root@${i}:${DOCROOT}/
    # ssh -q root@${i} "chmod -R 775 ${DOCROOT}"
    # ssh -q root@${i} "chmod -R g+s ${DOCROOT}"
#done
#rm -Rf ${SYNC_DIR}
