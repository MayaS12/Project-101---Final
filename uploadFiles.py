import dropbox
import os

class TransferData:
        def __init__(self, access_token):
            self.access_token = access_token

        def uploadFile(self, fileFrom, fileTo):
            dbx = dropbox.Dropbox(self.access_token)
            f = open(fileFrom, 'rb')
            for root, dirs, files in os.walk(fileFrom):

                for filename in files:
                    # construct the full local path
                    local_path = os.path.join(root, filename)

                    # construct the full Dropbox path
                    relative_path = os.path.relpath(local_path, fileFrom)
                    dropbox_path = os.path.join(fileTo, relative_path)
                    # upload the file
                    dbx.files_upload(f.read(), fileTo)

def main():
        access_token = "72YF2_O9r3oAAAAAAAAAAaHNGIVb1Ric4P2ZuRO5UHs2PS1mDnYqGX5IR6hgkZmf"

        transferData = TransferData(access_token)

        fileFrom = input("Enter file path")
        fileTo = input("Enter the dropbox path")

        transferData.uploadFile(fileFrom, fileTo)

        print("File completed")

main()