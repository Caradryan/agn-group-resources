#%%
import numpy as np
import matplotlib.pyplot as plt

# 88 mm = 3.4646 in
mm_to_in = 1 / 25.4
fig_w = 88 * mm_to_in
fig_h = 88 * mm_to_in

def style_axes(ax):
    ax.tick_params(
        direction="in",
        top=True, right=True, bottom=True, left=True,
        which="both"
    )
    ax.minorticks_on()

x = np.linspace(0, 10, 200)
y1 = np.sin(x)
y2 = np.cos(x)

# 1) Two subplots in a row (no whitespace between)
fig_row, (ax1, ax2) = plt.subplots(
    1, 2, figsize=(fig_w, fig_h), dpi=300, sharey=True
)

ax1.plot(x, y1, lw=1.5)
ax2.plot(x, y2, lw=1.5)

ax1.set_xlabel("X label")
ax1.set_ylabel("Y label")
ax2.set_xlabel("X label")
ax2.set_ylabel("Y label")

style_axes(ax1)
style_axes(ax2)

# Hide inner axis ticks/labels (right subplot y-axis)
ax2.tick_params(labelleft=False)
ax2.set_ylabel("")

# Remove whitespace between subplots
fig_row.subplots_adjust(left=0.2, right=0.95, bottom=0.2, top=0.95, wspace=0)

fig_row.savefig("multi_axis_row.pdf", dpi=300)
#%%
# 2) Two subplots in a column (no whitespace between)
fig_col, (ax3, ax4) = plt.subplots(
    2, 1, figsize=(fig_w, fig_h), dpi=300, sharex=True
)

ax3.plot(x, y1, lw=1.5)
ax4.plot(x, y2, lw=1.5)

ax3.set_xlabel("X label")
ax3.set_ylabel("Y label")
ax4.set_xlabel("X label")
ax4.set_ylabel("Y label")

style_axes(ax3)
style_axes(ax4)

# Hide inner axis ticks/labels (top subplot x-axis)
ax3.tick_params(labelbottom=False)
ax3.set_xlabel("")

# Remove whitespace between subplots
fig_col.subplots_adjust(left=0.2, right=0.95, bottom=0.2, top=0.95, hspace=0)

fig_col.savefig("multi_axis_col.pdf", dpi=300)

plt.show()

# %%
