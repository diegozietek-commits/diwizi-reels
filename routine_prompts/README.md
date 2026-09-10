# Routine prompts, kept here so they survive a container reset

These are the live prompts of the two Diwizi social Routines, saved verbatim.
The containers these routines run in are ephemeral, so a prompt that exists only
inside a scheduled session is lost the moment that session ends. Reconstructing
one from scratch means losing every correction Diego has accumulated, so it is
mirrored here instead.

| file | Routine | trigger id | schedule (UTC) |
|---|---|---|---|
| `insight-mon-wed-fri.md`    | diwizi-reels-3x-week        | `trig_01VWH63vVVKLtUf6Fc769mCK` | `0 16 * * 1,3,5` |
| `commercial-tue-thu-sat.md` | diwizi-social-posts-3x-week | `trig_01Jo24KRnemTbXmXYpKe2CUA` | `0 13 * * 2,4,6` |

**These files are a mirror, not the source of truth.** The Routine's stored prompt is
what actually runs. If you edit a file here, push the same text to the trigger with
`mcp__Claude_Code_Remote__update_trigger`; if you change a trigger, update the file in
the same commit. A copy that has silently drifted is worse than no copy at all.
