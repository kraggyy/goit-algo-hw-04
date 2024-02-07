def get_cats_info(path):
    cats_info = []

    try:   
        with open(path, "r") as fh:
            for line in fh:
                cat_id, cat_name, cat_age = line.strip().split(",")
                cat_dict = {"id":cat_id, "name":cat_name, "age":cat_age}
                cats_info.append(cat_dict)
            return cats_info
    except FileNotFoundError:
        print("File not found")
    except FileExistsError:
        print("File not exixt")

print(get_cats_info("./task2.txt"))