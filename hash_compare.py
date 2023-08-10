import hashlib

# Color codes for styling
class Color:
    GREEN = '\033[92m'
    RED = '\033[91m'
    END = '\033[0m'

def print_header():
    print("-----------------------------------------")
    print("           Hash Comparison Tool          ")
    print("-----------------------------------------")

def compare_hashes(hash1, hash2):
    return hash1 == hash2

def main():
    print_header()

    while True:
        print("\nOptions:")
        print("1. Match two hash values")
        print("2. Match a file's content with a hash value")
        print("3. Match a file's content with another file's content")
        print("4. Exit")
        
        choice = input("Select an option (1/2/3/4): ")

        if choice == '1':
            hash1 = input("Enter the first hash value: ").strip()
            hash2 = input("Enter the second hash value: ").strip()

            if compare_hashes(hash1, hash2):
                print(Color.GREEN + "Hashes match!" + Color.END)
            else:
                print(Color.RED + "Hashes do not match." + Color.END)

        elif choice == '2':
            hash_algorithms = {
                1: "md5",
                2: "sha1",
                3: "sha256",
		4: "sha512",
		5: "sha3_256",
		6: "sha3_512"
                # you ---> Add other hash algorithms...
            }

            print("Available hash algorithms:")
            for num, algorithm in hash_algorithms.items():
                print(f"{num}. {algorithm}")

            selected_algorithm = None
            while selected_algorithm not in hash_algorithms:
                try:
                    selected_algorithm = int(input("Enter the number for the hash algorithm you want to use: "))
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            hash_to_compare = input("Enter the hash value to compare: ")
            filename = input("Enter the path to the file: ")

            try:
                with open(filename, "rb") as file:
                    content = file.read()
                    hash_type = hash_algorithms[selected_algorithm]
                    hash_object = hashlib.new(hash_type)
                    hash_object.update(content)
                    computed_hash = hash_object.hexdigest()

                    if compare_hashes(computed_hash, hash_to_compare):
                        print(Color.GREEN + "Hashes match!" + Color.END)
                    else:
                        print(Color.RED + "Hashes do not match." + Color.END)

            except FileNotFoundError:
                print("File not found. Make sure to provide the correct file path.")

        elif choice == '3':
            file1 = input("Enter the path to the first file: ")
            file2 = input("Enter the path to the second file: ")

            try:
                with open(file1, "rb") as f1, open(file2, "rb") as f2:
                    content1 = f1.read()
                    content2 = f2.read()

                    if compare_hashes(content1, content2):
                        print(Color.GREEN + "File contents match!" + Color.END)
                    else:
                        print(Color.RED + "File contents do not match." + Color.END)

            except FileNotFoundError:
                print("File not found. Make sure to provide the correct file paths.")

        elif choice == '4':
            exit_choice = input("Are you sure you want to exit? (y/n): ")
            if exit_choice.lower() == 'y':
                print("Exiting...")
                break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

