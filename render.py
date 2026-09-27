"""Build the self-contained portfolio from bundled assets."""
import base64
from pathlib import Path
ROOT = Path(__file__).resolve().parent

def build_page():
    assets = ROOT
    template = (assets / 'portfolio.html').read_text(encoding='utf-8')
    image = base64.b64encode((assets / 'hero-ribbon.png').read_bytes()).decode('ascii')
    resume = base64.b64encode((assets / 'Mahima_Thakar_Resume.pdf').read_bytes()).decode('ascii')
    return template.replace('__HERO_IMAGE__', 'data:image/png;base64,' + image).replace('__RESUME_BASE64__', resume)

if __name__ == '__main__':
    (ROOT / 'preview.html').write_text(build_page(), encoding='utf-8')
    print('Open preview.html in your browser.')
