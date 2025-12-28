import base64

from docx import Document

from report_generator import build


# 1x1 transparent PNG for screenshot insertion test
_PNG_BYTES = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO8y+GkAAAAASUVORK5CYII="
)


def test_build_adds_image_when_provided(tmp_path):
    image_path = tmp_path / "shot.png"
    image_path.write_bytes(_PNG_BYTES)
    out_path = tmp_path / "report.docx"

    build(str(out_path), "term", "klass", "sid", "name", "teacher", image=str(image_path))

    doc = Document(out_path)
    assert len(doc.inline_shapes) == 1
