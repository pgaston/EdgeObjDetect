# Docker for EdgeObjDetect

## For colab

Start docker, noting the mapping of the local Documents folder
and a 'data' folder to the docker environment - for easy access to your data and other files.

`
docker run --gpus=all  \
	-p 127.0.0.1:9000:8080 \
	-v ~/Documents:/Documents \
	-v /media/pg/Expansion/data:/data \
	us-docker.pkg.dev/colab-images/public/runtime
`

Then open your browser as the docker tells you to...

