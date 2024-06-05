from pathlib import Path
import difflib

# INSTRUCTIONS
# request for a target directory {@param str}
# request for a destination directory {@param str}
# have a collection of extentions 
# check if the file matches any of the extentions if it does then move them to a new directory
# display a success message if it succeeded else return a failure message




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


def list_dir(dir_subdir):
    print("Listing Your directories")
    dir_subdir = destination_directory.glob("*")    
    for subdir in dir_subdir:
        if subdir.is_dir() and not subdir.name.startswith("."):
            print(subdir)


def cleanup(target_directory: Path, destination_directory: Path):
    choice = input("Do you want to create a new directory or continue with your old one? Y/N: ")

    # handles the input for both Yes/No and Y/N cases
    choice = choice.strip().capitalize()
    
    if choice in ["Yes", "Y"]:
        # Code for creating a new directory
        print("Creating a new directory...")
        # Add your logic here
    elif choice in ["No", "N"]:
        list_dir(destination_directory)
    else:
        print("Invalid choice. Please enter Yes, No, Y, or N.")

# This makes sure all the given paths exists
def path_exists(target_directory: Path, destination_directory: Path):
    target_exists = target_directory.exists()
    destination_exists = destination_directory.exists()

    if target_exists and destination_exists:
        return cleanup(target_directory, destination_directory)

    elif target_exists:
        recommendation = recommend_match(destination_directory.name, Path.home())
        return f"The destination directory '{destination_directory}' does not exist. did you mean {recommendation}?"
    elif destination_exists:
        recommendation = recommend_match(target_directory.name, Path.home())
        return f"The target directory '{target_directory}' does not seem to exist sorry did you mean {recommendation}?"
    else:
        return show_directory_tree()
    

if __name__ == "__main__":
    try:
        target_string = input("Insert your target e.g Videos:\t")
        # get the target directory
        target_dir = get_directory(target_string.capitalize())
        
        destination_string = input("Insert your Destination Folder e.g Videos:\t")
        # get the destination folder
        destination_dir = get_directory(destination_string.capitalize())
        # turn it into a POSIX path object
        target_directory = Path(target_dir)
        destination_directory = Path(destination_dir)

        #check if the both files exist
        print(path_exists(target_directory, destination_directory))
    except KeyboardInterrupt:
        print("\nOops you cancelled, come again some other time :)")


