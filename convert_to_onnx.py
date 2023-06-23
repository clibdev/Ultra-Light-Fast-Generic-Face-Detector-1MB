"""
This code is used to convert the pytorch model into an onnx format model.
"""
import sys
import argparse
import torch.onnx
from vision.ssd.config.fd_config import define_img_size

parser = argparse.ArgumentParser(description='convert_to_onnix')

parser.add_argument('--model_path', default="./models/pretrained/version-RFB-640.pth", type=str, help='Model path')
parser.add_argument('--net_type', default="RFB", type=str,
                    help='The network architecture ,optional: RFB (higher precision) or slim (faster)')
parser.add_argument('--input_size', default=640, type=int,
                    help='define network input size,default optional value 128/160/320/480/640/1280')
parser.add_argument('--device', default="cuda:0", type=str, help='cuda:0 or cpu')
args = parser.parse_args()

model_path = args.model_path
input_img_size = args.input_size
net_type = args.net_type
device = args.device

define_img_size(input_img_size)  # must put define_img_size() before 'import create_mb_tiny_fd, create_mb_tiny_fd_predictor'

img_size_dict = {128: [128, 96],
                 160: [160, 120],
                 320: [320, 240],
                 480: [480, 360],
                 640: [640, 480],
                 1280: [1280, 960]}

image_size = img_size_dict[input_img_size]

from vision.ssd.mb_tiny_RFB_fd import create_Mb_Tiny_RFB_fd
from vision.ssd.mb_tiny_fd import create_mb_tiny_fd

label_path = "models/voc-model-labels.txt"
class_names = [name.strip() for name in open(label_path).readlines()]
num_classes = len(class_names)

if net_type == 'slim':
    net = create_mb_tiny_fd(len(class_names), is_test=True, device=device)
elif net_type == 'RFB':
    net = create_Mb_Tiny_RFB_fd(len(class_names), is_test=True, device=device)
else:
    print("unsupport network type.")
    sys.exit(1)

net.load(model_path)
net.eval()
net.to(device)

model_name = model_path.split("/")[-1].split(".")[0]
model_path = f"models/onnx/{model_name}.onnx"

dummy_input = torch.randn(1, 3, image_size[1], image_size[0]).to(device)
torch.onnx.export(
    net,
    dummy_input,
    model_path,
    verbose=False,
    input_names=['input'],
    output_names=['scores', 'boxes'],
    opset_version=19
)
