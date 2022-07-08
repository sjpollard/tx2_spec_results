import numpy as np
from matplotlib import pyplot as plt

def tiny_gnu_mpi_time(times):
    times = np.log10(times)
    plt.title("Tiny suite - ThunderX2 - GNU Compiler - MPI Runtime (64 ranks/node)")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([2, 3.4])
    plt.plot([1,2,4,8], times.T[0], marker="x", label="lbm")
    plt.plot([1,2,4,8], times.T[1], marker="x", label="soma")
    plt.plot([1,2,4,8], times.T[2], marker="x", label="tealeaf")
    plt.plot([1,2,4,8], times.T[3], marker="x", label="clvleaf")
    plt.plot([1,2,4,8], times.T[4], marker="x", label="miniswp")
    plt.plot([1,2,4,8], times.T[5], marker="x", label="pot3d")
    plt.plot([1,2,4,8], times.T[6], marker="x", label="sph_exa")
    plt.plot([1,2,4,8], times.T[7], marker="x", label="hpgmgfv")
    plt.plot([1,2,4,8], times.T[8], marker="x", label="weather")
    plt.legend(loc="upper right")
    plt.xlabel("Number of nodes (64 cores/node)")
    plt.ylabel("$log_{10}$ Time(s)")
    plt.savefig("tiny_gnu_mpi_time.pdf")
    plt.clf()

def tiny_gnu_mpi_speedup(times):
    speedup = times[0]/times
    plt.title("Tiny suite - ThunderX2 - GNU Compiler - MPI Speedup (64 ranks/node)")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([1, 8])
    plt.plot(np.arange(0, 9), c="grey", linestyle="--")
    plt.plot([1,2,4,8], speedup.T[0], marker="x", label="lbm")
    plt.plot([1,2,4,8], speedup.T[1], marker="x", label="soma")
    plt.plot([1,2,4,8], speedup.T[2], marker="x", label="tealeaf")
    plt.plot([1,2,4,8], speedup.T[3], marker="x", label="clvleaf")
    plt.plot([1,2,4,8], speedup.T[4], marker="x", label="miniswp")
    plt.plot([1,2,4,8], speedup.T[5], marker="x", label="pot3d")
    plt.plot([1,2,4,8], speedup.T[6], marker="x", label="sph_exa")
    plt.plot([1,2,4,8], speedup.T[7], marker="x", label="hpgmgfv")
    plt.plot([1,2,4,8], speedup.T[8], marker="x", label="weather")
    plt.legend(loc="upper left")
    plt.xlabel("Number of nodes (64 cores/node)")
    plt.ylabel("Speedup")
    plt.savefig("tiny_gnu_mpi_speedup.pdf")
    plt.clf()

def tiny_gnu_mpi_efficiency(times):
    speedup = times[0]/times
    efficiency = speedup/np.array([[1],[2],[4],[8]]) * 100
    plt.title("Tiny suite - ThunderX2 - GNU Compiler - MPI Efficiency (64 ranks/node)")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([30, 110])
    plt.axhline(y=100, c="grey", linestyle="--")
    plt.plot([1,2,4,8], efficiency.T[0], marker="x", label="lbm")
    plt.plot([1,2,4,8], efficiency.T[1], marker="x", label="soma")
    plt.plot([1,2,4,8], efficiency.T[2], marker="x", label="tealeaf")
    plt.plot([1,2,4,8], efficiency.T[3], marker="x", label="clvleaf")
    plt.plot([1,2,4,8], efficiency.T[4], marker="x", label="miniswp")
    plt.plot([1,2,4,8], efficiency.T[5], marker="x", label="pot3d")
    plt.plot([1,2,4,8], efficiency.T[6], marker="x", label="sph_exa")
    plt.plot([1,2,4,8], efficiency.T[7], marker="x", label="hpgmgfv")
    plt.plot([1,2,4,8], efficiency.T[8], marker="x", label="weather")
    plt.legend(loc="lower left")
    plt.xlabel("Number of nodes (64 cores/node)")
    plt.ylabel("Parallel efficiency(%)")
    plt.savefig("tiny_gnu_mpi_efficiency.pdf")
    plt.clf()

def tiny_cray_mpi_time(times):
    times = np.log10(times)
    plt.title("Tiny suite - ThunderX2 - Cray Compiler - MPI Runtime (64 ranks/node)")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([2, 3.4])
    plt.plot([1,2,4,8], times.T[0], marker="x", label="lbm")
    plt.plot([1,2,4,8], times.T[1], marker="x", label="soma")
    plt.plot([1,2,4,8], times.T[2], marker="x", label="tealeaf")
    plt.plot([1,2,4,8], times.T[3], marker="x", label="clvleaf")
    plt.plot([1,2,4,8], times.T[4], marker="x", label="miniswp")
    plt.plot([1,2,4,8], times.T[5], marker="x", label="pot3d")
    plt.plot([1,2,4,8], times.T[6], marker="x", label="sph_exa")
    plt.plot([1,2,4,8], times.T[7], marker="x", label="hpgmgfv")
    plt.plot([1,2,4,8], times.T[8], marker="x", label="weather")
    plt.legend(loc="upper right")
    plt.xlabel("Number of nodes (64 cores/node)")
    plt.ylabel("$log_{10}$ Time(s)")
    plt.savefig("tiny_cray_mpi_time.pdf")
    plt.clf()

