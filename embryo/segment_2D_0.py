# %% [markdown]
# # Threshold one frame (XY projection)

# %%
import numpy as np
import matplotlib.pyplot as plt
import imageio.v3 as iio

# %%
from skimage.filters import try_all_threshold, threshold_otsu, threshold_local

# %% [markdown]
# The original .klb file was read into a NumPy array and saved into an .npy file.

# %%
frame = np.load('data/frame_184.npy')
