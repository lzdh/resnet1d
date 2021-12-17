dependencies = ['torch']
import net1d as _net1d

def net1d(pretrained=False, **kwargs):
    return _net1d(pretrained=pretrained, **kwargs)

