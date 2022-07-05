import numpy as np
from matplotlib import pyplot as plt

def tiny_gnu_mpi_time(times):
    plt.title("Tiny suite - ThunderX2 - GNU Compiler - MPI (64 ranks/node)")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([0, 2000])
    plt.plot([1,2,4,8], times.T[0], marker="x", label="505.lbm_t")
    plt.plot([1,2,4,8], times.T[1], marker="x", label="513.soma_t")
    plt.plot([1,2,4,8], times.T[2], marker="x", label="518.tealeaf_t")
    plt.plot([1,2,4,8], times.T[3], marker="x", label="519.clvleaf_t")
    plt.plot([1,2,4,8], times.T[4], marker="x", label="521.miniswp_t")
    plt.plot([1,2,4,8], times.T[5], marker="x", label="528.pot3d_t")
    plt.plot([1,2,4,8], times.T[6], marker="x", label="532.sph_exa_t")
    plt.plot([1,2,4,8], times.T[7], marker="x", label="534.hpgmgfv_t")
    plt.plot([1,2,4,8], times.T[8], marker="x", label="535.weather_t")
    plt.legend(loc="upper right")
    plt.xlabel("Number of nodes (64 cores/node)")
    plt.ylabel("Time(s)")
    plt.show()

def tiny_gnu_mpi_speedup(times):
    speedup = times[0]/times
    plt.title("Tiny suite - ThunderX2 - GNU Compiler - MPI (64 ranks/node)")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([1, 8])
    plt.plot(np.arange(0, 9), c="grey", linestyle="--")
    plt.plot([1,2,4,8], speedup.T[0], marker="x", label="505.lbm_t")
    plt.plot([1,2,4,8], speedup.T[1], marker="x", label="513.soma_t")
    plt.plot([1,2,4,8], speedup.T[2], marker="x", label="518.tealeaf_t")
    plt.plot([1,2,4,8], speedup.T[3], marker="x", label="519.clvleaf_t")
    plt.plot([1,2,4,8], speedup.T[4], marker="x", label="521.miniswp_t")
    plt.plot([1,2,4,8], speedup.T[5], marker="x", label="528.pot3d_t")
    plt.plot([1,2,4,8], speedup.T[6], marker="x", label="532.sph_exa_t")
    plt.plot([1,2,4,8], speedup.T[7], marker="x", label="534.hpgmgfv_t")
    plt.plot([1,2,4,8], speedup.T[8], marker="x", label="535.weather_t")
    plt.legend(loc="upper left")
    plt.xlabel("Number of nodes (64 cores/node)")
    plt.ylabel("Speedup")
    plt.show()

def tiny_gnu_mpi_efficiency(times):
    speedup = times[0]/times
    efficiency = speedup/np.array([[1],[2],[4],[8]]) * 100
    plt.title("Tiny suite - ThunderX2 - GNU Compiler - MPI (64 ranks/node)")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([35, 105])
    plt.plot([1,2,4,8], efficiency.T[0], marker="x", label="505.lbm_t")
    plt.plot([1,2,4,8], efficiency.T[1], marker="x", label="513.soma_t")
    plt.plot([1,2,4,8], efficiency.T[2], marker="x", label="518.tealeaf_t")
    plt.plot([1,2,4,8], efficiency.T[3], marker="x", label="519.clvleaf_t")
    plt.plot([1,2,4,8], efficiency.T[4], marker="x", label="521.miniswp_t")
    plt.plot([1,2,4,8], efficiency.T[5], marker="x", label="528.pot3d_t")
    plt.plot([1,2,4,8], efficiency.T[6], marker="x", label="532.sph_exa_t")
    plt.plot([1,2,4,8], efficiency.T[7], marker="x", label="534.hpgmgfv_t")
    plt.plot([1,2,4,8], efficiency.T[8], marker="x", label="535.weather_t")
    plt.legend(loc="lower left")
    plt.xlabel("Number of nodes (64 cores/node)")
    plt.ylabel("Parallel efficiency")
    plt.show()

