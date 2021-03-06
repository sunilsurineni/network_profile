import torch.nn as nn

DEFAULT_LTYPE = {nn.Conv2d, nn.BatchNorm2d, nn.MaxPool2d, nn.ReLU, nn.ReLU6, nn.AvgPool2d}

def select_layers(model, ltype=DEFAULT_LTYPE):
    """
        Filter the submodules of model according to ltype.
    """
    check_ltype = lambda x: type(x) in ltype 
    return list(filter(check_ltype, model.modules()))

def train_model(model, inp):
    """
    """
    out = model(inp)
    out.sum().backward()