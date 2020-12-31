#!/bin/bash

CMD=$1
# DECODE
if [[ $CMD == *"ch1_v_s"]];then
	ch1_v=`echo "$CMD" | sed -n 's/^.*ch1_v=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
fi

ch1_v=`echo "$CMD" | sed -n 's/^.*ch1_v=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`

# ENCODE & SEND
