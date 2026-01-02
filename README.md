# Auto Accept Queue for League of Legends

Small script/notebook that monitors the screen and automatically clicks the League of Legends "Accept" button when a match is found.


## Installation
This project uses `uv` for dependency management. To install the required packages, run the following command in the project root:
```bash
uv pip sync
```
This will install all the dependencies specified in the `pyproject.toml` file.

If you don't have `uv` installed, you can install it with pip:
```bash
pip install uv
```

## Quick start
- Run the notebook cell that calls `main()`.

## How it works
- The script uses image recognition to find `popup.png` on screen and clicks its location when detected.

## Notes & warnings
- The image must match your client resolution/theme and the client must be visible and not obscured.
- Automation may require additional OS permissions for screenshots/clicks.
- Use responsibly and in accordance with Riot Games' terms of service — this may violate their rules.