def tiny_cray_mpi_speedup(times):
    speedup = times[0]/times
    plt.title("Tiny suite - ThunderX2 - Cray Compiler - MPI Speedup (64 ranks/node)")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([1, 8])
    plt.plot(np.arange(0, 9), c="grey", linestyle="--")
    plt.plot([1,2,4,8], speedup.T[0], marker="x", label="lbm")
    plt.plot([1,2,4,8], speedup.T[1], marker="x", label="soma")
    plt.plot([1,2,4,8], speedup.T[2], marker="x", label="tealeaf")
    plt.plot([1,2,4,8], speedup.T[3], marker="x", label="clvleaf")
    plt.plot([1,2,4,8], speedup.T[4], marker="x", label="miniswp")
    plt.plot([1,2,4,8], speedup.T[5], marker="x", label="pot3d")
    plt.plot([1,2,4,8], speedup.T[6], marker="x", label="sph_exa")
    plt.plot([1,2,4,8], speedup.T[7], marker="x", label="hpgmgfv")
    plt.plot([1,2,4,8], speedup.T[8], marker="x", label="weather")
    plt.legend(loc="upper left")
    plt.xlabel("Number of nodes (64 cores/node)")
    plt.ylabel("Speedup")
    plt.savefig("tiny_cray_mpi_speedup.pdf")
    plt.clf()

def tiny_cray_mpi_efficiency(times):
    speedup = times[0]/times
    efficiency = speedup/np.array([[1],[2],[4],[8]]) * 100
    plt.title("Tiny suite - ThunderX2 - Cray Compiler - MPI Efficiency (64 ranks/node)")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([30, 110])
    plt.axhline(y=100, c="grey", linestyle="--")
    plt.plot([1,2,4,8], efficiency.T[0], marker="x", label="lbm")
    plt.plot([1,2,4,8], efficiency.T[1], marker="x", label="soma")
    plt.plot([1,2,4,8], efficiency.T[2], marker="x", label="tealeaf")
    plt.plot([1,2,4,8], efficiency.T[3], marker="x", label="clvleaf")
    plt.plot([1,2,4,8], efficiency.T[4], marker="x", label="miniswp")
    plt.plot([1,2,4,8], efficiency.T[5], marker="x", label="pot3d")
    plt.plot([1,2,4,8], efficiency.T[6], marker="x", label="sph_exa")
    plt.plot([1,2,4,8], efficiency.T[7], marker="x", label="hpgmgfv")
    plt.plot([1,2,4,8], efficiency.T[8], marker="x", label="weather")
    plt.legend(loc="lower left")
    plt.xlabel("Number of nodes (64 cores/node)")
    plt.ylabel("Parallel efficiency(%)")
    plt.savefig("tiny_cray_mpi_efficiency.pdf")
    plt.clf()

def tiny_arm_mpi_time(times):
    times = np.log10(times)
    plt.title("Tiny suite - ThunderX2 - Arm Compiler - MPI Runtime (64 ranks/node)")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([2, 3.4])
    plt.plot([1,2,4,8], times.T[0], marker="x", label="lbm")
    plt.plot([1,2,4,8], times.T[1], marker="x", label="soma")
    plt.plot([1,2,4,8], times.T[2], marker="x", label="tealeaf")
    plt.plot([1,2,4,8], times.T[3], marker="x", label="clvleaf")
    plt.plot([1,2,4,8], times.T[4], marker="x", label="miniswp")
    plt.plot([1,2,4,8], times.T[5], marker="x", label="pot3d")
    plt.plot([1,2,4,8], times.T[6], marker="x", label="sph_exa")
    plt.plot([1,2,4,8], times.T[7], marker="x", label="hpgmgfv")
    plt.plot([1,2,4,8], times.T[8], marker="x", label="weather")
    plt.legend(loc="upper right")
    plt.xlabel("Number of nodes (64 cores/node)")
    plt.ylabel("$log_{10}$ Time(s)")
    plt.savefig("tiny_arm_mpi_time.pdf")
    plt.clf()

def tiny_arm_mpi_speedup(times):
    speedup = times[0]/times
    plt.title("Tiny suite - ThunderX2 - Arm Compiler - MPI Speedup (64 ranks/node)")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([1, 8])
    plt.plot(np.arange(0, 9), c="grey", linestyle="--")
    plt.plot([1,2,4,8], speedup.T[0], marker="x", label="lbm")
    plt.plot([1,2,4,8], speedup.T[1], marker="x", label="soma")
    plt.plot([1,2,4,8], speedup.T[2], marker="x", label="tealeaf")
    plt.plot([1,2,4,8], speedup.T[3], marker="x", label="clvleaf")
    plt.plot([1,2,4,8], speedup.T[4], marker="x", label="miniswp")
    plt.plot([1,2,4,8], speedup.T[5], marker="x", label="pot3d")
    plt.plot([1,2,4,8], speedup.T[6], marker="x", label="sph_exa")
    plt.plot([1,2,4,8], speedup.T[7], marker="x", label="hpgmgfv")
    plt.plot([1,2,4,8], speedup.T[8], marker="x", label="weather")
    plt.legend(loc="upper left")
    plt.xlabel("Number of nodes (64 cores/node)")
    plt.ylabel("Speedup")
    plt.savefig("tiny_arm_mpi_speedup.pdf")
    plt.clf()

