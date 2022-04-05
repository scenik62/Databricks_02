#display(dbutils.fs.ls("dbfs:/FileStore/tables/"))
# DIR  zip.printdir()
# importing required modules
from zipfile import ZipFile
  
# specifying the zip file name
#file_name = "/dbfs/FileStore/tables/ZIP/test_01.zip"
file_name = "/dbfs/FileStore/tables/test.zip"
  
# opening the zip file in READ mode
with ZipFile(file_name, 'r') as zip:
    # printing all the contents of the zip file
    zip.printdir()
  
    # extracting all the files
    print('Extracting all the files now...')
    zip.extractall("/dbfs/tmp/capi/ZIP")
    print('Done!')
    display(dbutils.fs.ls("dbfs:/tmp/capi/ZIP"))
