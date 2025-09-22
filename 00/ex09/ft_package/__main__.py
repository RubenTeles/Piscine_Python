from ft_package import count_in_list

def main():
    list_to_test = ["toto", "tata", "toto"]
    item_to_count_1 = "toto"
    item_to_count_2 = "tutu"
    
    print(f"Counting '{item_to_count_1}' in {list_to_test}: {count_in_list(list_to_test, item_to_count_1)}")
    print(f"Counting '{item_to_count_2}' in {list_to_test}: {count_in_list(list_to_test, item_to_count_2)}")

if __name__ == "__main__":
    main()