def tiny_arm_mpi_efficiency(times):
    speedup = times[0]/times
    efficiency = speedup/np.array([[1],[2],[4],[8]]) * 100
    plt.title("Tiny suite - ThunderX2 - Arm Compiler - MPI Efficiency (64 ranks/node)")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([30, 110])
    plt.axhline(y=100, c="grey", linestyle="--")
    plt.plot([1,2,4,8], efficiency.T[0], marker="x", label="lbm")
    plt.plot([1,2,4,8], efficiency.T[1], marker="x", label="soma")
    plt.plot([1,2,4,8], efficiency.T[2], marker="x", label="tealeaf")
    plt.plot([1,2,4,8], efficiency.T[3], marker="x", label="clvleaf")
    plt.plot([1,2,4,8], efficiency.T[4], marker="x", label="miniswp")
    plt.plot([1,2,4,8], efficiency.T[5], marker="x", label="pot3d")
    plt.plot([1,2,4,8], efficiency.T[6], marker="x", label="sph_exa")
    plt.plot([1,2,4,8], efficiency.T[7], marker="x", label="hpgmgfv")
    plt.plot([1,2,4,8], efficiency.T[8], marker="x", label="weather")
    plt.legend(loc="lower left")
    plt.xlabel("Number of nodes (64 cores/node)")
    plt.ylabel("Parallel efficiency(%)")
    plt.savefig("tiny_arm_mpi_efficiency.pdf")
    plt.clf()

def tiny_gnu_omp_1ppn_time(times):
    times = np.log10(times)
    plt.title("Tiny suite - ThunderX2 - GNU Compiler - OMP Runtime (1 rank/node)")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([2, 3.6])
    plt.plot([1,2,4,8], times.T[0], marker="x", label="lbm")
    plt.plot([1,2,4,8], times.T[1], marker="x", label="soma")
    plt.plot([1,2,4,8], times.T[2], marker="x", label="tealeaf")
    plt.plot([1,2,4,8], times.T[3], marker="x", label="clvleaf")
    plt.plot([1,2,4,8], times.T[4], marker="x", label="miniswp")
    plt.plot([1,2,4,8], times.T[5], marker="x", label="pot3d")
    plt.plot([1,2,4,8], times.T[6], marker="x", label="sph_exa")
    plt.plot([1,2,4,8], times.T[7], marker="x", label="hpgmgfv")
    plt.plot([1,2,4,8], times.T[8], marker="x", label="weather")
    plt.legend(loc="upper right")
    plt.xlabel("Number of nodes (64 cores/node)")
    plt.ylabel("$log_{10}$ Time(s)")
    plt.savefig("tiny_gnu_omp_1ppn_time.pdf")
    plt.clf()

def tiny_gnu_omp_1ppn_speedup(times):
    speedup = times[0]/times
    plt.title("Tiny suite - ThunderX2 - GNU Compiler - OMP Speedup (1 rank/node)")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([1, 14])
    plt.plot(np.arange(0, 9), c="grey", linestyle="--")
    plt.plot([1,2,4,8], speedup.T[0], marker="x", label="lbm")
    plt.plot([1,2,4,8], speedup.T[1], marker="x", label="soma")
    plt.plot([1,2,4,8], speedup.T[2], marker="x", label="tealeaf")
    plt.plot([1,2,4,8], speedup.T[3], marker="x", label="clvleaf")
    plt.plot([1,2,4,8], speedup.T[4], marker="x", label="miniswp")
    plt.plot([1,2,4,8], speedup.T[5], marker="x", label="pot3d")
    plt.plot([1,2,4,8], speedup.T[6], marker="x", label="sph_exa")
    plt.plot([1,2,4,8], speedup.T[7], marker="x", label="hpgmgfv")
    plt.plot([1,2,4,8], speedup.T[8], marker="x", label="weather")
    plt.legend(loc="upper left")
    plt.xlabel("Number of nodes (64 cores/node)")
    plt.ylabel("Speedup")
    plt.savefig("tiny_gnu_omp_1ppn_speedup.pdf")
    plt.clf()

def tiny_gnu_omp_1ppn_efficiency(times):
    speedup = times[0]/times
    efficiency = speedup/np.array([[1],[2],[4],[8]]) * 100
    plt.title("Tiny suite - ThunderX2 - GNU Compiler - OMP Efficiency (1 rank/node)")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([20, 200])
    plt.axhline(y=100, c="grey", linestyle="--")
    plt.plot([1,2,4,8], efficiency.T[0], marker="x", label="lbm")
    plt.plot([1,2,4,8], efficiency.T[1], marker="x", label="soma")
    plt.plot([1,2,4,8], efficiency.T[2], marker="x", label="tealeaf")
    plt.plot([1,2,4,8], efficiency.T[3], marker="x", label="clvleaf")
    plt.plot([1,2,4,8], efficiency.T[4], marker="x", label="miniswp")
    plt.plot([1,2,4,8], efficiency.T[5], marker="x", label="pot3d")
    plt.plot([1,2,4,8], efficiency.T[6], marker="x", label="sph_exa")
    plt.plot([1,2,4,8], efficiency.T[7], marker="x", label="hpgmgfv")
    plt.plot([1,2,4,8], efficiency.T[8], marker="x", label="weather")
    plt.legend(loc="lower left")
    plt.xlabel("Number of nodes (64 cores/node)")
    plt.ylabel("Parallel efficiency(%)")
    plt.savefig("tiny_gnu_omp_1ppn_efficiency.pdf")
    plt.clf()

def tiny_gnu_omp_2ppn_time(times):
    times = np.log10(times)
    plt.title("Tiny suite - ThunderX2 - GNU Compiler - OMP Runtime (2 ranks/node)")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([2, 3.6])
    plt.plot([1,2,4,8], times.T[0], marker="x", label="lbm")
    plt.plot([1,2,4,8], times.T[1], marker="x", label="soma")
    plt.plot([1,2,4,8], times.T[2], marker="x", label="tealeaf")
    plt.plot([1,2,4,8], times.T[3], marker="x", label="clvleaf")
    plt.plot([1,2,4,8], times.T[4], marker="x", label="miniswp")
    plt.plot([1,2,4,8], times.T[5], marker="x", label="pot3d")
    plt.plot([1,2,4,8], times.T[6], marker="x", label="sph_exa")
    plt.plot([1,2,4,8], times.T[7], marker="x", label="hpgmgfv")
    plt.plot([1,2,4,8], times.T[8], marker="x", label="weather")
    plt.legend(loc="upper right")
    plt.xlabel("Number of nodes (64 cores/node)")
    plt.ylabel("$log_{10}$ Time(s)")
    plt.savefig("tiny_gnu_omp_2ppn_time.pdf")
    plt.clf()

