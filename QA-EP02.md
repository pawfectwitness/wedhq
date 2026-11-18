# EP02 launch QA

Updated 18 November 2026. This replaces the earlier signed-out verification blocker.

## Scope and routes

The approved V37 design and subsequent existing site improvements are retained. Shared EP02 data renders the homepage, the combined Podcast/episodes route `/episodes`, and `/episode-002`. EP01 now uses the supplied original thumbnail on its archive card and landing page, with matching share metadata. Existing EP01 listening links are unchanged.

## Completed verification

- EP02 title, host Q蚊, Cantonese, duration 27:26 and supplied summary verified.
- Both supplied artwork files preserved byte-for-byte; both thumbnails loaded successfully on the hosted preview.
- EP02 YouTube and Spotify links, disabled Apple button without URL, canonical/OG metadata and PodcastEpisode data checked.
- EP01 remains accessible with its existing listening links.
- Favicons and permanent anonymous-submission disclaimer retained.
- Desktop layout, 390px mobile layout, mobile menu, episode search and series filters checked in Chromium.
- Local build succeeds. Source and published form definitions match, including POST, data-netlify and hidden form-name fields. Existing route files remain present.

## Authenticated Netlify Forms verification

Real submissions were made through authenticated Deploy Preview #2 on 18 November 2026; this was not a simulation or a success-message-only test.

| Form and flow | Front-end receipt | Netlify backend | Notification delivery |
| --- | --- | --- | --- |
| scenario-submission: desktop, submission-only | Passed | Correct Verified record with complete fields | Actual notification received in configured inbox |
| event-notification: 390px viewport | Passed | Correct Verified record with email and role | Actual notification received in configured inbox |
| scenario-submission: 390px viewport, follow-up contact | Passed | Correct Verified record including contact field | Actual notification received in configured inbox |

Both forms' Verified and Spam queues were inspected. Test records were in Verified, not Spam. Form detection is enabled. Both existing notification rules were inspected and left unchanged; delivery was verified independently in the recipient inbox. Test content was clearly identified as QA. Existing records were not changed or deleted. Private recipient details and submission contents are intentionally excluded from this public report.

## Receipt validation review

Both handlers await the shared forms.js transport before showing success. It requires an OK response with the current default Netlify receipt phrase and rejects generic homepage/form/login HTML. All three legitimate hosted submissions passed; backend records and actual delivered notifications corroborated those results. A local POST without a Netlify backend correctly produced an error rather than false success.

The validator intentionally supports the current default English Netlify receipt. A future custom, localized or empty success response requires updating validation to avoid false rejection. A receipt alone does not guarantee future storage or email delivery.

## Coverage limits and release approval

Physical iPhone/Safari, interrupted/offline submission, every possible spam-filter outcome and future custom receipt formats were not tested. Production form submissions have not been exercised; authenticated hosted-preview submissions have.

The owner explicitly approved production publication conditional on final QA passing on 18 November 2026. Final deployment status and live-route checks will be reported after the production deployment. No unrelated changes are in scope.
