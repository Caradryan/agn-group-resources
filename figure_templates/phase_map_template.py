#%%
import numpy as np
import matplotlib.pyplot as plt


def style_axes(ax):
    ax.tick_params(direction="in", top=True, right=True, which="both")
    ax.minorticks_on()


rng = np.random.default_rng(7)
n = 200_000

# Two-component synthetic data to create visible bimodality
rv_a = rng.normal(loc=300, scale=350, size=n // 2)
rv_b = rng.normal(loc=1400, scale=350, size=n // 2)
rv = np.concatenate([rv_a, rv_b])

log_rho_a = rng.normal(loc=-21.3, scale=0.6, size=n // 2)
log_rho_b = rng.normal(loc=-19.2, scale=0.6, size=n // 2)
rho = 10 ** np.concatenate([log_rho_a, log_rho_b])

log_t_a = rng.normal(loc=5.2, scale=0.7, size=n // 2)
log_t_b = rng.normal(loc=7.0, scale=0.7, size=n // 2)
temp = 10 ** np.concatenate([log_t_a, log_t_b])

mass = 10 ** rng.normal(loc=2.2, scale=0.6, size=n)

# Control sample for contours (slightly shifted)
rv0 = rv + rng.normal(loc=-150, scale=120, size=n)
rho0 = rho * 10 ** rng.normal(loc=0.2, scale=0.15, size=n)
temp0 = temp * 10 ** rng.normal(loc=-0.1, scale=0.2, size=n)
mass0 = mass * 10 ** rng.normal(loc=0.0, scale=0.2, size=n)

# ---- Double 2D-hist layout ----
fig = plt.figure(figsize=(3.46, 5.0), dpi=300)
grid = plt.GridSpec(7, 4, hspace=0.0, wspace=0.0, left=0.2, right=0.95, bottom=0.1, top=0.95)

ax_vel_hist = fig.add_subplot(grid[0, 0:3])
ax_rho_hist = fig.add_subplot(grid[1:4, -1])
ax_temp_hist = fig.add_subplot(grid[4:, -1])

ax_rho_map = fig.add_subplot(grid[1:4, 0:3])
ax_temp_map = fig.add_subplot(grid[4:, 0:3])

for axis in [ax_vel_hist, ax_rho_hist, ax_temp_hist, ax_rho_map, ax_temp_map]:
    style_axes(axis)

ax_temp_map.set_ylabel("T [K]")
ax_temp_map.set_xlabel(r"$v_{\rm rad}$ [km s$^{-1}$]")
ax_rho_map.set_ylabel(r"$\rho$ [g cm$^{-3}$]")
ax_rho_map.set_xlabel(r"$v_{\rm rad}$ [km s$^{-1}$]")
ax_vel_hist.set_ylabel(r"$M$ [M$_\odot$]")
ax_temp_hist.set_xlabel(r"$M$ [M$_\odot$]")

ax_vel_hist.tick_params(labelbottom=False)
ax_rho_map.tick_params(labelbottom=False)
ax_rho_hist.tick_params(labelleft=False, labelbottom=False)
ax_temp_hist.tick_params(labelleft=False)

ax_rho_map.set_yscale("log")
ax_temp_map.set_yscale("log")
ax_temp_hist.set_yscale("log")
ax_rho_hist.set_yscale("log")

bins_v_rho = [np.linspace(-1000, 2800, 100), np.logspace(-26.5, -16, 100)]
bins_v_temp = [np.linspace(-1000, 2800, 100), np.logspace(1, 10, 100)]

ax_rho_map.hist2d(rv, rho, bins=bins_v_rho, cmap="Blues", norm="log", weights=mass)
hist0, xedges0, yedges0 = np.histogram2d(rv0, rho0, bins=bins_v_rho, weights=mass0)
X0, Y0 = np.meshgrid(xedges0, yedges0)
ax_rho_map.contour(X0[:-1, :-1], Y0[:-1, :-1], hist0.T, colors="black", linewidths=1, levels=5, alpha=0.5)

ax_vel_hist.hist(rv, bins=bins_v_rho[0], orientation="vertical", color="b", histtype="step", log=True, weights=mass)
ax_rho_hist.hist(rho, bins=bins_v_rho[1], orientation="horizontal", color="b", histtype="step", log=True, weights=mass)
ax_vel_hist.hist(rv0, bins=bins_v_rho[0], orientation="vertical", color="gray", histtype="step", log=True, alpha=0.5, weights=mass0)
ax_rho_hist.hist(rho0, bins=bins_v_rho[1], orientation="horizontal", color="gray", histtype="step", log=True, alpha=0.5, weights=mass0)

ax_temp_map.hist2d(rv, temp, bins=bins_v_temp, cmap="Blues", norm="log", weights=mass)
hist1, xedges1, yedges1 = np.histogram2d(rv0, temp0, bins=bins_v_temp, weights=mass0)
X1, Y1 = np.meshgrid(xedges1, yedges1)
ax_temp_map.contour(X1[:-1, :-1], Y1[:-1, :-1], hist1.T, colors="black", linewidths=1, levels=5, alpha=0.5)

ax_temp_hist.hist(temp, bins=bins_v_temp[1], orientation="horizontal", color="b", histtype="step", log=True, weights=mass)
ax_temp_hist.hist(temp0, bins=bins_v_temp[1], orientation="horizontal", color="gray", histtype="step", log=True, alpha=0.5, weights=mass0)

ax_rho_hist.set_xlim(600, 1e9)
ax_rho_hist.set_ylim(10**-26.5, 10**-16)
ax_temp_hist.set_xlim(600, 1e9)
ax_vel_hist.set_ylim(600, 1e9)
ax_vel_hist.set_xlim(-1000, 2800)
ax_temp_map.set_ylim(1e1, 10**9.5)
ax_temp_hist.set_ylim(1e1, 10**9.5)

fig.savefig("plots/phase_map_double.pdf", dpi=300)

#%%

fig2 = plt.figure(figsize=(3.46, 3.46), dpi=300)
grid2 = plt.GridSpec(4, 4, hspace=0.0, wspace=0.0, left=0.2, right=0.95, bottom=0.15, top=0.95)

ax_vel_hist2 = fig2.add_subplot(grid2[0, 0:3])
ax_rho_hist2 = fig2.add_subplot(grid2[1:4, -1])
ax_rho_map2 = fig2.add_subplot(grid2[1:4, 0:3])

for axis in [ax_vel_hist2, ax_rho_hist2, ax_rho_map2]:
    style_axes(axis)

ax_rho_map2.set_ylabel(r"$\rho$ [g cm$^{-3}$]")
ax_rho_map2.set_xlabel(r"$v_{\rm rad}$ [km s$^{-1}$]")
ax_vel_hist2.set_ylabel(r"$M$ [M$_\odot$]")

ax_vel_hist2.tick_params(labelbottom=False)
ax_rho_hist2.tick_params(labelleft=False, labelbottom=False)

ax_rho_map2.set_yscale("log")
ax_rho_hist2.set_yscale("log")

ax_rho_map2.hist2d(rv, rho, bins=bins_v_rho, cmap="Blues", norm="log", weights=mass)
hist2, xedges2, yedges2 = np.histogram2d(rv0, rho0, bins=bins_v_rho, weights=mass0)
X2, Y2 = np.meshgrid(xedges2, yedges2)
ax_rho_map2.contour(X2[:-1, :-1], Y2[:-1, :-1], hist2.T, colors="black", linewidths=1, levels=5, alpha=0.5)

ax_vel_hist2.hist(rv, bins=bins_v_rho[0], orientation="vertical", color="b", histtype="step", log=True, weights=mass)
ax_rho_hist2.hist(rho, bins=bins_v_rho[1], orientation="horizontal", color="b", histtype="step", log=True, weights=mass)
ax_vel_hist2.hist(rv0, bins=bins_v_rho[0], orientation="vertical", color="gray", histtype="step", log=True, alpha=0.5, weights=mass0)
ax_rho_hist2.hist(rho0, bins=bins_v_rho[1], orientation="horizontal", color="gray", histtype="step", log=True, alpha=0.5, weights=mass0)

ax_vel_hist2.set_ylim(600, 1e9)
ax_vel_hist2.set_xlim(-1000, 2800)
ax_rho_hist2.set_xlim(600, 1e9)
ax_rho_hist2.set_ylim(10**-26.5, 10**-16)

fig2.savefig("plots/phase_map_single.pdf", dpi=300)

# %%
