import os
import platform
import requests
import time
import zipfile

def download_file(url, base_path, sub_path, filename, retries=9, timeout=120):
    """
    Download a file from a given URL and save it to the specified path with resume support.

    Parameters:
    - url (str): URL of the file to be downloaded.
    - base_path (str): Base directory where the file will be saved.
    - sub_path (str): Subdirectory under the base directory where the file will be saved.
    - filename (str): Name of the file to be saved.
    - retries (int): Number of retries if the download fails. Default is 3.
    - timeout (int): Timeout for the download request in seconds. Default is 10.
    """

    print(f"\nDownloading {filename}!")
    # Construct the full file path using os.path.join
    file_path = os.path.join(base_path, sub_path, filename)

    downloaded_size = 0
    if os.path.exists(file_path):
        downloaded_size = os.path.getsize(file_path)

    headers = {}
    if downloaded_size:
        headers['Range'] = f"bytes={downloaded_size}-"

    try:
        response = requests.get(url, headers=headers, stream=True, timeout=timeout)
        response.raise_for_status()

        total_size = downloaded_size + int(response.headers.get('content-length', 0))

        block_size = 2048576  # 1 MB

        with open(file_path, 'ab') as file:
            start_time = time.time()
            for data in response.iter_content(block_size):
                file.write(data)

                downloaded_size += len(data)
                elapsed_time = time.time() - start_time
                download_speed = downloaded_size / elapsed_time / 1024  # Speed in KiB/s

                # Display download progress and speed
                progress = (downloaded_size / total_size) * 100
                print(f"Downloaded {downloaded_size}/{total_size} bytes "
                      f"({progress:.2f}%) at {download_speed:.2f} KiB/s", end='\r')

        print(f"\nDownload completed {filename}!")
        return file_path

    except requests.RequestException as e:
        if retries > 0:
            print(f"Error occurred: {e}. Retrying...")
            return download_file(url, base_path, sub_path, filename, retries=retries-1, timeout=timeout)
        else:
            print("Download failed after multiple retries.")
            return None


download_file('https://huggingface.co/SG161222/Realistic_Vision_V6.0_B1_noVAE/resolve/main/Realistic_Vision_V6.0_NV_B1.safetensors',
              'stable-diffusion-webui', 'models/Stable-diffusion', 'Realistic_Vision_6.0.safetensors')
download_file('https://huggingface.co/madebyollin/sdxl-vae-fp16-fix/resolve/main/sdxl_vae.safetensors',
              'stable-diffusion-webui', 'models/VAE', 'sd_xl_base_1.0.safetensors')
download_file('https://huggingface.co/SG161222/RealVisXL_V4.0/resolve/main/RealVisXL_V4.0.safetensors',
              'stable-diffusion-webui', 'models/Stable-diffusion', 'RealVisXL_V4.safetensors')
download_file('https://huggingface.co/MonsterMMORPG/Stable-Diffusion/resolve/main/best_realism.safetensors',
              'stable-diffusion-webui', 'models/Stable-diffusion', 'Hyper_Realism_V3.safetensors')
