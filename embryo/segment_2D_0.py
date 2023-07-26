# %% [markdown]
# # Threshold one frame (XY projection)

# %%
import numpy as np
import matplotlib.pyplot as plt
import imageio.v3 as iio

# %%
from skimage.filters import (
    threshold_local,
    threshold_otsu,
    threshold_multiotsu
    try_all_threshold
)

# %% [markdown]
# We are looking at the XY projection of frame 184 for Embryo 2.
#
# The original .klb file was read into a NumPy array and saved into an .npy file
# (see https://github.com/mkcor/draft-notebooks/wiki/Mouse-Embryo-Dataset#load-dataset).

# %%
frame = np.load('data/frame_184.npy')

# %%
print(f"The shape is: {frame.shape}")

# %%
plt.imshow(frame, cmap='gray')

# %%
# Contour plotting
fig, ax = plt.subplots(figsize=(5, 5))
qcs = ax.contour(frame, origin='image')
ax.set_title('Contour plot of the same raw image')
plt.show()
# Contouring does not reveal as many details

# %%
# Try various global thresholding techniques
fig, ax = try_all_threshold(frame, figsize=(10, 10), verbose=False)
plt.show()

# %% [markdown]
# Isodata and Otsu seem to give the best results.

# %%
# Global thresholding v/s Local thresholding
global_thresh = threshold_otsu(frame)
binary_global = frame > global_thresh

block_size = 35
local_thresh = threshold_local(frame, block_size, offset=10)
binary_local = frame > local_thresh

fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(20,60))
ax = axes.ravel()
plt.gray()

ax[0].imshow(frame)
ax[0].set_title('Original')

ax[1].imshow(binary_global)
ax[1].set_title('Global thresholding (Otsu)')

ax[2].imshow(binary_local)
ax[2].set_title('Local thresholding')

for a in ax:
    a.axis('off')

plt.show()
# There is a rather significant difference when we apply local thresholding as opposed to global thresholding.
# This happens because there is significant variation background intensity.

# %%
# Convenience function for plotting
def plot_comparison(plot1, plot2, title1, title2):
    fig, (ax1, ax2) = plt.subplots(
        ncols=2,
        figsize=(12, 6),
        sharex=True,
        sharey=True
    )
    ax1.imshow(plot1, cmap='gray')
    ax1.set_title(title1)
    ax2.imshow(plot2, cmap='gray')
    ax2.set_title(title2)


# %%
# Deep dive into local thresholding:
local_thresh_1 = threshold_local(frame, block_size=35, offset=10)
mask_1 = frame > local_thresh_1
local_thresh_2 = threshold_local(frame, block_size=35)
mask_2 = frame > local_thresh_2
plot_comparison(mask_1, mask_2, "Offset = 10", "Without Offset")
# Increasing the offset value yields more details of the image

# %%
local_thresh_1 = threshold_local(frame, block_size=25, offset=10)
mask_1 = frame > local_thresh_1
local_thresh_2 = threshold_local(frame, block_size=35, offset=10)
mask_2 = frame > local_thresh_2
plot_comparison(mask_1, mask_2, "block_size = 25", "block_size = 35")
# The nuclei are more defined when block_size is set to a higher value

# %%
# Try Multi-Otsu thresholding
thresholds = threshold_multiotsu(frame, classes=3)
regions = np.digitize(frame, bins=thresholds)
plot_comparison(frame, regions, "Original", "Multi-Otsu thresholding")
