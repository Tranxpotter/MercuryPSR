import os
for file_name in os.listdir("test"):
    os.remove(f"test/{file_name}")
    
for file_name in os.listdir("lat_lon_log"):
    os.remove(f"lat_lon_log/{file_name}")