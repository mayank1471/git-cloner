import os

keystore_path = os.path.join(os.getcwd(), 'keystore')
working_dir_path = os.path.join(os.getcwd(), 'workspace')


def clear_working_path():
    directory_list = os.listdir()
    delete_list = []
    ignore_list = ["GitUtils.py", "main.py", "test_main.http", "venv", ".idea", "__pycache__"]
    for file_name in directory_list:
        if file_name in ignore_list:
            continue
        else:
            delete_list.append(os.path.join(os.getcwd(), file_name))
    command = f"rm -rf {' '.join(delete_list)}"
    os.system(command)


def clone_and_mirror_repository(source_repository_url, destination_repository_url):
    clear_working_path()
    command = f"git clone {source_repository_url}"
    default_branch_to_push = "master"
    project_name = extract_project_name(source_repository_url)
    os.system(command)
    command = f"cd {project_name} && git checkout {default_branch_to_push} && git push --mirror {destination_repository_url}"
    os.system(command)
    clear_working_path()


def extract_project_name(source_repository_url: str):
    project_git_identifier = source_repository_url.split("/")[-1]
    project_name = project_git_identifier[:project_git_identifier.index(".git")]
    return project_name
