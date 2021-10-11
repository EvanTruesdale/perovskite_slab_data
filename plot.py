import numpy as np
import matplotlib.pyplot as plt

# Section III.B plotting
#data_reference = np.loadtxt('avg_BaTiO3_7_Ba-O_P4mm_reference.dat')
#for size in np.arange(5, 85, 5):
#    data = np.loadtxt('rho_BaTiO3_7_Ba-O_P4mm_{_size}.dat'.format(_size=int(size)))
#    plt.plot(data[:,0], data[:,1] - data_reference[:,1])
#    plt.savefig('screening_rho_BaTiO3_7_Ba-O_P4mm_{_size}.png'.format(_size=int(size)), dpi=300)
#    plt.clf()

# Section III.A plotting
data = np.loadtxt('charge_density_BaTiO3_7_Ba-O_P4mm_0.dat')
plt.plot(data[:,0], data[:,1])
plt.savefig('charge_density_BaTiO3_7_Ba-O_P4mm_0.png', dpi=300)
plt.clf()

data = np.loadtxt('ionic_hartree_potential_BaTiO3_7_Ba-O_P4mm_0.dat')
plt.plot(data[:,0], data[:,1])
plt.savefig('ionic_hartree_potential_BaTiO3_7_Ba-O_P4mm_0.png', dpi=300)
plt.clf()

data = np.loadtxt('ionic_potential_BaTiO3_7_Ba-O_P4mm_0.dat')
plt.plot(data[:,0], data[:,1])
plt.savefig('ionic_potential_BaTiO3_7_Ba-O_P4mm_0.png', dpi=300)
plt.clf()

data = np.loadtxt('sawtooth_BaTiO3_7_Ba-O_P4mm_0.dat')
plt.plot(data[:,0], data[:,1])
plt.savefig('sawtooth_BaTiO3_7_Ba-O_P4mm_0.png', dpi=300)
plt.clf()

data = np.loadtxt('total_potential_BaTiO3_7_Ba-O_P4mm_0.dat')
plt.plot(data[:,0], data[:,1])
plt.savefig('total_potential_BaTiO3_7_Ba-O_P4mm_0.png', dpi=300)
plt.clf()
