# EP02 launch preview

Source: approved V37 layout, compared with the current main branch a4a410b (later EP01/platform/SEO/favicon improvements retained).

## Routes

- `/`: newest episode feature now EP02.
- `/episodes`: the existing Podcast page and episodes listing are the **same route**. Original introduction, platform follow links, search and series filters retained; EP02 latest feature and archive card added before EP01. No separate `/podcast` route exists (404 on current production).
- `/episode-002`: uses EP01's header, typography, spacing, player and platform controls; supplied EP02 artwork used unchanged. Apple Podcasts is a real disabled button without any URL.
- `/episode-001`: original content, Spotify, YouTube, Apple URLs unchanged. Added the missing existing mobile-menu script.

Episode content is defined in `data/episodes.json` and rendered into static HTML by `tools/build-episodes.py`. Metadata remains indexable without client-side JavaScript.

## Verified

- Exact EP02 title, Q蚊, Cantonese, 27:26, both summary paragraphs.
- Source artwork matches the supplied PNG byte-for-byte.
- EP02 YouTube and Spotify hrefs, disabled Apple markup, canonical, OG and PodcastEpisode JSON-LD.
- EP01 content unchanged except the shared menu script.
- Favicons were already present and retained.
- Permanent anonymous-submission disclaimer added beside the submission form.
- Desktop EP02 visual inspection; 390px mobile iframe layout and mobile navigation tested in the managed browser (Chromium; not a physical iPhone/Safari test).
- Search EP02 hides EP01; series filter interactions checked.
- Actual local form POST receives HTTP 501 because this preview intentionally has no Netlify backend: UI correctly shows error, keeps the form and does not show success.
- JavaScript syntax checks and static content/schema assertions passed.

## Form limitation / release blocker

The old handler treated **any HTTP 2xx** as success, even a fallback homepage. Both forms now share a conservative handler that requires the Netlify receipt text and rejects returned form/homepage HTML. This guards false positives, but is **not proof of a stored submission or email delivery**.

Netlify Deploy Preview #2 built successfully, but its existing Team Protection requires a signed-in invited Netlify account. The connected browser was signed out. Consequently a real hosted submission, Verified/Spam list entry, and notification email have NOT been verified. Do not claim the mobile delivery issue resolved, and do not approve production until those checks pass. Check both form names (`scenario-submission`, `event-notification`), form detection, verified/spam queues and email notifications with an authenticated account.

Do not merge PR #2 or deploy production until Kit explicitly approves the preview. No production source branch or deployment changed.
