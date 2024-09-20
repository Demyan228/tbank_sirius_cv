import torch

device = "cuda" if torch.cuda.is_available() else "cpu"
num_batches = 10
