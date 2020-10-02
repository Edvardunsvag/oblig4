import argparse
from .. import grayscale_image as gray
from .. import sepia_image as sepia


def main():
    parser = argparse.ArgumentParser(
        description="This is the interface description", add_help=False)
    parser.add_argument("-h", "--help", action="help", default=argparse.SUPPRESS,
                        help="helpful message showing flags and usage of instapy")
    parser.add_argument(
        '-f', '--file', action='store', required=True, help="The file you wish to apply effect to")
    parser.add_argument(
        '-se', '--sepia', action='store_true', help="Select sepia filter")
    parser.add_argument(
        '-g', '--gray', action='store_true', help="Select gray filter")
    parser.add_argument(
        '-Sc', '--scale', type=float, help="Scale factor to resize image")
    parser.add_argument(
        '-i', '--implementation', choices=['numpy', 'python', 'cython', 'numba'], help="Choose the implementation", required=True)
    parser.add_argument(
        '-o', '--out', help="The output filename")
    args = parser.parse_args()

    if args.gray:
        gray.grayscale_image(args.file, args.out,
                             args.implementation, args.scale)
    elif args.sepia:
        sepia.sepia_image(args.file, args.out,
                          args.implementation, args.scale)
