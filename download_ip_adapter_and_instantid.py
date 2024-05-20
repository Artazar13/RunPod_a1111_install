import os
import requests
import time

def download_file(url, path, filename, retries=9, timeout=120):
    """
    Download a file from a given URL and save it to the specified path with resume support.

    Parameters:
    - url (str): URL of the file to be downloaded.
    - path (str): Directory where the file will be saved.
    - filename (str): Name of the file to be saved.
    - retries (int): Number of retries if the download fails. Default is 9.
    - timeout (int): Timeout for the download request in seconds. Default is 120.
    """

    # Create the directory if it does not exist
    os.makedirs(path, exist_ok=True)

    file_path = os.path.join(path, filename)
    print(f"\nDownloading {filename} to {file_path}")

    try:
        with requests.get(url, stream=True, timeout=timeout) as response:
            response.raise_for_status()
            total_size = int(response.headers.get('content-length', 0))
            block_size = 2048576  # 2 MB

            with open(file_path, 'wb') as file:
                start_time = time.time()
                for data in response.iter_content(block_size):
                    file.write(data)
                    downloaded_size = file.tell()
                    elapsed_time = time.time() - start_time
                    download_speed = downloaded_size / elapsed_time / 1024  # Speed in KiB/s

                    # Display download progress and speed
                    progress = (downloaded_size / total_size) * 100
                    print(f"Downloaded {downloaded_size}/{total_size} bytes "
                          f"({progress:.2f}%) at {download_speed:.2f} KiB/s", end='\r')

        print(f"\nDownload completed: {filename}")
        return file_path

    except requests.RequestException as e:
        if retries > 0:
            print(f"\nError occurred: {e}. Retrying...")
            return download_file(url, path, filename, retries=retries-1, timeout=timeout)
        else:
            print("\nDownload failed after multiple retries.")
            return None

# Example usage
download_file('https://huggingface.co/h94/IP-Adapter-FaceID/resolve/main/ip-adapter-faceid-plusv2_sd15_lora.safetensors',
              'stable-diffusion-webui/models/Lora',
              'ip-adapter-faceid-plusv2_sd15_lora.safetensors')

download_file('https://huggingface.co/h94/IP-Adapter-FaceID/resolve/main/ip-adapter-faceid-plusv2_sdxl_lora.safetensors',
              'stable-diffusion-webui/models/Lora',
              'ip-adapter-faceid-plusv2_sdxl_lora.safetensors')

download_file('https://huggingface.co/InstantX/InstantID/resolve/main/ip-adapter.bin',
              'stable-diffusion-webui/models/ControlNet',
              'ip-adapter_instant_id_sdxl.bin')

download_file('https://huggingface.co/InstantX/InstantID/resolve/main/ControlNetModel/diffusion_pytorch_model.safetensors',
              'stable-diffusion-webui/models/ControlNet',
              'control_instant_id_sdxl.safetensors')
