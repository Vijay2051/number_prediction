import io
import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
from PIL import Image

# hyper parameters
input_size = 784  # this is becoz the image we feed into the network is of size 28 x 28
hidden_size = 100  # random size
learning_rate = 0.01
num_classes = 10
MODEL_PATH = "./models/mnist.pth"


class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_of_classes):
        super(NeuralNet, self).__init__()
        self.l1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.l2 = nn.Linear(hidden_size, num_of_classes)

    def forward(self, x):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        return out


model = NeuralNet(input_size, hidden_size, num_classes)
model.load_state_dict(torch.load(MODEL_PATH))
model.eval()

# function for converting the image as the required output
def transform_image(image_bytes):
    transform = transforms.Compose(
        [
            transforms.Grayscale(num_output_channels=1),
            transforms.Resize((28, 28)),
            transforms.ToTensor(),
            transforms.Normalize((0.1307,), (0.3081,)),
        ]
    )

    image = Image.open(io.BytesIO((image_bytes)))
    return transform(image).unsqueeze(0)


# precitive functions
def get_predictions(image_tensor):
    images = image_tensor.reshape(-1, 28 * 28)
    output = model(images)
    _, predicted = torch.max(output.data, 1)
    return predicted
