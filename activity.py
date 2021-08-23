import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A3GL1qZ3EpwPv3S9_UWqf1koHcM2rOgEhn00wc8Xc1Ss7ltvfmOdU9KlAknvYnJNgAOTwWxXLZLwjrg3vIDZHaTKxDK30haRg92ErAffOJF68d2jVQVKzYVmKo6N2L3GMcewnoubDBM'
    transferData = TransferData(access_token)

    file_from = input("Enter the file to transfer")
    file_to = input("Enter the path to upload to the dropbox")

    # API v2
    transferData.upload_file(file_from, file_to)
    print("File has been moved")

if __name__ == '__main__':
    main()