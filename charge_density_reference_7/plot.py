import numpy as np
from scipy import stats
from scipy import integrate
import matplotlib.pyplot as plt

# # Plot screening charge density for all available electric fields
# for size in np.arange(0, 31, 5):
#     data = np.loadtxt('avg_{_size}.dat'.format(_size=int(size)))
#     data_reference = np.loadtxt('avg_{_size}_reference.dat'.format(_size=int(size)))
#     plt.plot(data[:,0], data[:,1] - data_reference[:,1])
#     plt.savefig('diff_{_size}.png'.format(_size=int(size)), dpi=200)
#     plt.clf()

# # Plot E_ext vs E_int with TRUE screening charge density
# e_ext_list = []
# e_int_list = []
# for size in np.arange(0, 31, 5):
#     e_ext = size/1000
#     e_ext_list.append(e_ext)
#     data = np.loadtxt('avg_{_size}.dat'.format(_size=int(size)))
#     data_reference = np.loadtxt('avg_{_size}_reference.dat'.format(_size=int(size)))
#     z = data[:,0]
#     rho_scr = data[:,1] - data_reference[:,1]
#     # Calculate surface charge on left
#     m, b, r, p, std_err = stats.linregress(z[56:59], rho_scr[56:59])
#     z_cut = -b/m # point where first peak would continue to 0
#     index = (np.abs(z-z_cut)).argmin()
#     sigma = np.trapz(rho_scr[:index+1], z[:index+1])
#     # Calculate E_int
#     e_int = e_ext -4*np.pi*sigma
#     e_int_list.append(e_int)
#
# plt.plot(e_ext_list, e_int_list)
#
# # Plot E_ext vs E_int with MODIFIED screening charge density
# e_ext_list = []
# e_int_list = []
# data_reference = np.loadtxt('avg_0_reference.dat')
# for size in np.arange(0, 31, 5):
#     e_ext = size/1000
#     e_ext_list.append(e_ext)
#     data = np.loadtxt('avg_{_size}.dat'.format(_size=int(size)))
#     z = data[:,0]
#     rho_scr = data[:,1] - data_reference[:,1]
#     # Calculate surface charge on left
#     m, b, r, p, std_err = stats.linregress(z[56:59], rho_scr[56:59])
#     z_cut = -b/m # point where first peak would continue to 0
#     index = (np.abs(z-z_cut)).argmin()
#     sigma = np.trapz(rho_scr[:index+1], z[:index+1])
#     # Calculate E_int
#     e_int = e_ext -4*np.pi*sigma
#     e_int_list.append(e_int)
#
# plt.plot(e_ext_list, e_int_list)
# plt.savefig('e_ext_vs_e_int_comb.png', dpi=200)

# Plot modified screening charge density for all available electric fields
data_reference = np.loadtxt('avg_0_reference.dat')
for size in np.arange(0, 31, 5):
    data = np.loadtxt('avg_{_size}.dat'.format(_size=int(size)))
    plt.plot(data[:,0], data[:,1] - data_reference[:,1])
    plt.savefig('diff_{_size}_mod.png'.format(_size=int(size)), dpi=200)
    plt.clf()
