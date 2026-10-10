# Study0SG Astro Replacement Plan

The current default branch contains a Flask website (`app.py`, `requirements.txt`, `template/`). The new Study0SG Astro application is prepared as a separate source bundle provided in the project conversation, including Home, Team, Events, Minister Honey chat, Supabase/Notion/DeepSeek/R2/Drive helpers, and expandable cards.

## Migration sequence
1. Create a backup tag pointing at the original `main` commit, before replacement.
2. Replace the source tree entirely with the **Study0SG_Astro_Rebuild_Clickable_Cards.zip** contents (copy the files within `study0sg-astro/` to the repo root).
3. Remove legacy `app.py`, `requirements.txt`, `template/`, and previous Flask-only assets.
4. Install Node 20+ and run `npm install`, `npm test`, `npm run check`, and `npm run build`.
5. Store all secret API credentials on the backend host, not in git. Configure Supabase policies before publishing any content.
6. Deploy to a **Node-compatible hosting platform**: GitHub Pages cannot run Astro SSR and its `/api/chat` endpoint.
7. Validate all interactive cards by mouse, touch, keyboard and screen reader. Check focus restoration and Escape to close dialogs.

## Card acceptance criteria
- Home update cards expand to show description and image.
- Current, upcoming and past event cards expand to show complete details and location.
- Team cards expand to show member bios, gallery and contact channels.
- Entire visible cards are clickable; keyboard focus is visible.
- Buttons have descriptive accessible labels; dialog opens with focus inside and closes with Escape.

## Release gate
**Do not merge this draft as a deployment.** This branch currently contains migration planning, not the replacement Astro source tree. First copy in and validate the source bundle described above. Review and test deployment before merging to `main`.
