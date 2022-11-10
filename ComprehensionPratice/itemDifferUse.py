dict = {'Name': 'Zara', 'Age': 7}
new_dict = {key: value for key, value in dict.items()}
# items is used for dict iterator
# {'Name': 'Zara', 'Age': 7}
print(new_dict)

import torch

x = torch.randn(3, 3)
print(x[1, 1].item())
# item is used for tensor specification
# -0.027050450444221497