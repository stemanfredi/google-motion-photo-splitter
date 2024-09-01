import os
import glob
import sys


def process_motion_photo(file_path):
    print(f"Processing: {file_path}")

    file_size = os.path.getsize(file_path)
    print(f"\tFile size: {file_size}")

    with open(file_path, "rb") as f:
        data = f.read()

    mp4_start_pos = data.find(b"ftyp")

    if mp4_start_pos != -1:
        mp4_start_pos -= 4  # The real beginning of the mp4 starts 4 bytes before "ftyp"

        jpg_end_pos = data.rfind(b"\xFF\xD9", 0, mp4_start_pos)

        if jpg_end_pos != -1:
            jpg_end_pos += 2  # Account for the length of the search string

            output_base = os.path.splitext(file_path)[0]

            print("\tSaving photo...")
            with open(f"{output_base}_photo.jpg", "wb") as f:
                f.write(data[:jpg_end_pos])

            print("\tSaving video...")
            with open(f"{output_base}_video.mp4", "wb") as f:
                f.write(data[mp4_start_pos:])
        else:
            print(
                "\tSKIPPING - File appears to contain an MP4 but no valid JPG EOI segment could be found."
            )
    else:
        print("\tSKIPPING - File does not appear to be a Google motion photo.")


def main(args):
    print("Scanning for files...")

    files_to_process = []
    for arg in args:
        if "*" in arg or "?" in arg:
            # If the argument contains wildcards, use glob
            files_to_process.extend(glob.glob(arg))
        else:
            # Otherwise, add the file directly
            files_to_process.append(arg)

    if not files_to_process:
        print(f"No files found matching the given patterns.")
        return

    for file in files_to_process:
        if os.path.isfile(file) and file.lower().endswith((".jpeg", ".jpg")):
            process_motion_photo(file)

    print("Done.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(
            "Usage: python splitter.py <file_path_or_pattern> [<file_path_or_pattern> ...]"
        )
        sys.exit(1)

    main(sys.argv[1:])
