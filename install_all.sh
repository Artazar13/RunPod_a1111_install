#!/bin/bash

fuser -k 3000/tcp

# Update package lists
apt update

python download_models.py

python download_ip_adapter_and_instantid.py

python control_net_downloader.py

source install_latest_auto_1111.sh

cd /workspace

source install_tensorRT.sh

python relauncher.py