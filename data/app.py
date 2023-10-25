import time
import cv2, numpy as np
from ovmsclient import make_grpc_client
print("Test app")
client = make_grpc_client("ovms-sample:8080")
img=cv2.imread("/container/data/zebra.jpeg")
resize_img = cv2.resize(img, (224,224))
image = resize_img[..., np.newaxis]
data = np.transpose(image, (3, 2,0,1))
inputs = {"0": np.float32(data)}
results = client.predict(inputs=inputs, model_name="resnet")
print("Detected class:", np.argmax(results))
while True:
    time.sleep(3600)  # Sleeps for 1 hour, but will loop indefinitely.
