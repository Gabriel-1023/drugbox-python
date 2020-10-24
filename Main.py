import CodeDetect as cd

if __name__ == '__main__':
    CodeDetect = cd.CodeDetect()
    code = CodeDetect.detect()
    print(code)