
#%%
import numpy as np
import matplotlib.pyplot as plt
from poeticpenny import loader
from pygadgetreader import readsnap, readhead

from tqdm import tqdm
from poeticpenny import basic
from poeticpenny import units
unt = units.Units("AGN")
from poeticpenny import grid
from poeticpenny import outflows
from functools import partial
from initial_condition import TimeTable
#%%
MS_yr = unt.UnitMass_in_g / unt.UnitTime_in_s * unt.year / unt.MS
punit = unt.UnitMass_in_g / unt.UnitTime_in_s * unt.UnitVelocity_in_cm_per_s #/ (1.2e46 / unt.cc) 
eunit = unt.UnitEnergy_in_cgs / unt.UnitTime_in_s

model = [  
    
    "/run/media/mt/LaCie/24AGN_mbkzmt/gadget/runs/08_corrected_ics/7_l05_c/",
    "/run/media/mt/LaCie/24AGN_mbkzmt/gadget/runs/08_corrected_ics/7_l10_c/",    
    "/run/media/mt/LaCie/24AGN_mbkzmt/gadget/runs/08_corrected_ics/7_l20_c/",
]

model_c = [
    "/run/media/mt/LaCie/24AGN_mbkzmt/gadget/runs/08_corrected_ics/7_l00_c/"
    ]

model_names = [ 
                'L0.5',            
                'L1.0',
                'L2.0'
                ]

selected_snaps = [11]
snaps = basic.get_snaps_in_dir(model)
snapsc = basic.get_snaps_in_dir(model_c)

data = loader.multi_dict(snaps, selected_snaps=selected_snaps, Nlimit=12)
datac = loader.multi_dict(snapsc, selected_snaps=selected_snaps, Nlimit=12)

#%%
N =0

