# media-tools

Small, focused tools for managing a media library. First tool converts FLAC to MP3 while mirroring directory structure.

## Tools

### `flac2mp3.py`
Walks a source directory of `.flac` files and writes `.mp3` files to a destination directory, preserving the folder structure. Skips files that already exist.

#### Requirements
- ffmpeg (path configurable via `--ffmpeg`)
- Python 3.8+

#### Usage (Unraid)
```bash
python3 scripts/flac2mp3.py \
	--src /mnt/user/media/media_files/_FLAC \
	--dst /mnt/user/media/media_files/flac_to_mp3 \
	--ffmpeg /usr/local/bin/ffmpeg/ffmpeg \
	--bitrate 320k \
	--dry-run

brew install ffmpeg
python3 scripts/flac2mp3.py \
	--src /path/to/FLAC \
	--dst /path/to/MP3
