import sys


"""
Populate a url

:param url: 

:param file: path to a file that contains string in the following format:
- lcitool: Add support for engine
- docs: Documentation for containers

: param commit_hash_file: a file that contains string in the following format:
commit 728886
commit 77r747


:returns:
    - [lcitool: Add support for engine](https://gitlab.com/mrbazzan/libvirt-ci/-/commit/77r747)
    - [docs: Documentation for containers](https://gitlab.com/mrbazzan/libvirt-ci/-/commit/728886)

"""


def markdown(url, file, commit_hash_file):
    commit_list = open(commit_hash_file).readlines()
    commit_list = list(map(lambda x: x.strip().strip('commit '), open(commit_hash_file)))
    
    file_length = len(commit_list)
    url_list = []

    for i, commit_hash in enumerate(commit_list):
        url_list.append(url+commit_list[file_length-i-1])

    index=0
    for i in open(file, newline=""):
        hypen, need = i.split("- ")
        print("- " + "[" + need.strip() + f"]({url_list[index]})")
        index+=1


markdown(
    "https://gitlab.com/mrbazzan/libvirt-ci/-/commit/"
    sys.argv[1], sys.argv[2]
)