def tiny_cray_mpi_time(times):
    plt.title("Tiny suite - ThunderX2 - Cray Compiler - MPI (64 ranks/node)")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([0, 2000])
    plt.plot([1,2,4,8], times.T[0], marker="x", label="505.lbm_t")
    plt.plot([1,2,4,8], times.T[1], marker="x", label="513.soma_t")
    plt.plot([1,2,4,8], times.T[2], marker="x", label="518.tealeaf_t")
    plt.plot([1,2,4,8], times.T[3], marker="x", label="519.clvleaf_t")
    plt.plot([1,2,4,8], times.T[4], marker="x", label="521.miniswp_t")
    plt.plot([1,2,4,8], times.T[5], marker="x", label="528.pot3d_t")
    plt.plot([1,2,4,8], times.T[6], marker="x", label="532.sph_exa_t")
    plt.plot([1,2,4,8], times.T[7], marker="x", label="534.hpgmgfv_t")
    plt.plot([1,2,4,8], times.T[8], marker="x", label="535.weather_t")
    plt.legend(loc="upper right")
    plt.xlabel("Number of nodes (64 cores/node)")
    plt.ylabel("Time(s)")
    plt.show()

def tiny_cray_mpi_speedup(times):
    speedup = times[0]/times
    plt.title("Tiny suite - ThunderX2 - Cray Compiler - MPI (64 ranks/node)")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([1, 8])
    plt.plot(np.arange(0, 9), c="grey", linestyle="--")
    plt.plot([1,2,4,8], speedup.T[0], marker="x", label="505.lbm_t")
    plt.plot([1,2,4,8], speedup.T[1], marker="x", label="513.soma_t")
    plt.plot([1,2,4,8], speedup.T[2], marker="x", label="518.tealeaf_t")
    plt.plot([1,2,4,8], speedup.T[3], marker="x", label="519.clvleaf_t")
    plt.plot([1,2,4,8], speedup.T[4], marker="x", label="521.miniswp_t")
    plt.plot([1,2,4,8], speedup.T[5], marker="x", label="528.pot3d_t")
    plt.plot([1,2,4,8], speedup.T[6], marker="x", label="532.sph_exa_t")
    plt.plot([1,2,4,8], speedup.T[7], marker="x", label="534.hpgmgfv_t")
    plt.plot([1,2,4,8], speedup.T[8], marker="x", label="535.weather_t")
    plt.legend(loc="upper left")
    plt.xlabel("Number of nodes (64 cores/node)")
    plt.ylabel("Speedup")
    plt.show()

def tiny_cray_mpi_efficiency(times):
    speedup = times[0]/times
    efficiency = speedup/np.array([[1],[2],[4],[8]]) * 100
    plt.title("Tiny suite - ThunderX2 - Cray Compiler - MPI (64 ranks/node)")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([35, 105])
    plt.plot([1,2,4,8], efficiency.T[0], marker="x", label="505.lbm_t")
    plt.plot([1,2,4,8], efficiency.T[1], marker="x", label="513.soma_t")
    plt.plot([1,2,4,8], efficiency.T[2], marker="x", label="518.tealeaf_t")
    plt.plot([1,2,4,8], efficiency.T[3], marker="x", label="519.clvleaf_t")
    plt.plot([1,2,4,8], efficiency.T[4], marker="x", label="521.miniswp_t")
    plt.plot([1,2,4,8], efficiency.T[5], marker="x", label="528.pot3d_t")
    plt.plot([1,2,4,8], efficiency.T[6], marker="x", label="532.sph_exa_t")
    plt.plot([1,2,4,8], efficiency.T[7], marker="x", label="534.hpgmgfv_t")
    plt.plot([1,2,4,8], efficiency.T[8], marker="x", label="535.weather_t")
    plt.legend(loc="lower left")
    plt.xlabel("Number of nodes (64 cores/node)")
    plt.ylabel("Parallel efficiency")
    plt.show()

def tiny_arm_mpi_time(times):
    plt.title("Tiny suite - ThunderX2 - Arm Compiler - MPI (64 ranks/node)")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([0, 2000])
    plt.plot([1,2,4,8], times.T[0], marker="x", label="505.lbm_t")
    plt.plot([1,2,4,8], times.T[1], marker="x", label="513.soma_t")
    plt.plot([1,2,4,8], times.T[2], marker="x", label="518.tealeaf_t")
    plt.plot([1,2,4,8], times.T[3], marker="x", label="519.clvleaf_t")
    plt.plot([1,2,4,8], times.T[4], marker="x", label="521.miniswp_t")
    plt.plot([1,2,4,8], times.T[5], marker="x", label="528.pot3d_t")
    plt.plot([1,2,4,8], times.T[6], marker="x", label="532.sph_exa_t")
    plt.plot([1,2,4,8], times.T[7], marker="x", label="534.hpgmgfv_t")
    plt.plot([1,2,4,8], times.T[8], marker="x", label="535.weather_t")
    plt.legend(loc="upper right")
    plt.xlabel("Number of nodes (64 cores/node)")
    plt.ylabel("Time(s)")
    plt.show()

