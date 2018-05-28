import sys
import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument("FILE", type=str)
args = parser.parse_args()

if len(sys.argv) == 2:
    if os.path.isfile(sys.argv[1]):
        print("HexDump of the file", sys.argv[1])
        try:
            with open(args.FILE, "rb") as x:
                j = 0
                k = x.read(16)

                while k:
                    s1 = " ".join([f"{i:02x}" for i in k])  # hex values

                    s2 = "".join([chr(i) if 32 <= i <= 127 else "." for i in
                                  k])  # ascii values of the content and replacing nonprintable characters with dot

                    snew = s1.replace(" ", "")  # removing spaces

                    # printing the final result
                    print(
                        f"{j * 16:08x}  {snew[0:4]} {snew[4:8]} {snew[8:12]} {snew[12:16]} {snew[16:20]} {snew[20:24]} {snew[24:28]} {snew[28:32]} {s2}")

                    j += 1
                    k = x.read(16)

        except Exception as e:
            print(__file__, ": ", type(e).__name__, " - ", e, sep="", file=sys.stderr)
    else:
        print("file is not found")
else:
    print("Enter only one file at a time")