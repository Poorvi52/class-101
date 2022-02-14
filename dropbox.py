import dropbox

class TransferData:
    def __init__(self,accessToken):
        self.accessToken=accessToken
    def upload_file(self,fileFrom,fileTo):
        dpx=dropbox.Dropbox(self.accessToken) 
        f=open(fileFrom,"rb")
        dpx.files_upload(f.read(),fileTo)  
def main():
    accessToken="sl.BCDN-3mvgN1B7m8xDpp0mLjYQM5GhQoHPlQUU8A3rPIzkb2yREPwjXnjq-YUueWXxymN6XPHOwOa6JGr1xzkBEsG87BhjoTppn0V133rcVzqjLomqu_kRBGYlm2z6y4RZc7zRKU"
    transferData=TransferData(accessToken)
    fileFrom=input("Enter the path to be transferred: ")  
    fileTo=input("Enter the path to upload the dropbox: ")    
    transferData.upload_file(fileFrom, fileTo)
    print("File has been moved!")
main()