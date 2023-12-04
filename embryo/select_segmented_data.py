# %% [markdown]
# # Select one time point (embryo B)

# %% [markdown]
# This is the code to generate file `data/frame_184.csv`.

# %%
import pandas as pd

# %% [markdown]
# Follow instructions at https://github.com/mkcor/draft-notebooks/wiki/Mouse-Embryo-Dataset#look-up-segmented-data
# to download the segmentation results for embryo B.

# %%
df = pd.read_csv('data/Data_S1L.csv')

# %%
frame = 184  # edit

# %%
cond = df.t == frame

# %%
frame_to_save = df[cond]

# %%
frame_to_save.to_csv('data/frame_184.csv', index=False)
