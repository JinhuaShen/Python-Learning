# note that this is not tested

import platform
import shutil
def ispython2x():
    python_ver = platform.python_version_tuple()
    if int(python_ver[0])<3:
        return True
    return False

def url_lib():
    #We want to remain compatible with python2.7 on Mac
    if ispython2x():
        import urllib
        return urllib
    import urllib.request
    return urllib.request


def downloadExtractorBuild():
    # Get the latest build
    url = ""
    file = url_lib().urlretrieve (url, "example.zip")
    
def main():
    downloadExtractorBuild2()


if __name__ == "__main__":
    main()