def tiny_gnu_omp_2ppn_speedup(times):
    speedup = times[0]/times
    plt.title("Tiny suite - ThunderX2 - GNU Compiler - OMP Speedup (2 ranks/node)")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([1, 14])
    plt.plot(np.arange(0, 9), c="grey", linestyle="--")
    plt.plot([1,2,4,8], speedup.T[0], marker="x", label="lbm")
    plt.plot([1,2,4,8], speedup.T[1], marker="x", label="soma")
    plt.plot([1,2,4,8], speedup.T[2], marker="x", label="tealeaf")
    plt.plot([1,2,4,8], speedup.T[3], marker="x", label="clvleaf")
    plt.plot([1,2,4,8], speedup.T[4], marker="x", label="miniswp")
    plt.plot([1,2,4,8], speedup.T[5], marker="x", label="pot3d")
    plt.plot([1,2,4,8], speedup.T[6], marker="x", label="sph_exa")
    plt.plot([1,2,4,8], speedup.T[7], marker="x", label="hpgmgfv")
    plt.plot([1,2,4,8], speedup.T[8], marker="x", label="weather")
    plt.legend(loc="upper left")
    plt.xlabel("Number of nodes (64 cores/node)")
    plt.ylabel("Speedup")
    plt.savefig("tiny_gnu_omp_2ppn_speedup.pdf")
    plt.clf()

def tiny_gnu_omp_2ppn_efficiency(times):
    speedup = times[0]/times
    efficiency = speedup/np.array([[1],[2],[4],[8]]) * 100
    plt.title("Tiny suite - ThunderX2 - GNU Compiler - OMP Efficiency (2 ranks/node)")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([40, 160])
    plt.axhline(y=100, c="grey", linestyle="--")
    plt.plot([1,2,4,8], efficiency.T[0], marker="x", label="lbm")
    plt.plot([1,2,4,8], efficiency.T[1], marker="x", label="soma")
    plt.plot([1,2,4,8], efficiency.T[2], marker="x", label="tealeaf")
    plt.plot([1,2,4,8], efficiency.T[3], marker="x", label="clvleaf")
    plt.plot([1,2,4,8], efficiency.T[4], marker="x", label="miniswp")
    plt.plot([1,2,4,8], efficiency.T[5], marker="x", label="pot3d")
    plt.plot([1,2,4,8], efficiency.T[6], marker="x", label="sph_exa")
    plt.plot([1,2,4,8], efficiency.T[7], marker="x", label="hpgmgfv")
    plt.plot([1,2,4,8], efficiency.T[8], marker="x", label="weather")
    plt.legend(loc="lower left")
    plt.xlabel("Number of nodes (64 cores/node)")
    plt.ylabel("Parallel efficiency(%)")
    plt.savefig("tiny_gnu_omp_2ppn_efficiency.pdf")
    plt.clf()

def tiny_gnu_omp_4ppn_time(times):
    times = np.log10(times)
    plt.title("Tiny suite - ThunderX2 - GNU Compiler - OMP Runtime (4 ranks/node)")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([2, 3.6])
    plt.plot([1,2,4,8], times.T[0], marker="x", label="lbm")
    plt.plot([1,2,4,8], times.T[1], marker="x", label="soma")
    plt.plot([1,2,4,8], times.T[2], marker="x", label="tealeaf")
    plt.plot([1,2,4,8], times.T[3], marker="x", label="clvleaf")
    plt.plot([1,2,4,8], times.T[4], marker="x", label="miniswp")
    plt.plot([1,2,4,8], times.T[5], marker="x", label="pot3d")
    plt.plot([1,2,4,8], times.T[6], marker="x", label="sph_exa")
    plt.plot([1,2,4,8], times.T[7], marker="x", label="hpgmgfv")
    plt.plot([1,2,4,8], times.T[8], marker="x", label="weather")
    plt.legend(loc="upper right")
    plt.xlabel("Number of nodes (64 cores/node)")
    plt.ylabel("$log_{10}$ Time(s)")
    plt.savefig("tiny_gnu_omp_4ppn_time.pdf")
    plt.clf()

def tiny_gnu_omp_4ppn_speedup(times):
    speedup = times[0]/times
    plt.title("Tiny suite - ThunderX2 - GNU Compiler - OMP Speedup (4 ranks/node)")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([1, 14])
    plt.plot(np.arange(0, 9), c="grey", linestyle="--")
    plt.plot([1,2,4,8], speedup.T[0], marker="x", label="lbm")
    plt.plot([1,2,4,8], speedup.T[1], marker="x", label="soma")
    plt.plot([1,2,4,8], speedup.T[2], marker="x", label="tealeaf")
    plt.plot([1,2,4,8], speedup.T[3], marker="x", label="clvleaf")
    plt.plot([1,2,4,8], speedup.T[4], marker="x", label="miniswp")
    plt.plot([1,2,4,8], speedup.T[5], marker="x", label="pot3d")
    plt.plot([1,2,4,8], speedup.T[6], marker="x", label="sph_exa")
    plt.plot([1,2,4,8], speedup.T[7], marker="x", label="hpgmgfv")
    plt.plot([1,2,4,8], speedup.T[8], marker="x", label="weather")
    plt.legend(loc="upper left")
    plt.xlabel("Number of nodes (64 cores/node)")
    plt.ylabel("Speedup")
    plt.savefig("tiny_gnu_omp_4ppn_speedup.pdf")
    plt.clf()

