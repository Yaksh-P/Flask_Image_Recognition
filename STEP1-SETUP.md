# Step 1 - Local application setup

Original project: https://github.com/Sachin-crypto/Flask_Image_Recognition

The original application source and model are unchanged for this setup step.
The exact upstream revision is recorded in `evidence/upstream-commit.txt`.

## Environment

The computer initially had Python 3.14 only. TensorFlow 2.10 requires an older
interpreter, so Python 3.10.11 was installed in `.python310` in this project.
A separate `.venv` contains project packages. Neither directory belongs in Git.

From PowerShell in this folder:

```powershell
.\.python310\python.exe -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe -m pip check
.\.venv\Scripts\python.exe -m flask --app app run --port 9000
```

Open http://127.0.0.1:9000 and choose a hand-sign photograph from `test_images`.
Click Submit and verify a digit appears. These are hand-sign photographs, not
handwritten digit images.

## Compatibility constraints

The instructor's original `requirements.txt` remains unchanged. The added
`requirements-dev.txt` includes it and constrains Werkzeug to 2.2.3 because
Flask 2.2.1 uses `url_quote`, which Werkzeug 3 removed. Protobuf 3.19.6 preserves
the older API expected by TensorFlow 2.10. Quality tools are installed now for
later steps; application refactoring and new tests have not started.

## GitHub status

Individual fork: https://github.com/Yaksh-P/Flask_Image_Recognition

`origin` points to this individual fork. `upstream` points to the instructor's
repository. Setup work is committed separately from later application changes.

## Evidence

Only actual execution results and screenshots will be recorded in `evidence`.
An application startup alone does not prove prediction works.

Verified locally on October 23, 2026:

- `pip check`: No broken requirements found.
- Flask home page: HTTP 200.
- A real multipart upload of `test_images/4/Sign 4 (92).jpeg` through the Flask
  test client returned HTTP 200 and displayed digit **4**, using the trained
  model (no mock). Full output: `evidence/real-prediction.txt`.
- Server started on http://127.0.0.1:9000 with debug mode off.
- TensorFlow reported missing CUDA libraries and continued on the CPU.
- The user verified the home page and prediction **4** in Chrome and saved two
  screenshots in `evidence`: `Screenshot 2026-10-23 183506.png` (home) and
  `Screenshot 2026-10-23 183754.png` (prediction).
- A request to port 9000 initially timed out despite a listening process.
  Duplicate assignment server launches were stopped and a single server was
  started. Actual HTTP requests then returned 200 for both home and prediction;
  the user subsequently confirmed the full browser workflow.

The two saved screenshots provide the required 2-3 application screenshots.
Keep them for the final report. They remain local because the home screenshot
also includes unrelated browser tabs. Live server logs and generated response
HTML remain local; selected execution evidence is saved in the repository.