def tiny_arm_mpi_speedup(times):
    speedup = times[0]/times
    plt.title("Tiny suite - ThunderX2 - Arm Compiler - MPI (64 ranks/node)")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([1, 8])
    plt.plot(np.arange(0, 9), c="grey", linestyle="--")
    plt.plot([1,2,4,8], speedup.T[0], marker="x", label="505.lbm_t")
    plt.plot([1,2,4,8], speedup.T[1], marker="x", label="513.soma_t")
    plt.plot([1,2,4,8], speedup.T[2], marker="x", label="518.tealeaf_t")
    plt.plot([1,2,4,8], speedup.T[3], marker="x", label="519.clvleaf_t")
    plt.plot([1,2,4,8], speedup.T[4], marker="x", label="521.miniswp_t")
    plt.plot([1,2,4,8], speedup.T[5], marker="x", label="528.pot3d_t")
    plt.plot([1,2,4,8], speedup.T[6], marker="x", label="532.sph_exa_t")
    plt.plot([1,2,4,8], speedup.T[7], marker="x", label="534.hpgmgfv_t")
    plt.plot([1,2,4,8], speedup.T[8], marker="x", label="535.weather_t")
    plt.legend(loc="upper left")
    plt.xlabel("Number of nodes (64 cores/node)")
    plt.ylabel("Speedup")
    plt.show()

def tiny_arm_mpi_efficiency(times):
    speedup = times[0]/times
    efficiency = speedup/np.array([[1],[2],[4],[8]]) * 100
    plt.title("Tiny suite - ThunderX2 - Arm Compiler - MPI (64 ranks/node)")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([35, 105])
    plt.plot([1,2,4,8], efficiency.T[0], marker="x", label="505.lbm_t")
    plt.plot([1,2,4,8], efficiency.T[1], marker="x", label="513.soma_t")
    plt.plot([1,2,4,8], efficiency.T[2], marker="x", label="518.tealeaf_t")
    plt.plot([1,2,4,8], efficiency.T[3], marker="x", label="519.clvleaf_t")
    plt.plot([1,2,4,8], efficiency.T[4], marker="x", label="521.miniswp_t")
    plt.plot([1,2,4,8], efficiency.T[5], marker="x", label="528.pot3d_t")
    plt.plot([1,2,4,8], efficiency.T[6], marker="x", label="532.sph_exa_t")
    plt.plot([1,2,4,8], efficiency.T[7], marker="x", label="534.hpgmgfv_t")
    plt.plot([1,2,4,8], efficiency.T[8], marker="x", label="535.weather_t")
    plt.legend(loc="lower left")
    plt.xlabel("Number of nodes (64 cores/node)")
    plt.ylabel("Parallel efficiency")
    plt.show()

def tiny_gnu_omp_1ppn_time(times):
    plt.title("Tiny suite - ThunderX2 - GNU Compiler - OMP (1 rank/node)")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([0, 4000])
    plt.plot([1,2,4,8], times.T[0], marker="x", label="505.lbm_t")
    plt.plot([1,2,4,8], times.T[1], marker="x", label="513.soma_t")
    plt.plot([1,2,4,8], times.T[2], marker="x", label="518.tealeaf_t")
    plt.plot([1,2,4,8], times.T[3], marker="x", label="519.clvleaf_t")
    plt.plot([1,2,4,8], times.T[4], marker="x", label="521.miniswp_t")
    plt.plot([1,2,4,8], times.T[5], marker="x", label="528.pot3d_t")
    plt.plot([1,2,4,8], times.T[6], marker="x", label="532.sph_exa_t")
    plt.plot([1,2,4,8], times.T[7], marker="x", label="534.hpgmgfv_t")
    plt.plot([1,2,4,8], times.T[8], marker="x", label="535.weather_t")
    plt.legend(loc="upper right")
    plt.xlabel("Number of nodes (64 cores/node)")
    plt.ylabel("Time(s)")
    plt.show()