def tiny_gnu_omp_4ppn_efficiency(times):
    speedup = times[0]/times
    efficiency = speedup/np.array([[1],[2],[4],[8]]) * 100
    plt.title("Tiny suite - ThunderX2 - GNU Compiler - OMP Efficiency (4 ranks/node)")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([40, 160])
    plt.axhline(y=100, c="grey", linestyle="--")
    plt.plot([1,2,4,8], efficiency.T[0], marker="x", label="lbm")
    plt.plot([1,2,4,8], efficiency.T[1], marker="x", label="soma")
    plt.plot([1,2,4,8], efficiency.T[2], marker="x", label="tealeaf")
    plt.plot([1,2,4,8], efficiency.T[3], marker="x", label="clvleaf")
    plt.plot([1,2,4,8], efficiency.T[4], marker="x", label="miniswp")
    plt.plot([1,2,4,8], efficiency.T[5], marker="x", label="pot3d")
    plt.plot([1,2,4,8], efficiency.T[6], marker="x", label="sph_exa")
    plt.plot([1,2,4,8], efficiency.T[7], marker="x", label="hpgmgfv")
    plt.plot([1,2,4,8], efficiency.T[8], marker="x", label="weather")
    plt.legend(loc="lower left")
    plt.xlabel("Number of nodes (64 cores/node)")
    plt.ylabel("Parallel efficiency(%)")
    plt.savefig("tiny_gnu_omp_4ppn_efficiency.pdf")
    plt.clf()

def tiny_gnu_omp_8ppn_time(times):
    times = np.log10(times)
    plt.title("Tiny suite - ThunderX2 - GNU Compiler - OMP Runtime (8 ranks/node)")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([2, 3.6])
    plt.plot([1,2,4,8], times.T[0], marker="x", label="lbm")
    plt.plot([1,2,4,8], times.T[1], marker="x", label="soma")
    plt.plot([1,2,4,8], times.T[2], marker="x", label="tealeaf")
    plt.plot([1,2,4,8], times.T[3], marker="x", label="clvleaf")
    plt.plot([1,2,4,8], times.T[4], marker="x", label="miniswp")
    plt.plot([1,2,4,8], times.T[5], marker="x", label="pot3d")
    plt.plot([1,2,4,8], times.T[6], marker="x", label="sph_exa")
    plt.plot([1,2,4,8], times.T[7], marker="x", label="hpgmgfv")
    plt.plot([1,2,4,8], times.T[8], marker="x", label="weather")
    plt.legend(loc="upper right")
    plt.xlabel("Number of nodes (64 cores/node)")
    plt.ylabel("$log_{10}$ Time(s)")
    plt.savefig("tiny_gnu_omp_8ppn_time.pdf")
    plt.clf()

def tiny_gnu_omp_8ppn_speedup(times):
    speedup = times[0]/times
    plt.title("Tiny suite - ThunderX2 - GNU Compiler - OMP Speedup (8 ranks/node)")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([1, 14])
    plt.plot(np.arange(0, 9), c="grey", linestyle="--")
    plt.plot([1,2,4,8], speedup.T[0], marker="x", label="lbm")
    plt.plot([1,2,4,8], speedup.T[1], marker="x", label="soma")
    plt.plot([1,2,4,8], speedup.T[2], marker="x", label="tealeaf")
    plt.plot([1,2,4,8], speedup.T[3], marker="x", label="clvleaf")
    plt.plot([1,2,4,8], speedup.T[4], marker="x", label="miniswp")
    plt.plot([1,2,4,8], speedup.T[5], marker="x", label="pot3d")
    plt.plot([1,2,4,8], speedup.T[6], marker="x", label="sph_exa")
    plt.plot([1,2,4,8], speedup.T[7], marker="x", label="hpgmgfv")
    plt.plot([1,2,4,8], speedup.T[8], marker="x", label="weather")
    plt.legend(loc="upper left")
    plt.xlabel("Number of nodes (64 cores/node)")
    plt.ylabel("Speedup")
    plt.savefig("tiny_gnu_omp_8ppn_speedup.pdf")
    plt.clf()

def tiny_gnu_omp_8ppn_efficiency(times):
    speedup = times[0]/times
    efficiency = speedup/np.array([[1],[2],[4],[8]]) * 100
    plt.title("Tiny suite - ThunderX2 - GNU Compiler - OMP Efficiency (8 ranks/node)")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([40, 140])
    plt.axhline(y=100, c="grey", linestyle="--")
    plt.plot([1,2,4,8], efficiency.T[0], marker="x", label="lbm")
    plt.plot([1,2,4,8], efficiency.T[1], marker="x", label="soma")
    plt.plot([1,2,4,8], efficiency.T[2], marker="x", label="tealeaf")
    plt.plot([1,2,4,8], efficiency.T[3], marker="x", label="clvleaf")
    plt.plot([1,2,4,8], efficiency.T[4], marker="x", label="miniswp")
    plt.plot([1,2,4,8], efficiency.T[5], marker="x", label="pot3d")
    plt.plot([1,2,4,8], efficiency.T[6], marker="x", label="sph_exa")
    plt.plot([1,2,4,8], efficiency.T[7], marker="x", label="hpgmgfv")
    plt.plot([1,2,4,8], efficiency.T[8], marker="x", label="weather")
    plt.legend(loc="lower left")
    plt.xlabel("Number of nodes (64 cores/node)")
    plt.ylabel("Parallel efficiency(%)")
    plt.savefig("tiny_gnu_omp_8ppn_efficiency.pdf")
    plt.clf()

