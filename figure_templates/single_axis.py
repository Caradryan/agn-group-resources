#%%
import numpy as np
import matplotlib.pyplot as plt

# 88 mm = 3.4646 in
mm_to_in = 1 / 25.4
fig_w = 88 * mm_to_in
fig_h = 88 * mm_to_in

fig, ax = plt.subplots(figsize=(fig_w, fig_h), dpi=300)

x = np.linspace(0, 10, 200)
y = np.sin(x)
ax.plot(x, y, lw=1.5)

# Labels (arbitrary)
ax.set_xlabel("x")
ax.set_ylabel("z")

# Ticks on all axes, inward
ax.tick_params(direction="in", top=True, right=True, bottom=True, left=True, which="both")
# Turn on minnor tick ax.minorticks_on()

# Keep the plotting area square
ax.set_box_aspect(1)
# Or use set_aspect() to 

# This is sometimes real pain to adjust. 
# Tick labels can change size etc. Sometimes this is better adjusted once
# all similar figures are "known"
fig.subplots_adjust(left=0.20, right=0.95, bottom=0.20, top=0.95)

# Vector output
fig.savefig("basic_plot.pdf", dpi=300) # Use to remove redundant whitespace automatically bbox_inches="tight"
plt.show()
#%%

# log-log version


import numpy as np
import matplotlib.pyplot as plt

# 88 mm = 3.4646 in
mm_to_in = 1 / 25.4
fig_w = 88 * mm_to_in
fig_h = 88 * mm_to_in

fig, ax = plt.subplots(figsize=(fig_w, fig_h), dpi=300)

x = np.linspace(0, 10, 200)
y = np.sin(x)
ax.plot(x, y, lw=1.5)

# Labels (arbitrary)
ax.set_xlabel("x")
ax.set_ylabel("z")

ax.set_yscale("log")
ax.set_xscale("log")

# Ticks on all axes, inward
ax.tick_params(direction="in", top=True, right=True, bottom=True, left=True, which="both")
# Turn on minnor tick ax.minorticks_on()

# Keep the plotting area square
ax.set_box_aspect(1)
# Or use set_aspect() to 

# This is sometimes real pain to adjust. 
# Tick labels can change size etc. Sometimes this is better adjusted once
# all similar figures are "known"
fig.subplots_adjust(left=0.20, right=0.95, bottom=0.20, top=0.95)

# Vector output
fig.savefig("basic_plot_log.pdf", dpi=300) # Use to remove redundant whitespace automatically bbox_inches="tight"
plt.show()