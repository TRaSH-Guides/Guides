document$.subscribe(function() {
  console.log("Script loaded and running.");

  const announceElement = document.querySelector('[data-md-component="announce"] .md-banner__inner');

  if (announceElement) {
    const canonicalUrlElement = document.querySelector('link[rel="canonical"]');

    if (canonicalUrlElement) {
      const currentUrl = window.location.href;
      const canonicalHref = canonicalUrlElement.href;

      const normalizeUrl = (url) => {
        let normalized = url.replace(/\/+$/, '');
        return normalized;
      };

      const normalizedCurrentUrl = normalizeUrl(currentUrl);
      const normalizedCanonicalHref = normalizeUrl(canonicalHref);

      if (normalizedCurrentUrl !== normalizedCanonicalHref) {
        announceElement.style.display = 'block';
      }
    } else {
      return;
    }
  }
});
