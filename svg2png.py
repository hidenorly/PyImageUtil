#   Copyright 2023 hidenorly
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
    parser = argparse.ArgumentParser(description='convert .svg to .png', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i", "--input", action='append', default=["."], help="Input folder path")
    parser.add_argument("-o", "--output", default=".", help="output folder path")
    parser.add_argument("-w", "--width", default=1920, help="output width")
    parser.add_argument("-t", "--height", default=1080, help="output height")
    args = parser.parse_args()

    imgPaths = {}
    for anInput in args.input:
        if os.path.exists(anInput):
            if os.path.isdir(anInput):
                for dirpath, dirnames, filenames in os.walk(anInput):
                    for filename in filenames:
                        # convert required image
                        if filename.endswith(('.svg', '.SVG')):
                            outputPath = os.path.join(args.output, ImageUtil.getFilenameWithExt(filename, ".png"))
                            imgPaths[os.path.join(dirpath, filename)] = outputPath
            else:
                imgPaths[anInput] = os.path.join(args.output, ImageUtil.getFilenameWithExt(anInput, ".png"))

    for inputPath, outputPath in imgPaths.items():
        ImageUtil.convertSvgToPng(inputPath, outputPath, args.width, args.height)