def tiny_gnu_omp_16ppn_time(times):
    times = np.log10(times)
    plt.title("Tiny suite - ThunderX2 - GNU Compiler - OMP Runtime (16 ranks/node)")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([2, 3.6])
    plt.plot([1,2,4,8], times.T[0], marker="x", label="lbm")
    plt.plot([1,2,4,8], times.T[1], marker="x", label="soma")
    plt.plot([1,2,4,8], times.T[2], marker="x", label="tealeaf")
    plt.plot([1,2,4,8], times.T[3], marker="x", label="clvleaf")
    plt.plot([1,2,4,8], times.T[4], marker="x", label="miniswp")
    plt.plot([1,2,4,8], times.T[5], marker="x", label="pot3d")
    plt.plot([1,2,4,8], times.T[6], marker="x", label="sph_exa")
    plt.plot([1,2,4,8], times.T[7], marker="x", label="hpgmgfv")
    plt.plot([1,2,4,8], times.T[8], marker="x", label="weather")
    plt.legend(loc="upper right")
    plt.xlabel("Number of nodes (64 cores/node)")
    plt.ylabel("$log_{10}$ Time(s)")
    plt.savefig("tiny_gnu_omp_16ppn_time.pdf")
    plt.clf()

def tiny_gnu_omp_16ppn_speedup(times):
    speedup = times[0]/times
    plt.title("Tiny suite - ThunderX2 - GNU Compiler - OMP Speedup (16 ranks/node)")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([1, 14])
    plt.plot(np.arange(0, 9), c="grey", linestyle="--")
    plt.plot([1,2,4,8], speedup.T[0], marker="x", label="lbm")
    plt.plot([1,2,4,8], speedup.T[1], marker="x", label="soma")
    plt.plot([1,2,4,8], speedup.T[2], marker="x", label="tealeaf")
    plt.plot([1,2,4,8], speedup.T[3], marker="x", label="clvleaf")
    plt.plot([1,2,4,8], speedup.T[4], marker="x", label="miniswp")
    plt.plot([1,2,4,8], speedup.T[5], marker="x", label="pot3d")
    plt.plot([1,2,4,8], speedup.T[6], marker="x", label="sph_exa")
    plt.plot([1,2,4,8], speedup.T[7], marker="x", label="hpgmgfv")
    plt.plot([1,2,4,8], speedup.T[8], marker="x", label="weather")
    plt.legend(loc="upper left")
    plt.xlabel("Number of nodes (64 cores/node)")
    plt.ylabel("Speedup")
    plt.savefig("tiny_gnu_omp_16ppn_speedup.pdf")
    plt.clf()

def tiny_gnu_omp_16ppn_efficiency(times):
    speedup = times[0]/times
    efficiency = speedup/np.array([[1],[2],[4],[8]]) * 100
    plt.title("Tiny suite - ThunderX2 - GNU Compiler - OMP Efficiency (16 ranks/node)")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([40, 140])
    plt.axhline(y=100, c="grey", linestyle="--")
    plt.plot([1,2,4,8], efficiency.T[0], marker="x", label="lbm")
    plt.plot([1,2,4,8], efficiency.T[1], marker="x", label="soma")
    plt.plot([1,2,4,8], efficiency.T[2], marker="x", label="tealeaf")
    plt.plot([1,2,4,8], efficiency.T[3], marker="x", label="clvleaf")
    plt.plot([1,2,4,8], efficiency.T[4], marker="x", label="miniswp")
    plt.plot([1,2,4,8], efficiency.T[5], marker="x", label="pot3d")
    plt.plot([1,2,4,8], efficiency.T[6], marker="x", label="sph_exa")
    plt.plot([1,2,4,8], efficiency.T[7], marker="x", label="hpgmgfv")
    plt.plot([1,2,4,8], efficiency.T[8], marker="x", label="weather")
    plt.legend(loc="lower left")
    plt.xlabel("Number of nodes (64 cores/node)")
    plt.ylabel("Parallel efficiency(%)")
    plt.savefig("tiny_gnu_omp_16ppn_efficiency.pdf")
    plt.clf()

def tiny_gnu_omp_32ppn_time(times):
    times = np.log10(times)
    plt.title("Tiny suite - ThunderX2 - GNU Compiler - OMP Runtime (32 ranks/node)")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([2, 3.6])
    plt.plot([1,2,4,8], times.T[0], marker="x", label="lbm")
    plt.plot([1,2,4,8], times.T[1], marker="x", label="soma")
    plt.plot([1,2,4,8], times.T[2], marker="x", label="tealeaf")
    plt.plot([1,2,4,8], times.T[3], marker="x", label="clvleaf")
    plt.plot([1,2,4,8], times.T[4], marker="x", label="miniswp")
    plt.plot([1,2,4,8], times.T[5], marker="x", label="pot3d")
    plt.plot([1,2,4,8], times.T[6], marker="x", label="sph_exa")
    plt.plot([1,2,4,8], times.T[7], marker="x", label="hpgmgfv")
    plt.plot([1,2,4,8], times.T[8], marker="x", label="weather")
    plt.legend(loc="upper right")
    plt.xlabel("Number of nodes (64 cores/node)")
    plt.ylabel("$log_{10}$ Time(s)")
    plt.savefig("tiny_gnu_omp_32ppn_time.pdf")
    plt.clf()

