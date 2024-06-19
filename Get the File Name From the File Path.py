#######################Using os.path.basename()#####################################
import os

def get_file_name_from_path(file_path):
    return os.path.basename(file_path)

# Example usage:
if __name__ == "__main__":
    file_path = "/path/to/file/example.txt"
    file_name = get_file_name_from_path(file_path)
    print(f"File name from path '{file_path}': '{file_name}'")


# ######################Using split() and [-1] indexing#########################################################
#
# def get_file_name_from_path(file_path):
#     return os.path.basename(file_path)
#
# # Example usage:
# if __name__ == "__main__":
#     file_path = "/path/to/file/example.txt"
#     file_name = get_file_name_from_path(file_path)
#     print(f"File name from path '{file_path}': '{file_name}'")
#
# ######################Using os.path.split()#########################################################
# def get_file_name_from_split(file_path):
#     return os.path.split(file_path)[1]
#
# # Example usage:
# if __name__ == "__main__":
#     file_path = "/path/to/file/example.txt"
#     file_name = get_file_name_from_split(file_path)
#     print(f"File name from path '{file_path}': '{file_name}'")
