# ComputerGraphicsHW

A small Python script for video processing. Created during the "Computer Graphics" course at HSE University.

Task: Given a video with a static background, people appear in some frames. The goal is to automatically remove all frames containing people.

Script description:
The script takes the original video, selects a reference frame (at the 2nd second), and keeps only the portions of the video that match this reference frame. The output is a new video without the unwanted fragments.

## Dependencies
```bash
pip install moviepy Pillow
```

## Usage
1. Place the file `input.mp4` next to the script.
2. Run:
```bash
python main.py
```
3. The result will be saved as `output.mp4`.

You can modify the input and output file names in the code, as well as the parameter `a` — the slicing step (default is 0.5 seconds). Smaller `a` means more precise comparison but longer processing time.

## Example Output
- Input: `input.mp4`
- Reference frame saved as `ref.png`
- Output: `output.mp4`

