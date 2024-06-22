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

Then, open the page normally in colab.    Here is the default page - https://colab.research.google.com/github/googlesamples/mediapipe/blob/main/examples/customization/object_detector.ipynb

--> Then 'Connect to a local runtime', pasting in the url provided.