#for k, M in enumerate(data):
    
    
k = 0
for k in range(len(data)):
    fig = plt.figure(figsize=(3.46,5), dpi=200)
    grid = plt.GridSpec(7, 4, hspace=0., wspace=0.0, left=0.2, right=0.95, bottom=0.1, top=0.95)
    
            
    ax_vel_hist = fig.add_subplot(grid[0, 0:3])
    ax_rho_hist = fig.add_subplot(grid[1:4, -1])
    ax_temp_hist = fig.add_subplot(grid[4:, -1])
    
    ax_rho_map = fig.add_subplot(grid[1:4, 0:3])
    ax_temp_map = fig.add_subplot(grid[4:, 0:3])
    
    ax_all = [ax_vel_hist, ax_rho_hist, ax_temp_hist, 
              ax_rho_map,  ax_temp_map]
    
    ax_temp_map.set_ylabel("$T [K]$")
    ax_temp_map.set_xlabel("$ v_{\\rm rad} \,[\\rm{km\, s}^{-1}]$")
    
    ax_rho_map.set_ylabel("$\\rho \,[\\rm{g\, cm}^{-3}]$")
    ax_rho_map.set_xlabel("$ v_{\\rm rad} \,[\\rm{km\, s}^{-1}]$")
    
    ax_vel_hist.set_ylabel("$M$[M$_{\\odot}$]")
    ax_temp_hist.set_xlabel("$M$[M$_{\\odot}$]")
    
    for axis in ax_all:
      axis.tick_params(axis='both',which='both',direction='in',top=True, right=True)  
      
    ax_vel_hist.tick_params(axis='both',which='both',direction='in',labelbottom=False)     
    ax_rho_map.tick_params(axis='both',which='both',direction='in',labelbottom=False)     
    
    ax_rho_hist.tick_params(axis='both',which='both',direction='in',labelleft=False, labelbottom=False)     
    ax_temp_hist.tick_params(axis='both',which='both',direction='in',labelleft=False)     
    

    
    ax_rho_map.set_yscale("log")
    ax_temp_map.set_yscale("log")
    

    ax_temp_hist.set_yscale("log")
    ax_rho_hist.set_yscale("log")
    
    bins_v_rho = [
            np.linspace(-1000,2800,100),
            #np.linspace(-26.5,-16,100)
            np.logspace(-26.5, -16, 100)
            ]
    
    bins_v_temp = [
            np.linspace(-1000,2800,100),
            #np.linspace(1,10,100)
            np.logspace(1,10,100)
            ]
    
    rv = data[k][11]["rad_vel"] * unt.UnitVelocity_in_cm_per_s / 1e5
    rho = data[k][11]["rho"] * unt.UnitDensity_in_cgs
    T = data[k][11]["u"] * unt.u_to_temp_fac
    Mass = data[k][11]["mass"] * unt.UnitMass_in_g / unt.MS
    
    rv0 = datac[0][11]["rad_vel"] * unt.UnitVelocity_in_cm_per_s /1e5
    rho0 = datac[0][11]["rho"] * unt.UnitDensity_in_cgs
    T0 = datac[0][11]["u"] * unt.u_to_temp_fac
    Mass0 = datac[0][11]["mass"] * unt.UnitMass_in_g / unt.MS
    
    
    ## Rho map
    hist, xedges, yedges, im = ax_rho_map.hist2d(rv, rho, 
                                                 bins=bins_v_rho, 
                                                 cmap='Blues', norm="log", weights=Mass)
    
    hist, xedges, yedges  = np.histogram2d(rv0, rho0, 
                                           bins=bins_v_rho, weights=Mass0)
    
    X, Y = np.meshgrid(xedges, yedges)
    
    ax_rho_map.contour(X[:-1, :-1], Y[:-1, :-1], hist.T, colors='black', linewidths=1, vmin=10, levels=5, alpha=0.5)
    
    ax_vel_hist.hist(rv, bins=bins_v_rho[0], 
                     orientation='vertical', color='b', 
                     histtype="step", log="True", weights=Mass)
    ax_rho_hist.hist(rho, bins=bins_v_rho[1], 
                     orientation='horizontal', color='b', 
                     histtype="step", log="True", weights=Mass)
    
    ax_vel_hist.hist(rv0, bins=bins_v_rho[0], 
                     orientation='vertical', color='gray', 
                     histtype="step", log="True", alpha=0.5, weights=Mass0)
    
    ax_rho_hist.hist(rho0, bins=bins_v_rho[1], 
                     orientation='horizontal', color='gray', 
                     histtype="step", log="True", alpha=0.5, weights=Mass0)
    

    ### temp map
    hist, xedges, yedges, im = ax_temp_map.hist2d(rv, T, bins=bins_v_temp, cmap='Blues', norm="log", weights=Mass)
    hist, xedges, yedges  = np.histogram2d(rv0, T0, bins=bins_v_temp, weights=Mass0)
    
    X, Y = np.meshgrid(xedges, yedges)
    
    ax_temp_map.contour(X[:-1, :-1], Y[:-1, :-1], hist.T, colors='black', linewidths=1, vmin=10, levels=5, alpha=0.5)
    
    ax_temp_hist.hist(T, bins=bins_v_temp[1], 
                      orientation='horizontal', color='b', histtype="step", 
                      log="True", weights=Mass)
    
    temp_bin_data = ax_temp_hist.hist(T0, bins=bins_v_temp[1], 
                      orientation='horizontal', color='gray', histtype="step", 
                      log="True", alpha=0.5, weights=Mass0)
    
    c = np.linspace(0,10,100)
    ax_rho_map.scatter(
        np.linspace(1250, 1500, 100), 
        10**(-16.8*np.ones(len(c))),c=c[::-1], 
        cmap="Blues", marker="s")
    
    ax_rho_map.plot([1200,1500], [10**-17.8,10**-17.8], c="gray")
    
    
    name = model_names[k]
    
    ax_rho_map.text(1800, 1e-17, name, fontsize=8)
    ax_rho_map.text(1800, 1e-18, "control", fontsize=8)
    
    ### lines 
    #ax_vel_hist.vlines(0, ls="--", c="k", alpha=0.2)
    
    
    ax_rho_map.text(-180, 1e-17, "$-\\sigma$", fontsize=8, va="center",ha="right", alpha=0.4)
    ax_rho_map.text(20, 1e-17, "0", fontsize=8, va="center",ha="left", alpha=0.4)
    
    ax_temp_map.text(1500, 8e4, "$3\\times10^4$ [K]", fontsize=8, va="center",ha="left", alpha=0.4)
    
    ax_vel_hist.vlines(0, 
              ymin=ax_vel_hist.get_ylim()[0], 
              ymax=ax_vel_hist.get_ylim()[1], 
              ls=":", alpha=0.3, zorder=900, color="k")
    ax_rho_map.vlines(0, 
              ymin=ax_rho_map.get_ylim()[0], 
              ymax=ax_rho_map.get_ylim()[1], 
              ls=":", alpha=0.3, zorder=900, color="k")
    ax_temp_map.vlines(0, 
              ymin=ax_temp_map.get_ylim()[0], 
              ymax=ax_temp_map.get_ylim()[1], 
              ls=":", alpha=0.3, zorder=900, color="k")
    
    ax_vel_hist.vlines(-142, 
              ymin=ax_vel_hist.get_ylim()[0], 
              ymax=ax_vel_hist.get_ylim()[1], 
              ls=":", alpha=0.3, zorder=900, color="k")
    ax_rho_map.vlines(-142, 
              ymin=ax_rho_map.get_ylim()[0], 
              ymax=ax_rho_map.get_ylim()[1], 
              ls=":", alpha=0.3, zorder=900, color="k")
    ax_temp_map.vlines(-142, 
              ymin=ax_temp_map.get_ylim()[0], 
              ymax=ax_temp_map.get_ylim()[1], 
              ls=":", alpha=0.3, zorder=900, color="k")
    
    ax_temp_map.hlines(3e4, 
              xmin=ax_temp_map.get_xlim()[0], 
              xmax=ax_temp_map.get_xlim()[1], 
              ls=":", alpha=0.3, zorder=900, color="k")
    
    ax_temp_hist.hlines(3e4, 
              xmin=ax_temp_hist.get_xlim()[0], 
              xmax=ax_temp_hist.get_xlim()[1], 
              ls=":", alpha=0.3, zorder=900, color="k")
    
    
    ax_rho_hist.set_xlim(600, 1e9)
    ax_rho_hist.set_ylim(10**-26.5, 10**-16)
    
    ax_temp_hist.set_xlim(600, 1e9)
    ax_vel_hist.set_ylim(600, 1e9)
    ax_vel_hist.set_xlim(-1000, 2800)
    ax_temp_map.set_ylim(1e1, 10**9.5)
    ax_temp_hist.set_ylim(1e1, 10**9.5)
    
    plt.savefig(f"./plots/better_phase_maps_vel_dens_temp_{name}.png", dpi=300)

# %%
