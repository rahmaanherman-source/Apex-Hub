# APEX Free AI Media Stack — 2026-09-23

**Purpose:** one launchpad for free/zero-cost AI media tools that can help produce commercials, product videos, social clips, images, captions and edits.

## Commercial-use rule

**Do not equate "$0" with "commercially cleared."** The registry separates free allowance from commercial rights. Before a commercial export, verify the exact account plan, model, export route, source-media rights and current terms.

## Quick launch table

| Tool | Free access currently documented | Commercial status | Primary use |
|---|---|---|---|
| ImagesArt.ai | 5 credits/day | **YES — listed by provider** | Image + image-to-video |
| ImagineArt | 100 daily credits | **VERIFY** | Image/video generation |
| Pika | 150 credits/month | **NO on Basic/free** | Video/effects |
| Runway | 125 one-time credits | **VERIFY** | Image-to-video |
| Canva Free | Up to 20 AI uses | **YES for permitted Canva content; asset restrictions apply** | Ads/design/video |
| Adobe Express Free | 2 lifetime 5-sec video generations | **VERIFY by feature** | Editing + Firefly |
| HeyGen Free | 3 videos/month | **VERIFY** | Avatar/spokesperson |
| Formats | 10 welcome credits / ~5 min captions | **VERIFY** | Captions/editing |
| ImgAI | Free daily image access + signup/check-in credits | **VERIFY by model/provider** | Image/video/product creative |
| CapCut | Free editor + commercial-use template collection | **CHECK EACH ASSET** | Editing/templates |
| Luma | Limited free web access | **Treat free web as non-commercial unless terms say otherwise** | Image/video |
| Artiroom | 10 credits/month | **NO on free tier** | Image/video ads |
| Image2.im | Up to 2 registration credits | **VERIFY** | Image/video |

## Evidence links

- ImagesArt pricing: https://imagesart.ai/pricing
- ImagineArt video/free tier: https://www.imagine.art/ai-video-generator
- Pika FAQ: https://pika.art/faq
- Runway Free plan: https://help.runwayml.com/hc/en-us/articles/50404627334547-Free-plan-details
- Canva pricing: https://www.canva.com/pricing/
- Canva license: https://www.canva.com/policies/content-license-agreement-2026-04-15/
- Adobe Express pricing: https://www.adobe.com/express/pricing
- HeyGen pricing: https://www.heygen.com/pricing
- Formats pricing: https://www.formats.app/pricing
- ImgAI free credits: https://imgai.ai/free-credits
- ImgAI terms: https://imgai.ai/terms-of-service
- CapCut commercial templates: https://www.capcut.com/explore/for-commercial-use
- Luma FAQ: https://docs.lumalabs.ai/docs/faq
- Artiroom pricing: https://www.artiroom.com/pricing
- Image2 pricing: https://image2.im/pricing

## APEX launch behavior

The launcher should open every provider in a browser tab and show:

1. **FREE ALLOWANCE**
2. **RESET TYPE**
3. **WATERMARK**
4. **COMMERCIAL STATUS**
5. **SOURCE/TERMS**
6. **LAST VERIFIED DATE**

No API keys belong in this registry.

## Recommended local-first additions

Also maintain a second lane for models that can run on your own hardware. Those have no hosted credit quota, but they consume local GPU/CPU/RAM instead:

- Wan-family open-weight video models
- Mochi-family open models
- Local image models through ComfyUI
- Ollama for text/agent orchestration
- Whisper-family local transcription
- FFmpeg for deterministic media processing

**Hosted free credits = testing pool. Local models = no hosted credit meter.**
