# PyImageUtil

```
    imgPaths = []
    for dirpath, dirnames, filenames in os.walk(args.input):
        for filename in filenames:
            # convert required image
            if filename.endswith(('.heic', '.HEIC')):
                filename = ImageUtil.covertToJpeg(os.path.join(dirpath, filename))
```