def tiny_gnu_omp_2ppn_time(times):
    plt.title("Tiny suite - ThunderX2 - GNU Compiler - OMP (2 ranks/node)")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([0, 2500])
    plt.plot([1,2,4,8], times.T[0], marker="x", label="505.lbm_t")
    plt.plot([1,2,4,8], times.T[1], marker="x", label="513.soma_t")
    plt.plot([1,2,4,8], times.T[2], marker="x", label="518.tealeaf_t")
    plt.plot([1,2,4,8], times.T[3], marker="x", label="519.clvleaf_t")
    plt.plot([1,2,4,8], times.T[4], marker="x", label="521.miniswp_t")
    plt.plot([1,2,4,8], times.T[5], marker="x", label="528.pot3d_t")
    plt.plot([1,2,4,8], times.T[6], marker="x", label="532.sph_exa_t")
    plt.plot([1,2,4,8], times.T[7], marker="x", label="534.hpgmgfv_t")
    plt.plot([1,2,4,8], times.T[8], marker="x", label="535.weather_t")
    plt.legend(loc="upper right")
    plt.xlabel("Number of nodes (64 cores/node)")
    plt.ylabel("Time(s)")
    plt.show()

def tiny_gnu_omp_4ppn_time(times):
    plt.title("Tiny suite - ThunderX2 - GNU Compiler - OMP (4 ranks/node)")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([0, 2500])
    plt.plot([1,2,4,8], times.T[0], marker="x", label="505.lbm_t")
    plt.plot([1,2,4,8], times.T[1], marker="x", label="513.soma_t")
    plt.plot([1,2,4,8], times.T[2], marker="x", label="518.tealeaf_t")
    plt.plot([1,2,4,8], times.T[3], marker="x", label="519.clvleaf_t")
    plt.plot([1,2,4,8], times.T[4], marker="x", label="521.miniswp_t")
    plt.plot([1,2,4,8], times.T[5], marker="x", label="528.pot3d_t")
    plt.plot([1,2,4,8], times.T[6], marker="x", label="532.sph_exa_t")
    plt.plot([1,2,4,8], times.T[7], marker="x", label="534.hpgmgfv_t")
    plt.plot([1,2,4,8], times.T[8], marker="x", label="535.weather_t")
    plt.legend(loc="upper right")
    plt.xlabel("Number of nodes (64 cores/node)")
    plt.ylabel("Time(s)")
    plt.show()

def tiny_gnu_omp_8ppn_time(times):
    plt.title("Tiny suite - ThunderX2 - GNU Compiler - OMP (8 ranks/node)")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([0, 2000])
    plt.plot([1,2,4,8], times.T[0], marker="x", label="505.lbm_t")
    plt.plot([1,2,4,8], times.T[1], marker="x", label="513.soma_t")
    plt.plot([1,2,4,8], times.T[2], marker="x", label="518.tealeaf_t")
    plt.plot([1,2,4,8], times.T[3], marker="x", label="519.clvleaf_t")
    plt.plot([1,2,4,8], times.T[4], marker="x", label="521.miniswp_t")
    plt.plot([1,2,4,8], times.T[5], marker="x", label="528.pot3d_t")
    plt.plot([1,2,4,8], times.T[6], marker="x", label="532.sph_exa_t")
    plt.plot([1,2,4,8], times.T[7], marker="x", label="534.hpgmgfv_t")
    plt.plot([1,2,4,8], times.T[8], marker="x", label="535.weather_t")
    plt.legend(loc="upper right")
    plt.xlabel("Number of nodes (64 cores/node)")
    plt.ylabel("Time(s)")
    plt.show()

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
    #tiny_gnu_mpi_time(tiny_gnu_mpi_times)
    #tiny_gnu_mpi_speedup(tiny_gnu_mpi_times)
    #tiny_gnu_mpi_efficiency(tiny_gnu_mpi_times)
    #tiny_cray_mpi_time(tiny_cray_mpi_times)
    #tiny_cray_mpi_speedup(tiny_cray_mpi_times)
    #tiny_cray_mpi_efficiency(tiny_cray_mpi_times)
    #tiny_arm_mpi_time(tiny_arm_mpi_times)
    #tiny_arm_mpi_speedup(tiny_arm_mpi_times)
    #tiny_arm_mpi_efficiency(tiny_arm_mpi_times)
    #tiny_gnu_omp_1ppn_time(tiny_gnu_omp_1ppn_times)
    #tiny_gnu_omp_2ppn_time(tiny_gnu_omp_2ppn_times)
    #tiny_gnu_omp_4ppn_time(tiny_gnu_omp_4ppn_times)
    #tiny_gnu_omp_8ppn_time(tiny_gnu_omp_8ppn_times)

if __name__ == "__main__":
    main()