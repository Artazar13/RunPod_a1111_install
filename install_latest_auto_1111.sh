#!/bin/bash

fuser -k 3000/tcp

# Update package lists
apt update

cd /workspace/stable-diffusion-webui/extensions/sd-webui-controlnet

git pull

cd /workspace/stable-diffusion-webui/extensions/deforum

git pull

cd /workspace/stable-diffusion-webui/extensions

git clone https://github.com/Gourieff/sd-webui-reactor

git clone https://github.com/Bing-su/adetailer

cd /workspace/stable-diffusion-webui

git stash

git checkout master

git pull

cd /workspace

source venv/bin/activate

pip install --upgrade albumentations==1.4.2

pip install --upgrade pydantic==1.10.14

pip install insightface

pip3 install torch==2.3.0 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 --upgrade

pip install xformers==0.0.26.post1 --upgrade

pip uninstall torchaudio --yes

cd /workspace/stable-diffusion-webui

# git checkout dev

rm -r webui-user.sh

wget -O /workspace/stable-diffusion-webui/webui-user.sh https://huggingface.co/MonsterMMORPG/SECourses/raw/main/webui-user-v2.sh

cd /workspace/stable-diffusion-webui

wget https://huggingface.co/MonsterMMORPG/SECourses/resolve/main/styles.csv -O styles.csv