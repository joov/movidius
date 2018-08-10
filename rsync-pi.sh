#!/bin/bash -e
#
# Copyright (c) 2018 Chen-Ting Chuang
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

PROGNAME="$(basename "$0")"

if [[ $(uname) == "Darwin" ]]; then
  GETOPT="/usr/local/opt/gnu-getopt/bin/getopt"
  if [[ ! -x "${GETOPT}" ]]; then
    echo "Error: cannot find gnu-getopt"
    echo "$ brew install gnu-getopt"
    exit 1
  fi
  RSYNC="/usr/local/bin/rsync"
  if [[ ! -x "${RSYNC}" ]]; then
    echo "Error: cannot find Homebrew rsync"
    echo "$ brew install rsync"
    exit 1
  fi
else
  GETOPT="getopt"
  RSYNC="rsync"
fi

OPTS=$("${GETOPT}" -o c:s:dh -l code:,host:,delete,help -n "${PROGNAME}" -- "$@")

if [ $? != 0 ] ; then echo "Failed parsing options." >&2 ; exit 1 ; fi

eval set -- "$OPTS"

declare -a HOSTS=()
CODE=
HELP=false
REMOTE_PATH=/home/pi/yolo3-camera

while true; do
    case "$1" in
        -h | --help ) HELP=true; shift ;;
        -c | --code ) CODE="$2"; shift; shift ;;
        -s | --host ) HOSTS=("${HOSTS[@]}" "$2"); shift; shift ;;
        -d | --delete ) EXTRA_RSYNC_OPTION="${EXTRA_RSYNC_OPTION} --delete"; shift ;;
        -- ) shift; break ;;
        * ) break ;;
    esac
done

if [ $HELP = true ]; then
    cat <<EOF

${PROGNAME} [OPTIONS]

       -h, --help
               Show this help

       -c, --code     [CODE_PATH]
               Specify local code path of yolo3-camera.

       -s, --host     [HOSTNAME]
               Specify SSH hostname.
               You can specify this option more than once to 
               deploy multiple hosts.

       -d, --delete
               Enable --delete rsync option (use with caution).

This script will rsync CODE_PATH into HOSTNAME:${REMOTE_PATH}.

You need add your Raspberry Pi in ~/.ssh/config first.

Example ~/.ssh/config:

	Host pi
	HostName 192.168.1.102
	User pi

Example command:

	\$ ${PROGNAME} -c ~/Code/yolo3-camera -s pi

EOF
    exit 0
fi

if [[ -z "${CODE}" ]]; then
    echo "${PROGNAME}: --code argument is missing." >&2
    exit 1
fi

if [ ${#HOSTS[@]} -eq 0 ]; then
    echo "${PROGNAME}: --host argument is missing." >&2
    exit 1
fi

# rsync acts differently with and without trailing slash.
# We always append trailing slash.
CODE=$(echo $CODE | sed 's#\/*$#\/#g')

echo CODE=$CODE
echo HOSTS="${HOSTS[@]}"
echo REMOTE_PATH=$REMOTE_PATH
echo

for HOST in "${HOSTS[@]}"
do
  echo ================================================
  echo "[${HOST}]"

  "$RSYNC" -ave ssh \
        --exclude '.*' --exclude 'TAGS' \
        --exclude '*.pyc' --exclude '__pycache__' \
        --exclude '*.so' --exclude '*.a' --exclude '*.o' \
        "${CODE}" "${HOST}:${DEST_PATH}"
done
