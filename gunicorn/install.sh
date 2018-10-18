#!/usr/bin/env ksh
SOURCE_DIR=$(dirname $0)

GUNICORN_DAEMON="${1:-/usr/bin/gunicorn}"
GUNICORN_DIR="${2:-/etc/gunicorn}"
GUNICORN_LOG="${3:-/var/log/gunicorn}"
GUNICORN_RUN="${4:-/var/run/gunicorn}"
VIRTUALENV_PATH="${5:-/etc/gunicorn/venvs}"
RUNS_AS="${6:-python}"

mkdir -p ${GUNICORN_DIR}
mkdir -p ${GUNICORN_DIR}/conf.d

SCRIPT_CONFIG="${DEPLOY_DIR}/gunicorn.conf"
[[ -f ${SCRIPT_CONFIG} ]] && SCRIPT_CONFIG="${SCRIPT_CONFIG}.new"

cp -rp ${SOURCE_DIR}/etc/gunicorn/gunicorn.conf               ${SCRIPT_CONFIG}
cp -rp ${SOURCE_DIR}/etc/gunicorn/conf.d/example.json.save    ${GUNICORN_DIR}/conf.d/example.json.save
cp -rp ${SOURCE_DIR}/etc/init.d/gunicorn                      /etc/init.d/gunicorn

chown -R root: /etc/gunicorn /etc/init.d/gunicorn
chmod -R 755   /etc/gunicorn /etc/init.d/gunicorn

regex_array[0]="s|GUNICORN_DAEMON=.*|GUNICORN_DAEMON=\"${GUNICORN_DAEMON}\"|g"
regex_array[1]="s|GUNICORN_DIR=.*|GUNICORN_DIR=\"${GUNICORN_DIR}\"|g"
regex_array[2]="s|GUNICORN_LOG=.*|GUNICORN_LOG=\"${GUNICORN_LOG}\"|g"
regex_array[3]="s|GUNICORN_RUN=.*|GUNICORN_RUN=\"${GUNICORN_RUN}\"|g"
regex_array[4]="s|VIRTUALENV_PATH=.*|VIRTUALENV_PATH=\"${VIRTUALENV_PATH}\"|g"
regex_array[5]="s|RUN_AS=.*|RUN_AS=\"${RUN_AS}\"|g"
for index in ${!regex_array[*]}; do
    sed -i "${regex_array[${index}]}" ${SCRIPT_CONFIG}
done

if [[ ${SCRIPT_CONFIG} =~ .*.new$ ]]; then
    if diff ${SCRIPT_CONFIG} ${SCRIPT_CONFIG%.new} > /dev/null; then
	rm ${SCRIPT_CONFIG}
    fi
fi

