BUILD REQUEST — APEX PLANT LIVING DESTINATION

You are building the APEX Plant application from the attached/approved visual references and the canonical specification in docs/APEX_PLANT_LIVING_DESTINATION_SPEC.md.

IMPORTANT: treat the supplied visual reference as the canonical landing/front-door direction. Upgrade quality; do not reduce it, replace it with a generic SaaS dashboard, or turn the modules into unrelated pages.

PRODUCT GOAL
Create a premium, welcoming, highly visual plant destination that people have a reason to revisit every day. It combines AI plant intelligence, a plant growth/social feed, local discovery, plant trading, expert help, plant-care records, and commerce.

CORE LOOP
SEE → LEARN → GROW → POST → CONNECT → TRADE/BUY → GET HELP → RETURN

LANDING PAGE
Build ONE coherent landing/front-door experience. Functional modules/tabs live inside the same product workspace. Do not clutter the first screen with every capability.

The landing page should prominently feature:
1. WHAT'S GROWING TODAY? — a daily-changing featured plant.
2. PLANT OF THE WEEK — weekly featured plant with community submissions and challenges.
3. GROW — short-form plant growth videos/posts.
4. WHAT'S HAPPENING NOW? — fresh daily activity.
5. Local plant discovery/trades.
6. Experts available for help.
7. A clear My Plants entry point.

Use premium imagery, strong typography, tasteful liquid-glass-style UI, excellent spacing, responsive design, and high-quality transitions. The design should feel alive rather than like a database.

DAILY RETURN ENGINE
Every day, surface fresh content such as:
- featured plant
- new growth posts
- challenges
- local trades
- experts available
- local events
- relevant plant/care alerts
- availability/deals when verified data exists

PLANT OF THE WEEK
Make it participatory:
- community submissions
- best growth
- best collection
- best photo
- best care story
- best new grower
- challenge countdown
Never invent winners, counts, reviews, prices, or availability.

AI PLANT CHECK
Allow photo upload/camera input. Return:
- likely plant identity
- visible symptoms
- water/light/soil/fertilizer guidance
- pests/weeds observations
- seasonality
- planting order
- companion/incompatible plant warnings, including underground/root competition where relevant
- likely causes
- confidence
- escalation when uncertain

Never represent uncertain AI output as guaranteed professional diagnosis.

GROW FEED
Users can post short growth content. A post may include plant identity, timeline, care information, propagation, optional location, and actions for trade/buy/help.

Include an AI growth-story workflow that can turn a sequence of user photos into a short visual story/video with user-controlled captions/music/style.

PLANT CARE NETWORK
Let qualified/experienced plant people create profiles showing:
- identity verification status
- credential/evidence status
- specialties
- portfolio
- reviews/references
- service area
- pricing
- availability
- insurance information where applicable

Keep identity verification separate from credential verification.

REMOTE EXPERT CONSULTATION
Make video consultation a first-class option:
- choose a time
- supported video workflow; FaceTime can be offered where technically appropriate
- transparent consultation fee
- expert records findings/recommendations
- no home entry required

OPTIONAL PHYSICAL SERVICES
In-home care, boarding, pickup/drop-off, and trusted-circle care may exist, but never assume a customer wants a stranger inside their home.

LOCAL + COMMERCE
Where authorized location data is available, show nearby:
- plants
- nurseries
- garden centers
- supplies
- growers
- trades/cuttings
- events

Show multiple reasonable options and transparent prices when available. Do not automatically favor the most expensive option.

PLANT CARE PASSPORT
Let users keep:
- plant photo/identity
- acquired/planted date
- care schedule
- light/soil/water requirements
- growth history
- photos
- observations/diagnoses
- treatments
- fertilizer history
- propagation records
- owner-approved care instructions

For services, capture evidence of what happened.

MONEY LINES
Connect monetization directly to value:
- free AI check
- paid expert video consultation
- local professional services
- plant/supply commerce
- premium collection features
- justified subscriptions/tiers
- events/community opportunities

Do not manufacture problems to create sales.

UX RULE
Use progressive disclosure and minimize taps. Suggested primary modules:
Discover | My Plants | Grow | Experts | Local | Trade | Challenges

Do not turn these into seven disconnected websites.

TECHNICAL/PRODUCT RULES
- Inspect the existing project before modifying it.
- Preserve working APEX architecture and existing functionality.
- Do not invent external data.
- Use explicit unavailable states when live data is not connected.
- Keep location sharing opt-in.
- Keep provider integrations replaceable.
- Build a production-quality vertical slice first, then expand.
- Include real loading, empty, error, permission, and success states.
- Do not use fake metrics as if they were real.
- Do not claim a service, payment, map, video, AI model, or marketplace integration works until it is actually wired and tested.

ACCEPTANCE TEST
The build passes only if:
1. The landing page is one coherent premium plant destination.
2. Daily content can change.
3. Plant of the Week works.
4. Grow supports short-form growth content.
5. Photo-based AI plant check works or clearly reports unavailable integration.
6. AI uncertainty is visible.
7. Human video consultation can be requested.
8. Local discovery works when authorized data is connected.
9. Plant trade flow exists.
10. Plant Care Passport works.
11. No giant cluttered all-feature dashboard appears.
12. Desktop/mobile are usable.
13. External-data claims are evidence-backed.
14. Commercial actions can be traced from discovery to purchase/service request.
15. The supplied visual direction remains recognizable and is improved, not degraded.

FINAL INSTRUCTION
Do not give me a mockup that merely says these features exist. Build the functional experience. If a backend/API/key/provider is missing, implement the interface and explicit integration boundary, report the exact blocker, and do not fake completion.