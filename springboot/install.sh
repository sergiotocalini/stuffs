#!/usr/bin/env ksh
SOURCE_DIR=$(dirname $0)

SPRING_DIR="${1:-/etc/springboot}"
SPRING_LOG="${2:-/var/log/springboot}"
SPRING_RUN="${3:-/var/run/springboot}"

mkdir -p ${SPRING_DIR}
mkdir -p ${SPRING_DIR}/conf.d

SCRIPT_CONFIG="${SPRING_DIR}/springboot.conf"
[[ -f ${SCRIPT_CONFIG} ]] && SCRIPT_CONFIG="${SCRIPT_CONFIG}.new"

cp -rp ${SOURCE_DIR}/etc/springboot/springboot.conf             ${SCRIPT_CONFIG}
cp -rp ${SOURCE_DIR}/etc/springboot/conf.d/example.json.save    ${SPRING_DIR}/conf.d/example.json.save
cp -rp ${SOURCE_DIR}/etc/init.d/springboot                      /etc/init.d/springboot

chown -R root: /etc/springboot /etc/init.d/springboot
chmod -R 755   /etc/springboot /etc/init.d/springboot

regex_array[0]="s|SPRING_DIR=.*|SPRING_DIR=\"${SPRING_DIR}\"|g"
regex_array[1]="s|SPRING_LOG=.*|SPRING_LOG=\"${SPRING_LOG}\"|g"
regex_array[2]="s|SPRING_RUN=.*|SPRING_RUN=\"${SPRING_RUN}\"|g"
for index in ${!regex_array[*]}; do
    sed -i "${regex_array[${index}]}" ${SCRIPT_CONFIG}
done

if [[ ${SCRIPT_CONFIG} =~ .*.new$ ]]; then
    if diff ${SCRIPT_CONFIG} ${SCRIPT_CONFIG%.new} > /dev/null; then
	rm ${SCRIPT_CONFIG}
    fi
fi

