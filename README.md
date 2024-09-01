    # Google Motion Photo Splitter

    A Python script to extract still images and videos from Google Motion Photos.

    ## Description

    This tool processes Google Motion Photos, splitting them into separate JPEG (still image) and MP4 (video) files. It works with motion photos taken on Google Pixel phones and other devices using the Google Camera app.

    ## Requirements

    - Python 3.6 or higher

    ## Usage

    Run the script from the command line:

    ```sh
    python splitter.py <file_path_or_pattern>
    ```

    Examples:

    ```sh
    python splitter.py path/to/your/file.jpg
    python splitter.py "path/to/your/*.jpg"
    ```

    ## Output

    For each motion photo, the script creates:

    - `<original_filename>_photo.jpg`: The still image
    - `<original_filename>_video.mp4`: The motion video

    ## Features

    - Non-destructive: Original files are not modified
    - Batch processing: Can handle multiple files using wildcards
    - Cross-platform: Works on Windows, macOS, and Linux

    ## Acknowledgements

    Developed based on insights from this [Stack Exchange discussion](https://android.stackexchange.com/questions/196831/how-do-i-view-google-cameras-motion-photos-on-my-windows-pc).

    ## Contributing

    Contributions, issues, and feature requests are welcome. Check the [issues page](../../issues) to contribute.
