/* Shared Netlify transport. A generic 2xx page is not a form receipt. */
(function (root) {
  function isNetlifyReceipt(response, html) {
    if (!response.ok || response.redirected) return false;
    const doc = new DOMParser().parseFromString(html, 'text/html');
    // Reject a rewrite to our homepage, a login page, or a bot challenge.
    if (doc.querySelector('form, .site-header, [name="password"]')) return false;
    return /your form submission has been received/i.test(doc.body.textContent || '');
  }
  async function submit(form) {
    const data = new FormData(form);
    if (data.get('form-name') !== form.name) throw new Error('Invalid form identity');
    const body = new URLSearchParams();
    data.forEach((value, key) => body.append(key, String(value)));
    const response = await fetch('/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'text/html' },
      credentials: 'same-origin', cache: 'no-store', body: body.toString()
    });
    const receipt = await response.text();
    if (!isNetlifyReceipt(response, receipt)) throw new Error('No confirmed Netlify receipt');
  }
  root.WedHQForms = { submit, isNetlifyReceipt };
})(window);
