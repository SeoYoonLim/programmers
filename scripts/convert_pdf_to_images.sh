#!/usr/bin/env bash
set -euo pipefail

if [[ "${1:-}" == "" ]]; then
  echo "Usage: $0 /workspace/assets/<file>.pdf [dpi]" >&2
  exit 1
fi

PDF_PATH="$1"
DPI="${2:-200}"

if ! command -v pdftoppm >/dev/null 2>&1; then
  echo "Error: 'pdftoppm' not found. Please install poppler-utils (apt-get install -y poppler-utils)." >&2
  exit 1
fi

if [[ ! -f "$PDF_PATH" ]]; then
  echo "Error: PDF not found at $PDF_PATH" >&2
  exit 1
fi

BASENAME="$(basename "$PDF_PATH")"
NAME_NO_EXT="${BASENAME%.*}"
OUT_DIR="/workspace/assets/images/$NAME_NO_EXT"
mkdir -p "$OUT_DIR"

echo "Converting '$PDF_PATH' -> '$OUT_DIR/page-#.png' at ${DPI} DPI..."
# pdftoppm names pages as prefix-1.png, prefix-2.png ...
pdftoppm -png -r "$DPI" "$PDF_PATH" "$OUT_DIR/page" >/dev/null

COUNT=$(ls -1 "$OUT_DIR"/page-*.png 2>/dev/null | wc -l | tr -d ' ')
if [[ "$COUNT" == "0" ]]; then
  echo "No images were generated. Please check the PDF file." >&2
  exit 1
fi

echo "Done. Generated $COUNT images in $OUT_DIR"