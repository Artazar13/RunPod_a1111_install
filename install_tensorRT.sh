fuser -k 3000/tcp

# Update package lists
apt update

cd /workspace/stable-diffusion-webui/extensions/sd-webui-controlnet

git pull

cd /workspace/stable-diffusion-webui/extensions/deforum

git pull

cd ..

rm -r Stable-Diffusion-WebUI-TensorRT

git clone https://github.com/andrewtvuong/Stable-Diffusion-WebUI-TensorRT

cd /workspace/stable-diffusion-webui

wget https://huggingface.co/MonsterMMORPG/SECourses/resolve/main/styles.csv -O styles.csv

# we have to checkout dev for SDXL TensorRT to work at the moment

git pull

cd /workspace/stable-diffusion-webui

git stash

git checkout master

git pull

rm -r webui-user.sh

wget -O /workspace/stable-diffusion-webui/webui-user.sh https://huggingface.co/MonsterMMORPG/SECourses/raw/main/webui-user-v2.sh

cd /workspace

source venv/bin/activate

pip install --upgrade albumentations==1.4.2

pip install --upgrade pydantic==1.10.14

pip install insightface

cd /workspace/stable-diffusion-webui