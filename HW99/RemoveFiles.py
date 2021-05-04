import os
import shutil
import time

def main ():
    deleted_folders_count=0
    deleted_files_count  =0
    path = "/Users/pavi/Desktop/PY/HW99/delete.txt"
    days = 30
    seconds =  time.time()-(days*24*60*60)
    if os.path.exists(path):
        for root_folder,folders,files in os.walk(path):
            if seconds>=get_file_or_folder_age(root_folder):
                remove_folder(root_folder)
                deleted_folders_count+=1
                break
            else:
                for folder in folders:
                    folder_path=os.path.join(root_folder,folder)
                    if seconds>=get_file_or_folder_age(folder_path):
                        remove_folder(folder_path)
                        deleted_folders_count+=1
                for file in files:
                    file_path=os.path.join(root_folder,file)
                    if seconds>=get_file_or_folder_age(file_path):
                        remove_file(file_path)
                        deleted_files_count+=1
    else:
        if seconds>=get_file_or_folder_age(path):
            remove_file(path)
            deleted_files_count+=1
        else:
            print("{path}is not found")
            deleted_files_count+=1
    print("Total folders deleted:{deleted_folders_count}")
    print("Total files deleted:{deleted_files_count}")

def remove_folder(path):
    if not shutil.rmtree(path):
        print("{path} is successfully removed")
    else:
        print("{path} is unable to remove")

def remove_file(path):
    if not os.remove(path):
        print("{path} is successfully removed")
    else:
        print("{path} is unable to remove")

def get_file_or_folder_age(path):
    ctime=os.stat(path).st_ctime
    return ctime

if __name__ == '__main__':
    main()




        

