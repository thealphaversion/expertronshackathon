def check_validity(num):
    try:
        mobile = int(num)
        if len(num) != 10:
            return "NOT VALID"
        if num[0] == 7 or num[0] == 8 or num[0] == 9:
            return "VALID"
        return "NOT VALID"
    except:
        return "NOT VALID"

if __name__ == "__main__":
    mobile_num = input()
    result = check_validity(mobile_num)
    print(result)