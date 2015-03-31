# -*- coding: utf-8 -*-

from postgres_access import factory


def main():
    repo = factory.create_APARepository()
    print "Adding Data"
    for count in xrange(5):
        repo.put("value:{} added".format(count))

    print "Read all data"
    for ele in repo.find_all():
        print "Element id:{} value:{}".format(ele[0], ele[1])

if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print "FAILS: ", exc

