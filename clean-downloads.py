from pathlib import Path
import difflib


def get_directory(url_str:str):
    return Path.home().joinpath(url_str)


def show_directory_tree():
    home_folder = Path.home()
    print("Heres your directory tree you can choose from here")
    for item in home_folder.glob("*"):
        if item.is_dir() and not item.name.startswith("."):
            print(item)    


def recommend_match(mismatched_path, home_reference):
    # Get the names of directories in the home_reference directory
    directory_names = [directory.name for directory in home_reference.iterdir() if directory.is_dir()]

    # Find the closest match to the mismatched path among the directory names
    closest_match = difflib.get_close_matches(mismatched_path, directory_names, n=1)
    if closest_match:
        return closest_match[0]
    else:
        return None


def select_dir(sub_dirs):
    folder_choice = input("Type in your folder: ")
    # check if the subdirectory from the list dir function exists
    if folder_choice in sub_dirs:
        print(f"You selected the folder: {folder_choice}")
    else:
        print("Invalid choice. Please try again.")
        select_dir(sub_dirs)  # Recursively ask for input again

def list_dir(destination_directory):
    sub_dirs = []
    print("Listing your directories:")
    for subdir in destination_directory.glob("*"):
        if subdir.is_dir() and not subdir.name.startswith("."):
            sub_dirs.append(subdir.name)
            print(type(sub_dirs))
            print(subdir.name + " (dir)")
    
    if sub_dirs:
        select_dir(sub_dirs)
    else:
        print("No directories found.")


def errorMessage()-> None:
    print("Invalid choice. Please enter Yes, No, Y, or N.")



def create_dir(file_location: Path, new_folder_name: str):
    new_dir_path = file_location / new_folder_name
    try:
        new_dir_path.mkdir(parents=True, exist_ok=False)
        print(f"Directory '{new_folder_name}' created at {destination_directory}")
    except FileExistsError:
        print(f"Directory '{new_folder_name}' already exists at {destination_directory}")
    except Exception as e:
        print(f"An error occurred: {e}")

# show listed dir and also creates dir from choice
def cleanup(target_directory: Path, destination_directory: Path):
    choice = input("Do you want to create a new directory or continue with your old one? Y/N: ")
    # handles the input for both Yes/No and Y/N cases
    choice = choice.strip().capitalize()
    
    if choice in ["Yes", "Y"]:
        # Code for creating a new directory
        path_name = input("What would you like to name the path (Insert name): ")
        print(f"your current path is '{destination_directory}'")
        create_dir(destination_directory, path_name)
        # Add your logic here
    elif choice in ["No", "N"]:
        list_dir(destination_directory)
    else:
        errorMessage()

# This makes sure all the given paths exists
def path_exists(target_directory: Path, destination_directory: Path):
    target_exists = target_directory.exists()
    destination_exists = destination_directory.exists()

    if target_exists and destination_exists:
        return cleanup(target_directory, destination_directory)

    elif target_exists:
        recommendation = recommend_match(destination_directory.name, Path.home())
        option = input(F"The destination directory '{destination_directory}' does not exist. did you mean {recommendation}? Y/N: ")
        option = option.strip().capitalize()

        if option in ["N", "No"]:
            return
        elif option in ["Y","Yes"]:
            return cleanup(target_directory, destination_directory)
        else:
            errorMessage()

    elif destination_exists:
        recommendation = recommend_match(target_directory.name, Path.home())
        option =  input(f"The target directory '{target_directory}' does not seem to exist sorry did you mean {recommendation}? Y/N: ")
        option = option.strip().capitalize()

        if option in ["N", "No"]:
            return
        elif option in ["Y","Yes"]:
            return cleanup(target_directory, destination_directory)
        else:
            errorMessage()
        
    else:
        return show_directory_tree()
    

if __name__ == "__main__":
    try:
        target_string = input("Insert your target Folder name (e.g Videos): ")
        # get the target directory
        target_dir = get_directory(target_string.capitalize())
        
        destination_string = input("Insert your Destination Folder name (e.g Videos): ")
        # get the destination folder
        destination_dir = get_directory(destination_string.capitalize())
        # turn it into a POSIX path object
        target_directory = Path(target_dir)
        destination_directory = Path(destination_dir)

        #check if the both files exist
        print(path_exists(target_directory, destination_directory))
    except KeyboardInterrupt:
        print("\nOops you cancelled, come again some other time :)")