def tiny_gnu_omp_32ppn_speedup(times):
    speedup = times[0]/times
    plt.title("Tiny suite - ThunderX2 - GNU Compiler - OMP Speedup (32 ranks/node)")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([1, 14])
    plt.plot(np.arange(0, 9), c="grey", linestyle="--")
    plt.plot([1,2,4,8], speedup.T[0], marker="x", label="lbm")
    plt.plot([1,2,4,8], speedup.T[1], marker="x", label="soma")
    plt.plot([1,2,4,8], speedup.T[2], marker="x", label="tealeaf")
    plt.plot([1,2,4,8], speedup.T[3], marker="x", label="clvleaf")
    plt.plot([1,2,4,8], speedup.T[4], marker="x", label="miniswp")
    plt.plot([1,2,4,8], speedup.T[5], marker="x", label="pot3d")
    plt.plot([1,2,4,8], speedup.T[6], marker="x", label="sph_exa")
    plt.plot([1,2,4,8], speedup.T[7], marker="x", label="hpgmgfv")
    plt.plot([1,2,4,8], speedup.T[8], marker="x", label="weather")
    plt.legend(loc="upper left")
    plt.xlabel("Number of nodes (64 cores/node)")
    plt.ylabel("Speedup")
    plt.savefig("tiny_gnu_omp_32ppn_speedup.pdf")
    plt.clf()

def tiny_gnu_omp_32ppn_efficiency(times):
    speedup = times[0]/times
    efficiency = speedup/np.array([[1],[2],[4],[8]]) * 100
    plt.title("Tiny suite - ThunderX2 - GNU Compiler - OMP Efficiency (32 ranks/node)")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([40, 140])
    plt.axhline(y=100, c="grey", linestyle="--")
    plt.plot([1,2,4,8], efficiency.T[0], marker="x", label="lbm")
    plt.plot([1,2,4,8], efficiency.T[1], marker="x", label="soma")
    plt.plot([1,2,4,8], efficiency.T[2], marker="x", label="tealeaf")
    plt.plot([1,2,4,8], efficiency.T[3], marker="x", label="clvleaf")
    plt.plot([1,2,4,8], efficiency.T[4], marker="x", label="miniswp")
    plt.plot([1,2,4,8], efficiency.T[5], marker="x", label="pot3d")
    plt.plot([1,2,4,8], efficiency.T[6], marker="x", label="sph_exa")
    plt.plot([1,2,4,8], efficiency.T[7], marker="x", label="hpgmgfv")
    plt.plot([1,2,4,8], efficiency.T[8], marker="x", label="weather")
    plt.legend(loc="lower left")
    plt.xlabel("Number of nodes (64 cores/node)")
    plt.ylabel("Parallel efficiency(%)")
    plt.savefig("tiny_gnu_omp_32ppn_efficiency.pdf")
    plt.clf()

def tiny_gnu_total_time(times):
    times = np.log10(times)
    plt.title("Tiny suite - ThunderX2 - GNU Compiler - Total Runtime")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([3.2, 4.4])
    plt.plot([1,2,4,8], times[0], marker="x", label="1x64")
    plt.plot([1,2,4,8], times[1], marker="x", label="2x32")
    plt.plot([1,2,4,8], times[2], marker="x", label="4x16")
    plt.plot([1,2,4,8], times[3], marker="x", label="8x8")
    plt.plot([1,2,4,8], times[4], marker="x", label="64x1")
    plt.legend(loc="upper right")
    plt.xlabel("Number of nodes (64 cores/node)")
    plt.ylabel("$log_{10}$ Time(s)")
    plt.savefig("tiny_gnu_total_time.pdf")
    plt.clf()

def tiny_mpi_total_time(times):
    times = np.log10(times)
    plt.title("Tiny suite - ThunderX2 - MPI Total Runtime")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([3.2, 4.4])
    plt.plot([1,2,4,8], times[0], marker="x", label="GNU")
    plt.plot([1,2,4,8], times[1], marker="x", label="Cray")
    plt.plot([1,2,4,8], times[2], marker="x", label="Arm")
    plt.legend(loc="upper right")
    plt.xlabel("Number of nodes (64 cores/node)")
    plt.ylabel("$log_{10}$ Time(s)")
    plt.savefig("tiny_mpi_total_time.pdf")
    plt.clf()

def tiny_gnu_spec_score(scores):
    plt.title("Tiny suite - ThunderX2 - GNU Compiler - SPEC Score")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([0, 12])
    plt.plot([1,2,4,8], scores[0], marker="x", label="1x64")
    plt.plot([1,2,4,8], scores[1], marker="x", label="2x32")
    plt.plot([1,2,4,8], scores[2], marker="x", label="4x16")
    plt.plot([1,2,4,8], scores[3], marker="x", label="8x8")
    plt.plot([1,2,4,8], scores[4], marker="x", label="16x4")
    plt.plot([1,2,4,8], scores[5], marker="x", label="32x2")
    plt.plot([1,2,4,8], scores[6], marker="x", label="64x1")
    plt.legend(loc="upper left")
    plt.xlabel("Number of nodes (64 cores/node)")
    plt.ylabel("SPEC Score")
    plt.savefig("tiny_gnu_spec_score.pdf")   
    plt.clf() 

