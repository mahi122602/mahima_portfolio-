"""Render the portfolio with iframe-safe internal navigation."""
import base64
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def asset_path(name):
    """Support both GitHub root uploads and the original assets folder."""
    for folder in (ROOT, ROOT / 'assets'):
        candidate = folder / name
        if candidate.is_file():
            return candidate
    raise FileNotFoundError(f'Please upload {name} beside render.py or inside assets/.')


NAVIGATION = '''
<script>
(function () {
  document.addEventListener('click', function (event) {
    const link = event.target.closest('a[href^="#"]');
    if (!link) return;
    const fragment = link.getAttribute('href').slice(1);
    if (!fragment) return;
    const target = document.getElementById(fragment);
    if (!target) return;
    event.preventDefault();
    const quiet = window.matchMedia('(prefers-reduced-motion: reduce)').matches
      || document.body.classList.contains('paused');
    target.scrollIntoView({behavior: quiet ? 'instant' : 'smooth', block: 'start'});
    // Keep keyboard navigation in the destination section without a second jump.
    if (!target.hasAttribute('tabindex')) target.setAttribute('tabindex', '-1');
    target.focus({preventScroll: true});
  });
})();
</script>
'''


def build_page():
    template = asset_path('portfolio.html').read_text(encoding='utf-8')
    image = base64.b64encode(asset_path('hero-ribbon.png').read_bytes()).decode('ascii')
    resume = base64.b64encode(asset_path('Mahima_Thakar_Resume.pdf').read_bytes()).decode('ascii')
    page = template.replace('__HERO_IMAGE__', 'data:image/png;base64,' + image)
    page = page.replace('__RESUME_BASE64__', resume)
    return page.replace('</body>', NAVIGATION + '</body>')


if __name__ == '__main__':
    (ROOT / 'preview.html').write_text(build_page(), encoding='utf-8')
    print('Open preview.html in your browser.')
