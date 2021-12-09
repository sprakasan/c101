import dropbox
import os
class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            for name in files:
                local_path=os.path.join(root,file_name)
                relative_path=os.path.reltath(local_path,file_from)
                dropbox_path=os.path.join(file_to,relative_path)
                with open(local_path,'rb') as f:
                        dbx.files_upload(f.read(),dropbox_path)
def main():
    access_token= "sl.A91XuvMJlzVoyWpMdNUs0t6SLAgy7L5exo4cq8erw3Mma8PYhIBhXEzVbXbgbIleGxeUTOOHUNCKLfJxsFXFP-qeqWkDHv3YwYw85lfivyFw-3tBNl9QlpMmzQpUQ_BttU-IFJU"
    tdata = TransferData(access_token)
    
    file_from = input("Enter the name of the file you want to transfer.")
    file_to = input("Enter the path to upload to Dropbox")

    tdata.upload_file(file_from,file_to)
    print("File has been moved.")

main()
