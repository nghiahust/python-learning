def format_customer(first, last, *loc):
    if loc:
        print("{0} {1} ({2})".format(first, last, *loc))
    else:
        print("{0} {1}".format(first, last, loc))