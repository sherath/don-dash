#!/bin/sh
/opt/cloudpassage/bin/cphalo --agent-key=$HALO_AGENT_KEY --tag=$SERVER_GROUP --server-label="don-dash" 2>&1 >/dev/null &

python -m flask run --host=0.0.0.0
