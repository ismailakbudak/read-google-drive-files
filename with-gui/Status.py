class Status(object):
    uploaded=0
    uploaded_shared=1
    uploaded_could_not_shared=2
    could_not_uploaded=3
    uploaded_not_shared=4
    mapkey={
        0: "null",
        1: "The file uploaded and shared successfully..",
        2: "The file uploaded successfully.. But could not shared..",
        3: "The file could not uploaded...",
        4: "The file uploaded successfully but not shared..",
    }

    @staticmethod
    def getStatusText(status):
        return Status.mapkey[status]