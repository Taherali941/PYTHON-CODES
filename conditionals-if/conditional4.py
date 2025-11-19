age = 25
has_license = True

if age >= 18:
    print("You are old enough to drive.")
    if has_license:
        print("You have a valid license")
    else:
        print("You are old enough, but you need a license to drive legally.")
else:
    print("You are not old enough to drive.")