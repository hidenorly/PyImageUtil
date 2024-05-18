#   Copyright 2023, 2024 hidenorly
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import argparse
import os

from ImageUtil import ImageUtil

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='convert .heic to .jpeg', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i", "--input", action='append', default=["."], help="Input folder path")
    parser.add_argument("-o", "--output", default=".", help="output folder path")
    parser.add_argument("-n", "--noJpegIfFallback", default=False, action="store_true", help="Specify if you want no jpeg in case of fallback")
    parser.add_argument("-d", "--deleteIfSuccess", default=False, action="store_true", help="Specify if you want to delete source .HEIC files")
    args = parser.parse_args()

    imgPaths = []
    for anInput in args.input:
        if os.path.exists(anInput):
            if os.path.isdir(anInput):
                for dirpath, dirnames, filenames in os.walk(anInput):
                    for filename in filenames:
                        # convert required image
                        if filename.endswith(('.heic', '.HEIC')):
                            imgPaths.append( os.path.join(dirpath, filename) )
            else:
                imgPaths.append(anInput)

    convertSuccessFiles = []
    for inputPath in imgPaths:
        outFilename = ImageUtil.covertToJpeg(inputPath, args.output, True, args.noJpegIfFallback)
        if outFilename:
            convertSuccessFiles.append(inputPath)

    if args.deleteIfSuccess:
        for aPath in convertSuccessFiles:
            try:
                os.remove(aPath)
            except:
                pass