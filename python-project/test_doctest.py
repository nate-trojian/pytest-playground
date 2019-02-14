def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))

def success():
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")


if __name__ == "__main__":
    import doctest
    t = doctest.testmod()
    if t.failed:
        fail()
    else:
        success()
