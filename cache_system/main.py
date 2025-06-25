from hash_table import HashTable

def main():
    cache = HashTable()

    print("{Asset Cache System (Film Pipeline Demo)}")
    print("-----------------------------------------")

    # command line menu 
    while True:
        print("\nChoose an option:")
        print("1. Put (add/update asset)")
        print("2. Get (retrieve asset)")
        print("3. Delete (remove asset)")
        print("4. View cache contents")
        print("5. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == "1":
            key = input("Enter shot-task key (e.g., SHOT_014_ANIM): ")
            value = input("Enter asset path (e.g., cache/anim/shot_014/charA_cache_v03.abc): ")
            cache.put(key, value)
            print(f">> Cached: [{key}] > {value}")

        elif choice == "2":
            key = input("Enter key to retrieve: ")
            result = cache.get(key)
            if result:
                print(f">> Found: {result}")
            else:
                print("[Error] Key not found.")

        elif choice == "3":
            key = input("Enter key to delete: ")
            success = cache.delete(key)
            if success:
                print(f">> Deleted: {key}")
            else:
                print("[Error] Key not found.")

        elif choice == "4":
            cache.display()

        elif choice == "5":
            print("Exiting.")
            break

        else:
            print("[Error] Invalid choice. Try again.")

if __name__ == "__main__":
    main()