def main():
    tiny_gnu_mpi_times = np.array([[1253,1872,1043,942,1022,1370,1603,1051,1475],
                                   [633,990,558,482,687,702,792,532,764],
                                   [327,549,365,256,412,389,396,284,381],
                                   [166,332,197,139,308,214,209,167,212]])
    tiny_cray_mpi_times = np.array([[1475,1563,831,761,1155,1082,1543,833,1244],
                                    [743,913,635,493,805,737,821,646,651],
                                    [381,504,323,233,476,360,405,295,347],
                                    [195,316,194,131,363,211,217,182,190]])
    tiny_arm_mpi_times = np.array([[1491,1713,1018,936,1150,1340,1765,1035,1210],
                                   [751,908,584,484,774,691,871,558,604],
                                   [381,514,348,257,458,359,435,286,323],
                                   [195,314,191,140,346,209,232,172,167]])
    tiny_gnu_omp_1ppn_times = np.array([[1601,1847,1013,1067,786,2592,3705,1098,2574],
                                        [819,945,596,586,431,1362,1098,843,1300],
                                        [422,493,381,332,240,717,541,586,652],
                                        [213,266,272,192,159,395,271,431,348]])
    tiny_gnu_omp_2ppn_times = np.array([[1276,1865,1254,1582, 768,2076,1840,1590,2259],
                                        [635,907,563,571,398,884,928,676,1037],
                                        [321,475,333,313,257,508,453,414,455],
                                        [170,260,237,173,159,270,239,264,236]])
    tiny_gnu_omp_4ppn_times = np.array([[1269,1785,1056,1073,728,1682,1602,1209,2124],
                                        [629,917,557,563,437,874,843,644,925],
                                        [325,480,341,280,261,478,442,332,402],
                                        [169,266,212,157,174,256,235,207,208]])
    tiny_gnu_omp_8ppn_times = np.array([[1263,1802,1030,1005,823,1544,1580,1009,1726],
                                        [645,914,534,499,455,849,812,545,837],
                                        [328,484,345,274,295,422,427,309,387],
                                        [165,268,204,153,183,245,232,172,196]])
    tiny_gnu_omp_16ppn_times = np.array([[1275,1822,1027,982,846,1624,1546,1040,1659],
                                         [641,920,527,484,537,749,795,485,770],
                                         [318,500,350,273,321,440,433,304,380],
                                         [164,281,202,152,238,234,224,172,196]])
    tiny_gnu_omp_32ppn_times = np.array([[1269,1762,902,880,992,1159,1480,858,1423],
                                         [626,964,587,516,579,791,816,555,716],
                                         [320,518,371,268,416,411,409,293,370],
                                         [167,302,200,147,261,232,211,168,207]])
    tiny_gnu_total_times = np.array([tiny_gnu_omp_1ppn_times.sum(axis=1),
                                     tiny_gnu_omp_2ppn_times.sum(axis=1),
                                     tiny_gnu_omp_4ppn_times.sum(axis=1),
                                     tiny_gnu_omp_8ppn_times.sum(axis=1),
                                     tiny_gnu_omp_16ppn_times.sum(axis=1),
                                     tiny_gnu_omp_32ppn_times.sum(axis=1),
                                     tiny_gnu_mpi_times.sum(axis=1)])
    tiny_mpi_total_times = np.array([tiny_gnu_mpi_times.sum(axis=1),
                                     tiny_cray_mpi_times.sum(axis=1),
                                     tiny_arm_mpi_times.sum(axis=1)])
    tiny_gnu_spec_scores = np.array([[1.27,2.43,4.39,7.50],
                                      [1.31,2.88,5.28,9.24],
                                      [1.52,2.94,5.57,9.81],
                                      [1.60,3.08,5.66,10.2],
                                      [1.59,3.16,5.59,9.96],
                                      [1.75,3.02,5.49,9.84],
                                      [1.61,3.03,5.54,9.71]])
    tiny_gnu_mpi_time(tiny_gnu_mpi_times)
    tiny_gnu_mpi_speedup(tiny_gnu_mpi_times)
    tiny_gnu_mpi_efficiency(tiny_gnu_mpi_times)
    tiny_cray_mpi_time(tiny_cray_mpi_times)
    tiny_cray_mpi_speedup(tiny_cray_mpi_times)
    tiny_cray_mpi_efficiency(tiny_cray_mpi_times)
    tiny_arm_mpi_time(tiny_arm_mpi_times)
    tiny_arm_mpi_speedup(tiny_arm_mpi_times)
    tiny_arm_mpi_efficiency(tiny_arm_mpi_times)
    tiny_gnu_omp_1ppn_time(tiny_gnu_omp_1ppn_times)
    tiny_gnu_omp_1ppn_speedup(tiny_gnu_omp_1ppn_times)
    tiny_gnu_omp_1ppn_efficiency(tiny_gnu_omp_1ppn_times)
    tiny_gnu_omp_2ppn_time(tiny_gnu_omp_2ppn_times)
    tiny_gnu_omp_2ppn_speedup(tiny_gnu_omp_2ppn_times)
    tiny_gnu_omp_2ppn_efficiency(tiny_gnu_omp_2ppn_times)
    tiny_gnu_omp_4ppn_time(tiny_gnu_omp_4ppn_times)
    tiny_gnu_omp_4ppn_speedup(tiny_gnu_omp_4ppn_times)
    tiny_gnu_omp_4ppn_efficiency(tiny_gnu_omp_4ppn_times)
    tiny_gnu_omp_8ppn_time(tiny_gnu_omp_8ppn_times)
    tiny_gnu_omp_8ppn_speedup(tiny_gnu_omp_8ppn_times)
    tiny_gnu_omp_8ppn_efficiency(tiny_gnu_omp_8ppn_times)
    tiny_gnu_omp_16ppn_time(tiny_gnu_omp_16ppn_times)
    tiny_gnu_omp_16ppn_speedup(tiny_gnu_omp_16ppn_times)
    tiny_gnu_omp_16ppn_efficiency(tiny_gnu_omp_16ppn_times)
    tiny_gnu_omp_32ppn_time(tiny_gnu_omp_32ppn_times)
    tiny_gnu_omp_32ppn_speedup(tiny_gnu_omp_32ppn_times)
    tiny_gnu_omp_32ppn_efficiency(tiny_gnu_omp_32ppn_times)
    tiny_gnu_total_time(tiny_gnu_total_times)
    tiny_mpi_total_time(tiny_mpi_total_times)
    tiny_gnu_spec_score(tiny_gnu_spec_scores)

if __name__ == "__main__":
    main()
