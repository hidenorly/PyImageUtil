# PyImageUtil

```
    imgPaths = []
    for dirpath, dirnames, filenames in os.walk(args.input):
        for filename in filenames:
            # convert required image
            if filename.endswith(('.heic', '.HEIC')):
                filename = ImageUtil.covertToJpeg(os.path.join(dirpath, filename))
```

# trouble shoot

## ffi.error

```
  File "/opt/homebrew/lib/python3.12/site-packages/pyheif/reader.py", line 402, in _read_heif_image
    p_options.ignore_transformations = int(not heif_file.apply_transformations)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ffi.error: struct heif_decoding_options: wrong total size (cdef says 48, but C compiler says 72). fix it or use "...;" as the last field in the cdef for struct heif_decoding_options to make it flexible
```

Workaround for the above:

```
def _read_heif_image(handle, heif_file):
..snip..
    p_options = _libheif_cffi.ffi.gc(
        p_options, _libheif_cffi.lib.heif_decoding_options_free
    )
-   p_options.ignore_transformations = int(not heif_file.apply_transformations)
-   p_options.convert_hdr_to_8bit = int(heif_file.convert_hdr_to_8bit)
+   try:
+       p_options.ignore_transformations = int(not heif_file.apply_transformations)
+       p_options.convert_hdr_to_8bit = int(heif_file.convert_hdr_to_8bit)
+   except:
+       pass

    p_img = _libheif_cffi.ffi.new("struct heif_image **")
```

use try-catch for the above p_options...
