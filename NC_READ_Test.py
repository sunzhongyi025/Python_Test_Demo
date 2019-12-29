import netCDF4 as nc

File_test = nc.Dataset('D:\Studies\Python_Sun\PY_NE_Test/CLASS-CTEM_S3_npp.nc')
# print(File_test.variables) #看看都有哪些变量及其属性
# print(File_test.variables.keys()) 看看变量的名字
NPP = File_test.variables['npp']
CLASS_CTM_NPP = NPP[:]
# print(CLASS_CTM_NPP.shape) 看看得到的变量的维数

Lon = File_test.variables['lon'][:]
Lat = File_test.variables['lat'][:]
time = File_test.variables['time'][:]

#times = nc.num2date(time, time.units)
