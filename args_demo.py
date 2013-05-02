import argparse


def main():
    parser = argparse.ArgumentParser(description='Gather settings for time '
                                     'lapse recordings')
    parser.add_argument('-l', '--length', help='Length in minutes for the '
                        'program to run for.', type=int)
    parser.add_argument('-d', '--delay', help='The delay between shots',
                         type=int)
    parser.add_argument('-c', '--clockwise', help='Should the camera initially'
                        'rotate in a clockwise direction.', type=bool)
    parser.add_argument('-a', '--arc', help='The total arc that the camera'
                        'should rotate by', type=int)
    
    args = parser.parse_args()

    print "lenght: %s" % args.length
#     print "lenght: %s" % args.l

if __name__ == "__main__":
    main()