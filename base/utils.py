class Utils:
    @classmethod
    def save_into_file(cls, result, file):

        with open(file, "r+") as f:
            s = f.read()
            f.seek(0)
            f.write(str(result) + "\n" + str(s))
