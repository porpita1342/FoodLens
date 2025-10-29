docker run -it --name TorchTest --shm_size=4g --mount type=bind,src=$(pwd),dst=/app --gpus all 1b29f8187294 bash


