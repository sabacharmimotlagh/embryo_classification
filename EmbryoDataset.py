import torch.utils.data as data_utl
from PIL import Image

class EmbryoDataset(data_utl.Dataset):

    def __init__(self, image_label_mapping, train=True, transform=None):
        self.image_label_mapping = image_label_mapping
        self.image_paths = list(image_label_mapping.keys())
        self.labels = list(image_label_mapping.values())
        self.transform = transform
        self.train = train

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, index):

        image_path = self.image_paths[index]
        image = Image.open(image_path)

        # image transformation
        if self.transform:
            image = self.transform(image)

        if self.train:
            label = self.labels[index]
            return image, label
        else:
            ID = self.labels[index]
            return image, ID