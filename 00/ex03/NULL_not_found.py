def NULL_not_found(object: any) -> int:
    try:
        if object is None:
            print("Nothing:", object, type(object))
        elif isinstance(object, float) and object != object:
            print("Cheese:", object, type(object))
        elif isinstance(object, int) and object == 0:
            print("Zero:", object, type(object))
        elif isinstance(object, str) and object == "":
            print("Empty:", object, type(object))
        elif isinstance(object, bool) and object is False:
            print("Fake:", object, type(object))
        else:
            raise ValueError("Type not Found")
        return 0
    except Exception as e:
        print(e)
        return 1
