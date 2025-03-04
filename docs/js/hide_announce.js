document$.subscribe(function() {
  console.log("Script loaded and running.");

  const announceElement = document.querySelector('[data-md-component="announce"] .md-banner__inner');

  if (announceElement) {
    console.log("Announce element found:", announceElement);

    const canonicalUrlElement = document.querySelector('link[rel="canonical"]');

    if (canonicalUrlElement) {
      const currentUrl = window.location.href;
      const canonicalHref = canonicalUrlElement.href;

      console.log("Current URL:", currentUrl);
      console.log("Canonical URL:", canonicalHref);

      const getBaseUrl = (url) => {
        try {
          const urlObj = new URL(url);
          return `${urlObj.hostname}`;
        } catch (error) {
          console.error("Invalid URL:", url, error);
          return null;
        }
      };

      const currentBaseUrl = getBaseUrl(currentUrl);
      const canonicalBaseUrl = getBaseUrl(canonicalHref);

      if (currentBaseUrl && canonicalBaseUrl) {
        console.log("Current Base URL:", currentBaseUrl);
        console.log("Canonical Base URL:", canonicalBaseUrl);

        if (currentBaseUrl !== canonicalBaseUrl) {
          console.log("Base URLs do NOT match. Showing announce element.");
          announceElement.style.display = 'block';
        } else {
          console.log("Base URLs match. Element remains hidden (as set by CSS).");
        }
      } else {
        console.log("Could not extract base URL. Check URLs or browser console.");
      }

    } else {
      console.log("Canonical URL element NOT found. Is a canonical URL set?");
      return;
    }
  } else {
    console.log("Announce element NOT found. Check your selector.");
  }
});
