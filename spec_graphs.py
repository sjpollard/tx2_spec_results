import numpy as np
from matplotlib import pyplot as plt

def time_tiny_gnu_results():
    times = np.array([[1253,1872,1043,942,1022,1370,1603,1051,1475],
                      [633,990,558,482,687,702,792,532,764],
                      [327,549,365,256,412,389,396,284,381],
                      [166,332,197,139,308,214,209,167,212]])
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

def speedup_tiny_gnu_results():
    times = np.array([[1253,1872,1043,942,1022,1370,1603,1051,1475],
                      [633,990,558,482,687,702,792,532,764],
                      [327,549,365,256,412,389,396,284,381],
                      [166,332,197,139,308,214,209,167,212]])
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

def efficiency_tiny_gnu_results():
    times = np.array([[1253,1872,1043,942,1022,1370,1603,1051,1475],
                      [633,990,558,482,687,702,792,532,764],
                      [327,549,365,256,412,389,396,284,381],
                      [166,332,197,139,308,214,209,167,212]])
    speedup = times[0]/times
    efficiency = speedup/np.array([[1],[2],[4],[8]]) * 100
    plt.title("Tiny suite - ThunderX2 - GNU Compiler - MPI (64 ranks/node)")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([40, 110])
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

def time_tiny_cray_results():
    times = np.array([[1475,1563,831,761,1155,1082,1543,833,1244],
                      [1351,927,584,463,801,712,809,593,648],
                      [381,504,323,233,476,360,405,295,347],
                      [195,316,194,131,363,211,217,182,190]])
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

def speedup_tiny_cray_results():
    times = np.array([[1475,1563,831,761,1155,1082,1543,833,1244],
                      [1351,927,584,463,801,712,809,593,648],
                      [381,504,323,233,476,360,405,295,347],
                      [195,316,194,131,363,211,217,182,190]])
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

def efficiency_tiny_cray_results():
    times = np.array([[1475,1563,831,761,1155,1082,1543,833,1244],
                      [1351,927,584,463,801,712,809,593,648],
                      [381,504,323,233,476,360,405,295,347],
                      [195,316,194,131,363,211,217,182,190]])
    speedup = times[0]/times
    efficiency = speedup/np.array([[1],[2],[4],[8]]) * 100
    plt.title("Tiny suite - ThunderX2 - Cray Compiler - MPI (64 ranks/node)")
    plt.xticks([1,2,4,8])
    plt.xlim([1, 8])
    plt.ylim([40, 110])
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

def main():
    #time_tiny_gnu_results()
    #speedup_tiny_gnu_results()
    #efficiency_tiny_gnu_results()
    #time_tiny_cray_results()
    #speedup_tiny_cray_results()
    #efficiency_tiny_cray_results()

if __name__ == "__main__":
    main()
