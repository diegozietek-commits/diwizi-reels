# WFA Digital — pending changes (handover note)

Not a Diwizi document. Parked here only because it is the durable store this session has;
the WFA Digital routine lives in a different session and does not read this repo. Paste this
into that session when you find it.

WFA Digital publishes through the **same PostProxy token** as Diwizi.
Instagram profile id: `ZDUr85`. No new credentials needed.

## What Diego asked for (2026-08-09 and 2026-08-11)

1. **Stop posting raw job listings.** They read as a classifieds feed. Move to content that is
   interesting on its own: remote-work **statistics** and **curiosities**, friendlier in tone.
   People who are not applying today should still want to follow.

2. **Drop the red background.** Diego: "nao quero mais fundo vermelho, quero algo mais sobrio."
   The red gradient job card is the specific thing he objected to. Sober palette instead.

3. **Link in the comments, not in the bio** — on Instagram and Facebook. The caption should point
   down to it ("link below"), not to a bio. On LinkedIn the URL is clickable inline in the post,
   so no comment is needed there. Current WFA posts still end with "link in bio" / "See this and
   more open roles: link in bio."

4. **Stop printing the "Public domain." credit line.** Diego, 2026-08-11: "nao precisa mais
   mencionar 'Public domain.' dos proximos posts." Seen on:
     - `kZtOvDL` (Instagram, 2026-08-07) — Katsushika Hokusai, "Six women seated around a bird
       cage". Public domain.
     - `o7t0ewq` (LinkedIn, 2026-08-04) — Ridolfo Ghirlandaio, "Portrait of a Gentleman".
       Public domain.
   Note the paintings really are public domain and legally need no credit, so removing the line
   is safe. If that routine ever switches to a source that DOES require attribution (most stock
   libraries do not, but some CC licences do), the credit has to come back.

## Worth stealing from the Diwizi routine

`socialkit_image_posts.py` in this repo already solves several problems that routine will hit:

- **Per-platform copy.** PostProxy sends one `post.body` per request, so different wording per
  platform requires separate calls per profile set. See `publish_image_post`.
- **LinkedIn company page.** Without `organization_id` the post lands on the personal profile.
  Diwizi's is 28874141; WFA will have its own. There is a hard guard in `publish_image_post`.
- **Photo reuse guard.** `used_photos.json` plus `photo_is_free()` / `record_photo_use()`, so the
  same image never appears on two posts.
- **Style parity.** Counting PostProxy records breaks once a run writes more than one record
  (Diwizi hit this when LinkedIn was added). Count runs, not records. See `count_diwizi_runs`.
