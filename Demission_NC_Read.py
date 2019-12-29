import netCDF4 as nc

File_test = nc.Dataset('D:\Studies\Python_Sun\PY_NE_Test/CLASS-CTEM_S3_npp.nc')
NPP = File_test.variables['npp']
CLASS_CTM_NPP = NPP[:10, 10:11, 20:45] #按照维度去读取数据
print(CLASS_CTM_NPP.shape)

